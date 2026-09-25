# Validation: indi_w9_s1

Log: `/home/trananhduy/quadplane-indi/rework/runs/noisy_wind/indi_w9_s1/flight.BIN`  
Mission completed (landed + disarmed): **True**

## Parameters read back from the log

| param | value |
|---|---|
| Q_ENABLE | 1.0 |
| Q_OPTIONS | 0.0 |
| Q_ASSIST_SPEED | 13.0 |
| AHRS_EKF_TYPE | 10.0 |
| SIM_WIND_SPD | 0.0 |
| AIRSPEED_CRUISE | 17.0 |
| AIRSPEED_MIN | 14.0 |
| AIRSPEED_STALL | 12.0 |
| Q_A_RAT_RLL_P | 0.699999988079071 |
| Q_A_RAT_RLL_I | 0.699999988079071 |
| Q_A_RAT_RLL_D | 0.029999999329447746 |
| Q_A_RAT_RLL_FF | 0.0 |
| Q_A_RAT_PIT_P | 0.30000001192092896 |
| Q_A_RAT_PIT_I | 0.30000001192092896 |
| Q_A_RAT_PIT_D | 0.02500000037252903 |
| Q_A_RAT_PIT_FF | 0.0 |
| Q_A_RAT_YAW_P | 4.0 |
| Q_A_RAT_YAW_I | 0.4000000059604645 |
| Q_A_RAT_YAW_D | 0.10000000149011612 |
| Q_A_ANG_RLL_P | 4.5 |
| Q_A_ANG_PIT_P | 4.5 |
| Q_A_ANG_YAW_P | 1.520650029182434 |
| RLL_RATE_P | 0.14106599986553192 |
| RLL_RATE_I | 0.17587700486183167 |
| RLL_RATE_D | 0.0015910000074654818 |
| RLL_RATE_FF | 0.17587700486183167 |
| PTCH_RATE_P | 0.2803190052509308 |
| PTCH_RATE_I | 0.8886290192604065 |
| PTCH_RATE_D | 0.004360999912023544 |
| PTCH_RATE_FF | 0.8886290192604065 |
| Q_M_PWM_MIN | 1000.0 |
| Q_M_PWM_MAX | 2000.0 |
| Q_M_SPIN_MIN | 0.15000000596046448 |
| Q_M_THST_HOVER | 0.30494028329849243 |
| Q_INDI_ENABLE | 1.0 |
| Q_INDI_AXES | 27.0 |
| Q_INDI_FILT_HZ | 12.699999809265137 |
| Q_INDI_RLL_K | 13.5 |
| Q_INDI_PIT_K | 13.5 |
| Q_INDI_RLL_G | 56.70000076293945 |
| Q_INDI_PIT_G | 44.79999923706055 |
| Q_INDI_ACT_TC | 0.0 |
| Q_INDI_ACT_DLY | 0.004000000189989805 |
| Q_INDI_FW_RLL_G | 16.700000762939453 |
| Q_INDI_FW_PIT_G | 12.399999618530273 |
| Q_INDI_FW_TC | 0.009999999776482582 |
| Q_INDI_FW_RLL_K | 10.5 |
| Q_INDI_FW_PIT_K | 10.5 |

## Events (s from log start)

- arm: -0.0
- transition_start: 17.9
- transition_done: 37.7
- back_transition: 120.5
- position2: 124.1
- land_complete: 171.9
- disarm: 171.9

## Phases

| phase | start | end | dur (s) | INDI on motors (% time) | INDI on surfaces (% time) |
|---|---|---|---|---|---|
| hover_takeoff | -0.0 | 17.9 | 17.9 | 92.6 | 0.0 |
| transition | 17.9 | 37.7 | 19.8 | 100.0 | 0.0 |
| fixed_wing | 37.7 | 120.5 | 82.8 | 9.8 | 89.8 |
| back_transition | 120.5 | 124.1 | 3.6 | 92.7 | 0.1 |
| hover_land | 124.1 | 171.9 | 47.8 | 100.0 | 0.0 |

## Attitude tracking (desired - actual, deg)

| phase | roll RMS | roll max | pitch RMS | pitch max | yaw RMS | yaw max |
|---|---|---|---|---|---|---|
| hover_takeoff | 0.46 | 2.92 | 0.31 | 1.71 | 3.84 | 93.55 |
| transition | 1.76 | 5.81 | 2.36 | 12.12 | - | - |
| fixed_wing | 10.45 | 43.64 | 4.04 | 33.56 | - | - |
| back_transition | 0.32 | 0.60 | 1.01 | 1.59 | - | - |
| hover_land | 0.97 | 8.30 | 1.15 | 11.48 | 1.10 | 9.16 |

## VTOL rate loop (PIQx target - actual, deg/s)

| phase | roll RMS | pitch RMS | yaw RMS | roll peak Hz | roll >5 Hz share / RMS (deg/s) | pitch peak Hz | pitch >5 Hz share / RMS (deg/s) |
|---|---|---|---|---|---|---|---|
| hover_takeoff | 4.30 | 2.42 | 22.01 | 0.11 | 0.06 / 1.056 | 1.45 | 0.10 / 0.706 |
| transition | 3.80 | 4.97 | 2.01 | 0.13 | 0.07 / 0.946 | 0.21 | 0.01 / 0.458 |
| back_transition | 0.94 | 2.07 | 0.63 | 1.37 | 0.50 / 0.596 | 0.23 | 0.03 / 0.139 |
| hover_land | 5.22 | 6.91 | 3.39 | 0.12 | 0.06 / 0.844 | 0.09 | 0.00 / 0.400 |

## VTOL height and motors

| phase | alt err RMS (m) | alt err max (m) | climb err RMS (m/s) | motor mean (0-1) | motor max | % any motor at max | % any motor at min |
|---|---|---|---|---|---|---|---|
| hover_takeoff | 0.08 | 0.42 | 0.34 | [0.547, 0.694, 0.609, 0.737] | [0.912, 0.95, 0.87, 0.95] | 0.0 | 10.49 |
| transition | 0.31 | 1.26 | 0.34 | [0.308, 0.472, 0.529, 0.655] | [0.729, 0.782, 0.741, 0.87] | 0.0 | 30.91 |
| back_transition | 0.52 | 0.69 | 0.66 | [0.169, 0.207, 0.177, 0.22] | [0.243, 0.274, 0.245, 0.276] | 0.0 | 100.0 |
| hover_land | 0.70 | 2.50 | 0.90 | [0.417, 0.452, 0.458, 0.5] | [0.709, 0.827, 0.767, 0.823] | 0.0 | 26.57 |

## Fixed-wing

### transition

- airspeed min/mean/max: 9.0 / 12.0 / 15.0 m/s; TECS speed-demand tracking RMS 5.30 m/s
- nav roll/pitch tracking RMS (CTUN): 1.75 / 2.35 deg (max 5.65 / 12.09)
- FW rate loop (PIDR/PIDP) RMS: 3.79 / 4.97 deg/s
- TECS height error RMS / max: 1.19 / 2.28 m
- cross-track RMS / max: 0.00 / 0.00 m
- throttle mean/max: 70.1 / 77.7 % (0.0 % of samples at max)
- VTOL assist active: 100.0 % of time; lift motors above idle: 100.0 % of samples

### fixed_wing

- airspeed min/mean/max: 11.3 / 16.0 / 19.0 m/s; TECS speed-demand tracking RMS 1.59 m/s
- nav roll/pitch tracking RMS (CTUN): 10.37 / 4.02 deg (max 42.89 / 33.28)
- FW rate loop (PIDR/PIDP) RMS: 2.49 / 4.74 deg/s
- TECS height error RMS / max: 2.75 / 7.97 m
- cross-track RMS / max: 25.26 / 75.74 m
- throttle mean/max: 81.0 / 100.0 % (4.2 % of samples at max)
- VTOL assist active: 10.2 % of time; lift motors above idle: 11.26 % of samples

## Mode changes

- 0.0 s: QHOVER
- 1.2 s: AUTO

## Autopilot messages

- -0.0 s: Throttle armed
- 0.0 s: ArduPlane V4.8.0-dev (7fa89979)
- 0.0 s: 158c274630044e33ab0c21188889c480
- 0.0 s: Param space used: 77/3840
- 0.0 s: RC Protocol: UDP
- 0.0 s: New mission
- 0.0 s: New rally
- 0.0 s: New fence
- 0.0 s: QuadPlane Frame: QUAD/X
- 0.0 s: GPS 1: probing for u-blox at 230400 baud
- 1.2 s: Mission: 1 Takeoff
- 3.2 s: Weathervane Active: nose in
- 17.9 s: Mission: 2 WP
- 17.9 s: Transition started airspeed 9.0
- 34.7 s: Transition airspeed reached 14.0
- 37.7 s: Transition done
- 43.9 s: Reached waypoint #2 dist 25m
- 43.9 s: Mission: 3 CondYaw
- 43.9 s: Mission: 4 WP
- 43.9 s: Skipping invalid cmd #115
- 55.8 s: Reached waypoint #4 dist 24m
- 55.8 s: Mission: 5 WP
- 64.8 s: Transition started airspeed 13.0
- 70.2 s: Transition airspeed reached 14.0
- 73.2 s: Transition done
- 83.7 s: Reached waypoint #5 dist 26m
- 83.7 s: Mission: 6 Land
- 83.7 s: VTOL approach d=257.4
- 120.5 s: VTOL airbrake v=6.2 d=21 sd=22 h=35.2
- 124.1 s: VTOL position1 v=5.0 d=2.5 h=35.9 dc=3.0
- 124.1 s: VTOL position2 started v=5.0 d=2.5 h=35.9
- 130.0 s: Weathervane Active: nose in
- 133.4 s: Land descend started
- 156.3 s: Land final started
- 171.9 s: Land complete
- 171.9 s: Throttle disarmed
- 177.3 s: PreArm: In landing sequence
- 177.3 s: PreArm: Auto missing takeoff waypoint

![overview](validation.png)
