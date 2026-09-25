# Validation: indi_w9_s3

Log: `/home/trananhduy/quadplane-indi/rework/runs/noisy_wind/indi_w9_s3/flight.BIN`  
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
| Q_M_THST_HOVER | 0.30527380108833313 |
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
- transition_start: 17.3
- transition_done: 37.0
- back_transition: 120.4
- position2: 124.1
- land_complete: 171.9
- disarm: 171.9

## Phases

| phase | start | end | dur (s) | INDI on motors (% time) | INDI on surfaces (% time) |
|---|---|---|---|---|---|
| hover_takeoff | -0.0 | 17.3 | 17.3 | 92.8 | 0.0 |
| transition | 17.3 | 37.0 | 19.7 | 100.0 | 0.0 |
| fixed_wing | 37.0 | 120.4 | 83.4 | 10.1 | 89.6 |
| back_transition | 120.4 | 124.1 | 3.7 | 92.9 | 0.1 |
| hover_land | 124.1 | 171.9 | 47.8 | 100.0 | 0.0 |

## Attitude tracking (desired - actual, deg)

| phase | roll RMS | roll max | pitch RMS | pitch max | yaw RMS | yaw max |
|---|---|---|---|---|---|---|
| hover_takeoff | 0.15 | 0.54 | 0.32 | 1.74 | 3.90 | 93.61 |
| transition | 1.74 | 5.61 | 2.32 | 12.02 | - | - |
| fixed_wing | 10.44 | 43.32 | 4.28 | 38.28 | - | - |
| back_transition | 0.30 | 0.83 | 1.14 | 1.76 | - | - |
| hover_land | 0.84 | 7.11 | 1.07 | 8.56 | 1.03 | 8.70 |

## VTOL rate loop (PIQx target - actual, deg/s)

| phase | roll RMS | pitch RMS | yaw RMS | roll peak Hz | roll >5 Hz share / RMS (deg/s) | pitch peak Hz | pitch >5 Hz share / RMS (deg/s) |
|---|---|---|---|---|---|---|---|
| hover_takeoff | 1.10 | 2.47 | 22.26 | 0.14 | 0.20 / 0.831 | 1.88 | 0.15 / 0.853 |
| transition | 3.69 | 4.97 | 1.95 | 0.13 | 0.07 / 0.959 | 0.25 | 0.01 / 0.443 |
| back_transition | 1.47 | 2.21 | 0.85 | 1.36 | 0.30 / 0.633 | 0.23 | 0.03 / 0.152 |
| hover_land | 4.63 | 6.17 | 3.20 | 0.12 | 0.07 / 0.841 | 0.09 | 0.01 / 0.783 |

## VTOL height and motors

| phase | alt err RMS (m) | alt err max (m) | climb err RMS (m/s) | motor mean (0-1) | motor max | % any motor at max | % any motor at min |
|---|---|---|---|---|---|---|---|
| hover_takeoff | 0.09 | 0.42 | 0.34 | [0.552, 0.707, 0.628, 0.753] | [0.915, 0.95, 0.866, 0.95] | 0.0 | 8.78 |
| transition | 0.31 | 1.26 | 0.32 | [0.303, 0.47, 0.533, 0.658] | [0.704, 0.773, 0.771, 0.892] | 0.0 | 29.82 |
| back_transition | 0.49 | 0.64 | 0.63 | [0.175, 0.208, 0.184, 0.218] | [0.25, 0.278, 0.254, 0.306] | 0.0 | 100.0 |
| hover_land | 0.68 | 2.50 | 0.86 | [0.413, 0.448, 0.455, 0.494] | [0.734, 0.827, 0.752, 0.824] | 0.0 | 26.44 |

## Fixed-wing

### transition

- airspeed min/mean/max: 9.0 / 12.0 / 15.0 m/s; TECS speed-demand tracking RMS 5.29 m/s
- nav roll/pitch tracking RMS (CTUN): 1.75 / 2.32 deg (max 5.60 / 12.02)
- FW rate loop (PIDR/PIDP) RMS: 3.68 / 4.97 deg/s
- TECS height error RMS / max: 1.20 / 2.29 m
- cross-track RMS / max: 0.00 / 0.00 m
- throttle mean/max: 69.9 / 77.9 % (0.0 % of samples at max)
- VTOL assist active: 100.0 % of time; lift motors above idle: 100.0 % of samples

### fixed_wing

- airspeed min/mean/max: 10.9 / 16.0 / 19.1 m/s; TECS speed-demand tracking RMS 1.68 m/s
- nav roll/pitch tracking RMS (CTUN): 10.51 / 4.30 deg (max 43.31 / 36.40)
- FW rate loop (PIDR/PIDP) RMS: 2.47 / 5.38 deg/s
- TECS height error RMS / max: 2.87 / 8.46 m
- cross-track RMS / max: 25.41 / 75.97 m
- throttle mean/max: 81.0 / 100.0 % (4.1 % of samples at max)
- VTOL assist active: 10.4 % of time; lift motors above idle: 11.8 % of samples

## Mode changes

- 0.0 s: QHOVER
- 1.1 s: AUTO

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
- 1.1 s: Mission: 1 Takeoff
- 3.1 s: Weathervane Active: nose in
- 17.3 s: Mission: 2 WP
- 17.3 s: Transition started airspeed 9.5
- 34.0 s: Transition airspeed reached 14.0
- 37.0 s: Transition done
- 43.3 s: Reached waypoint #2 dist 26m
- 43.3 s: Mission: 3 CondYaw
- 43.3 s: Mission: 4 WP
- 43.3 s: Skipping invalid cmd #115
- 55.2 s: Reached waypoint #4 dist 24m
- 55.2 s: Mission: 5 WP
- 64.2 s: Transition started airspeed 12.8
- 69.9 s: Transition airspeed reached 14.0
- 72.9 s: Transition done
- 83.4 s: Reached waypoint #5 dist 25m
- 83.4 s: Mission: 6 Land
- 83.4 s: VTOL approach d=257.6
- 120.4 s: VTOL airbrake v=6.1 d=21 sd=22 h=35.4
- 124.1 s: VTOL position1 v=5.0 d=2.6 h=36.3 dc=2.9
- 124.1 s: VTOL position2 started v=5.0 d=2.6 h=36.3
- 129.9 s: Weathervane Active: nose in
- 133.3 s: Land descend started
- 156.4 s: Land final started
- 171.9 s: Land complete
- 171.9 s: Throttle disarmed
- 177.3 s: PreArm: In landing sequence
- 177.3 s: PreArm: Auto missing takeoff waypoint

![overview](validation.png)
