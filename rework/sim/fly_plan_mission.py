#!/usr/bin/env python3
"""Fly a QGroundControl .plan file in AUTO and report whether it completed.

The validation campaign flies `sim/square.plan`: VTOL take-off, a closed
250 m square circuit at 35 m, and a VTOL landing back at the take-off point.
A closed circuit is what makes a single steady wind vector a complete
disturbance case - it is a crosswind from the left on one leg, a headwind on
the next, a crosswind from the right on the third and a tailwind on the
fourth, so one run exercises every relative wind direction with the same
airframe, the same controller and the same navigation gains.

Reading the mission from the .plan file rather than hard-coding waypoints
means the figure of the desired path and the mission the aircraft actually
flew come from the same source, and the plan can be edited in QGC without
touching this harness.

Connect straight to SITL's TCP port rather than through MAVProxy: MAVProxy's
own waypoint module races the mission upload and makes ArduPilot report
"Mission upload timeout" / OPERATION_CANCELLED.

Writes a JSON summary so a batch runner can decide whether the run is worth
analysing without a human reading the console.
"""
import argparse
import json
import math
import os
import subprocess
import threading
import time

from pymavlink import mavutil


def load_plan(path):
    """Return (home_lat, home_lon, home_alt, items) from a QGC .plan file.

    `items` is a list of MISSION_ITEM_INT argument tuples starting at seq 1.
    Sequence 0 is reserved by AP_Mission for the home slot and is filled in
    by the caller: AP_Mission::set_current_cmd() silently redirects index 0
    to index 1, so a real nav command placed there would never execute.
    """
    with open(path) as fh:
        plan = json.load(fh)

    mission = plan["mission"]
    home = mission["plannedHomePosition"]

    items = []
    for seq, entry in enumerate(mission["items"], start=1):
        if entry.get("type") != "SimpleItem":
            raise ValueError(
                "%s: item %d is %r; only SimpleItem is supported"
                % (path, seq, entry.get("type")))
        p = list(entry["params"]) + [0] * (7 - len(entry["params"]))
        # QGC stores lat/lon as floats in params[4]/params[5] and altitude in
        # params[6]. MISSION_ITEM_INT wants lat/lon as 1e7 integers. A null
        # (used for "no yaw constraint" in param4) has to become a number.
        p = [0.0 if v is None else float(v) for v in p]
        items.append((
            seq,
            int(entry["frame"]),
            int(entry["command"]),
            0,                                   # current
            1 if entry.get("autoContinue", True) else 0,
            p[0], p[1], p[2], p[3],
            int(round(p[4] * 1e7)),
            int(round(p[5] * 1e7)),
            p[6],
        ))
    return float(home[0]), float(home[1]), float(home[2]), items


def plan_extent_m(items):
    """Largest distance between any two waypoints, metres.

    Reported so the run log records the scale of the circuit next to the
    navigation settings it was flown with; a waypoint acceptance radius that
    is a large fraction of the leg length cuts the corners off the path
    regardless of how well the attitude loop tracks.
    """
    pts = [(it[9] * 1e-7, it[10] * 1e-7) for it in items if it[9] or it[10]]
    if len(pts) < 2:
        return 0.0
    best = 0.0
    for i, (la1, lo1) in enumerate(pts):
        for la2, lo2 in pts[i + 1:]:
            dn = (la2 - la1) * 111_320.0
            de = (lo2 - lo1) * 111_320.0 * math.cos(math.radians(la1))
            best = max(best, math.hypot(dn, de))
    return best


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--connect", default="tcp:127.0.0.1:5760")
    ap.add_argument("--plan", required=True, help="QGroundControl .plan file to fly")
    ap.add_argument("--case", default="run")
    ap.add_argument("--status-out", default=None)
    ap.add_argument("--disturb-nm", type=float, default=0.0,
                    help="size of the roll/pitch moment pulses in N.m (0 = none); "
                         "see sim/disturb.py")
    ap.add_argument("--timeout", type=float, default=900.0,
                    help="seconds to wait for the mission to finish")
    args = ap.parse_args()

    home_lat, home_lon, home_alt, plan_items = load_plan(args.plan)
    print("plan %s: %d items, extent %.0f m, home %.7f %.7f"
          % (args.plan, len(plan_items), plan_extent_m(plan_items), home_lat, home_lon))

    status = dict(case=args.case, plan=args.plan, armed=False, auto=False,
                  completed=False, reason="", max_airspeed=0.0, max_alt=0.0,
                  max_nav_roll_deg=0.0, max_nav_pitch_deg=0.0,
                  transitioned=False, landed=False, waypoints_reached=0)

    # source_system must equal MAV_GCS_SYSID (255): heartbeats from any other
    # system id do not count for the GCS failsafe, which then fires ~15 s after
    # arming and switches to QLAND.
    master = mavutil.mavlink_connection(args.connect, source_system=255)
    print("waiting for heartbeat...")
    if master.wait_heartbeat(timeout=60) is None:
        status["reason"] = "no heartbeat"
        _write(args.status_out, status)
        raise SystemExit("no heartbeat from SITL")
    print("heartbeat from sys %u comp %u" % (master.target_system, master.target_component))

    # Keep a GCS heartbeat going for the whole run. Without it the vehicle
    # declares a GCS failsafe part way through the mission and diverts to
    # QLAND, which ends the run before the transition happens.
    stop_hb = threading.Event()

    def _heartbeat():
        while not stop_hb.is_set():
            try:
                master.mav.heartbeat_send(
                    mavutil.mavlink.MAV_TYPE_GCS,
                    mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
            except Exception:
                pass
            # 10 Hz of wall time: the simulation can run many times faster
            # than real time, and the GCS failsafe counts vehicle time
            stop_hb.wait(0.1)

    threading.Thread(target=_heartbeat, daemon=True).start()

    def send(cmd, *params):
        p = list(params) + [0] * (7 - len(params))
        master.mav.command_long_send(master.target_system, master.target_component,
                                     cmd, 0, *p)

    def set_mode(name):
        master.mav.set_mode_send(master.target_system,
                                 mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
                                 master.mode_mapping()[name])

    def show_text(m):
        txt = m.text if isinstance(m.text, str) else m.text.decode(errors='replace')
        print("  STATUSTEXT:", txt)
        return txt

    def drain(seconds):
        """Read and print STATUSTEXT for a while.

        Pre-arm refusals only ever appear as STATUSTEXT, so without this a
        rejected arm gives a numeric result and no reason.
        """
        t0 = time.time()
        seen = []
        while time.time() - t0 < seconds:
            m = master.recv_match(type='STATUSTEXT', blocking=True, timeout=0.5)
            if m is not None:
                seen.append(show_text(m))
        return seen

    def wait_ack(cmd, timeout=10):
        t0 = time.time()
        while time.time() - t0 < timeout:
            m = master.recv_match(type=['COMMAND_ACK', 'STATUSTEXT'],
                                  blocking=True, timeout=1)
            if m is None:
                continue
            if m.get_type() == 'STATUSTEXT':
                show_text(m)
                continue
            if m.command == cmd:
                return m.result
        return None

    # Wait for a usable position estimate before touching the mission.
    print("waiting for EKF/GPS...")
    t0 = time.time()
    while time.time() - t0 < 120:
        m = master.recv_match(type='GPS_RAW_INT', blocking=True, timeout=2)
        if m is not None and m.fix_type >= 3:
            break
    else:
        status["reason"] = "no GPS fix"
        _write(args.status_out, status)
        raise SystemExit("no 3D fix")
    time.sleep(5)

    R = mavutil.mavlink
    home_item = (0, R.MAV_FRAME_GLOBAL, R.MAV_CMD_NAV_WAYPOINT, 0, 1, 0, 0, 0, 0,
                 int(round(home_lat * 1e7)), int(round(home_lon * 1e7)), home_alt - 1.0)
    mission = [home_item] + plan_items

    master.mav.mission_clear_all_send(master.target_system, master.target_component)
    # mission_clear_all_send() triggers its own MISSION_ACK; consume it or the
    # upload loop below reads it as the upload-complete ack.
    master.recv_match(type='MISSION_ACK', blocking=True, timeout=5)

    master.mav.mission_count_send(master.target_system, master.target_component, len(mission))
    uploaded = 0
    t0 = time.time()
    while uploaded < len(mission) and time.time() - t0 < 30:
        m = master.recv_match(type=['MISSION_REQUEST_INT', 'MISSION_REQUEST', 'MISSION_ACK'],
                              blocking=True, timeout=3)
        if m is None:
            continue
        if m.get_type() == 'MISSION_ACK':
            break
        master.mav.mission_item_int_send(master.target_system, master.target_component,
                                         *mission[m.seq])
        uploaded += 1
    master.recv_match(type='MISSION_ACK', blocking=True, timeout=5)
    print("uploaded %d/%d mission items" % (uploaded, len(mission)))
    if uploaded < len(mission):
        status["reason"] = "mission upload incomplete (%d/%d)" % (uploaded, len(mission))
        _write(args.status_out, status)
        raise SystemExit(status["reason"])

    set_mode('QHOVER')
    drain(3)

    # Ask for the pre-arm report explicitly so any refusal is on the record
    # before the arm attempt rather than only as a numeric result code.
    print("arming...")
    reasons = []
    res = None
    for attempt in range(1, 4):
        send(mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 1)
        res = wait_ack(mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM)
        if res == 0:
            break
        reasons = drain(4)
        print("  arm attempt %d rejected (result %s)" % (attempt, res))
    if res != 0:
        detail = "; ".join(r for r in reasons if "rearm" in r.lower() or "Arm" in r)
        status["reason"] = "arm rejected (result %s) %s" % (res, detail)
        _write(args.status_out, status)
        raise SystemExit(status["reason"])
    status["armed"] = True
    time.sleep(0.5)

    print("AUTO...")
    set_mode('AUTO')
    status["auto"] = True

    dist = Disturbance(master, args.disturb_nm) if args.disturb_nm > 0 else None
    status["disturb_nm"] = args.disturb_nm
    status["pulses"] = []

    t0 = time.time()
    last_print = 0.0
    armed = True
    while time.time() - t0 < args.timeout:
        if dist is not None:
            fired = dist.update()
            if fired:
                status["pulses"].append(dict(t=round(time.time() - t0, 2), **fired))
        m = master.recv_match(blocking=True, timeout=0.02)
        if m is None:
            continue
        t = m.get_type()
        if t == 'ATTITUDE' and dist is not None:
            dist.attitude = (m.roll, m.pitch, m.yaw)
            dist.now = m.time_boot_ms * 1e-3
        if t == 'VFR_HUD':
            status["max_airspeed"] = max(status["max_airspeed"], float(m.airspeed))
            status["max_alt"] = max(status["max_alt"], float(m.alt))
            if m.airspeed > 15.0:
                status["transitioned"] = True
        elif t == 'MISSION_CURRENT':
            status["waypoints_reached"] = max(status["waypoints_reached"], int(m.seq))
        elif t == 'NAV_CONTROLLER_OUTPUT':
            status["max_nav_roll_deg"] = max(status["max_nav_roll_deg"],
                                             abs(float(m.nav_roll)))
            status["max_nav_pitch_deg"] = max(status["max_nav_pitch_deg"],
                                              abs(float(m.nav_pitch)))
        elif t == 'HEARTBEAT':
            armed_now = bool(m.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)
            if armed and not armed_now:
                status["landed"] = True
                status["completed"] = True
                status["reason"] = "disarmed after landing"
                break
            armed = armed_now
        elif t == 'STATUSTEXT':
            txt = show_text(m)
            if dist is not None:
                dist.on_text(txt)
            if 'Crash' in txt or 'CRASH' in txt:
                status["reason"] = "crash detected: " + txt
                break

        now = time.time() - t0
        if now - last_print > 20:
            last_print = now
            print("  t=%.0fs wp=%d aspd_max=%.1f alt_max=%.0f transitioned=%s"
                  % (now, status["waypoints_reached"], status["max_airspeed"],
                     status["max_alt"], status["transitioned"]))

    if not status["completed"] and not status["reason"]:
        status["reason"] = "timeout after %.0fs" % args.timeout

    if dist is not None:
        dist.close()
    stop_hb.set()
    print(json.dumps(status, indent=1))
    _write(args.status_out, status)


class Disturbance:
    """Roll then pitch moment pulses at fixed points of the mission.

    Each window starts a set delay after an autopilot message, so PID and INDI
    get the pulses at the same point of the flight:
        roll  +M for 1 s, 4 s rest, pitch +M for 1 s.
    Timing uses the vehicle clock (ATTITUDE.time_boot_ms), not wall time, so
    the pulses land at the same point when the simulation runs faster than
    real time. (The torque is applied at the next message after the start
    time, i.e. within ~0.1 s of vehicle time.)
    The torque itself is applied in Gazebo by sim/disturb.py. While a pulse is
    on, SERVO9 (unused, SERVO9_FUNCTION 0) is set to 1900 (roll) or 1100
    (pitch), else 1500, so RCOU.C9 marks every pulse in the DataFlash log.
    """
    WINDOWS = [                      # (message prefix, delay s, window name)
        ("Mission: 1 Takeoff", 4.0, "hover_takeoff"),
        ("Transition started", 3.0, "transition"),
        ("Reached waypoint #4", 3.0, "fixed_wing"),
        ("Land descend started", 5.0, "hover_land"),
    ]
    MARK_CH, PWM_ROLL, PWM_PITCH, PWM_OFF = 9, 1900, 1100, 1500

    def __init__(self, master, nm):
        self.master, self.nm = master, nm
        self.attitude = (0.0, 0.0, 0.0)
        self.now = 0.0               # vehicle time, s
        self.events = []             # (time, action, window)
        self.used = set()
        here = os.path.dirname(os.path.abspath(__file__))
        self.proc = subprocess.Popen(["/usr/bin/python3", os.path.join(here, "disturb.py")],
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        if self.proc.stdout.readline().strip() != "ready":
            raise SystemExit("disturb.py did not start")
        self._mark(self.PWM_OFF)
        print("disturbance pulses: %.2f N.m" % nm)

    def _send(self, line):
        self.proc.stdin.write(line + "\n")
        self.proc.stdin.flush()
        return self.proc.stdout.readline().strip() == "ok"

    def _mark(self, pwm):
        self.master.mav.command_long_send(
            self.master.target_system, self.master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, self.MARK_CH, pwm, 0, 0, 0, 0, 0)

    def on_text(self, txt):
        for prefix, delay, name in self.WINDOWS:
            if txt.startswith(prefix) and name not in self.used:
                self.used.add(name)
                t = self.now + delay
                self.events += [(t, "roll", name), (t + 1.0, "off", name),
                                (t + 5.0, "pitch", name), (t + 6.0, "off", name)]

    def update(self):
        if not self.events:
            return None
        self.events.sort()
        t, action, name = self.events[0]
        if self.now < t:
            return None
        self.events.pop(0)
        if action == "off":
            ok = self._send("clear")
            self._mark(self.PWM_OFF)
        else:
            L, M = (self.nm, 0.0) if action == "roll" else (0.0, self.nm)
            ok = self._send("body %f %f 0 %f %f %f" % ((L, M) + tuple(self.attitude)))
            self._mark(self.PWM_ROLL if action == "roll" else self.PWM_PITCH)
        print("  pulse %s %s %s" % (name, action, "ok" if ok else "FAILED"))
        return dict(window=name, action=action, ok=ok)

    def close(self):
        try:
            self._send("clear")
            self.proc.stdin.close()
            self.proc.wait(timeout=5)
        except Exception:
            self.proc.kill()


def _write(path, status):
    if path:
        with open(path, 'w') as fh:
            json.dump(status, fh, indent=1)


if __name__ == "__main__":
    main()
