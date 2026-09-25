#!/usr/bin/env bash
# One unattended run: start Gazebo + SITL, fly sim/square.plan in AUTO
# (VTOL take-off -> transition -> square circuit -> VTOL land), stop the sim,
# and copy the DataFlash log out.
#
#   sim/run_square_mission.sh <run-name>
#
# Output: runs/<run-name>/ with world.sdf, params.param, gz/sitl logs,
# mission.log, mission_status.json, logs/*.BIN, and flight.BIN (the log).
# Same environment variables as run_gazebo_sitl.sh (PARAMS, WIND_E, SEED, GUI, ...),
# plus DISTURB_NM: size of the roll/pitch moment pulses in N.m (default 0 = none).
set -euo pipefail

name="${1:?usage: sim/run_square_mission.sh <run-name>}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
[[ "$name" =~ ^[a-zA-Z0-9_-]+$ ]] || { echo "invalid run name: $name" >&2; exit 1; }
run_dir="${RUNS_DIR:-$root/runs}/$name"
rm -rf "$run_dir"
mkdir -p "$run_dir"

trap 'bash "$root/sim/stop_gazebo_sitl.sh"' EXIT

MAVPROXY=0 bash "$root/sim/run_gazebo_sitl.sh" "$run_dir"
sleep 10

python3 -u "$root/sim/fly_plan_mission.py" \
    --connect tcp:127.0.0.1:5760 \
    --plan "$root/sim/square.plan" \
    --case "$name" \
    --status-out "$run_dir/mission_status.json" \
    --disturb-nm "${DISTURB_NM:-0}" \
    2>&1 | tee "$run_dir/mission.log"

python3 - "$run_dir/mission_status.json" "${DISTURB_NM:-0}" <<'PY'
import json
import sys

status = json.load(open(sys.argv[1]))
pulses = status.get("pulses", [])
if not (status.get("completed") and status.get("transitioned")
        and status.get("waypoints_reached", 0) >= 6):
    raise SystemExit("incomplete square mission: " + str(status.get("reason")))
if float(sys.argv[2]) > 0 and (len(pulses) != 16 or not all(p["ok"] for p in pulses)):
    raise SystemExit("missing or failed moment pulses (%d/16)" % len(pulses))
PY

# Let the logger flush after disarm before killing SITL.
sleep 5
bash "$root/sim/stop_gazebo_sitl.sh"
trap - EXIT
sleep 2

bin=$(ls -t "$run_dir"/logs/*.BIN 2>/dev/null | head -1 || true)
if [[ -n "$bin" ]]; then
    cp -f "$bin" "$run_dir/flight.BIN"
    echo "[$name] log: $run_dir/flight.BIN ($(du -h "$bin" | cut -f1))"
else
    echo "[$name] WARNING: no .BIN produced" >&2
    exit 1
fi
