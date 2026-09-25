# Real flight reference: `realflight.bin`

Context only - not compared run by run with the simulation.

## Flight modes

- 0.2-0.3 s (0.1 s): QHOVER
- 0.3-104.7 s (104.3 s): QHOVER
- 104.7-113.1 s (8.4 s): FBWA - GPS ground speed mean 3.7 / max 5.9 m/s
- 113.1-157.5 s (44.4 s): QHOVER

## Hover

- airborne (QTUN ThO > 0.2): 85.9-125.9 s
- hover throttle (ThO) mean 0.410, Q_M_THST_HOVER 0.408

## Settings: real aircraft vs SITL file

| param | real | SITL |
|---|---|---|
| SCHED_LOOP_RATE | 300 | 400 (differs) |
| INS_GYRO_FILTER | 42 | 20 (differs) |
| INS_HNTCH_ENABLE | 1 | 0 (differs) |
| INS_HNTCH_FREQ | 122 | - |
| Q_M_THST_HOVER | 0.408294 | 0.298002 (differs) |
| Q_M_THST_EXPO | 0.6 | 0.65 (differs) |
| Q_M_SPIN_MIN | 0.15 | 0.15 |
| Q_M_SPIN_MAX | 0.95 | 0.95 |
| Q_A_RAT_RLL_P | 0.16 | 0.7 (differs) |
| Q_A_RAT_RLL_I | 0.16 | 0.7 (differs) |
| Q_A_RAT_RLL_D | 0.0052294 | 0.03 (differs) |
| Q_A_RAT_PIT_P | 0.298692 | 0.3 (differs) |
| Q_A_RAT_PIT_I | 0.298692 | 0.3 (differs) |
| Q_A_RAT_PIT_D | 0.00334997 | 0.025 (differs) |
| Q_A_RAT_YAW_P | 0.5 | 4 (differs) |
| Q_A_RAT_YAW_I | 0.05 | 0.4 (differs) |
| Q_A_ANG_RLL_P | 4.5 | 4.5 |
| Q_A_ANG_PIT_P | 4.5 | 4.5 |
| RLL_RATE_P | 0.08 | 0.141066 (differs) |
| RLL_RATE_I | 0.15 | 0.175877 (differs) |
| RLL_RATE_FF | 0.345 | 0.175877 (differs) |
| PTCH_RATE_P | 0.04 | 0.280319 (differs) |
| PTCH_RATE_I | 0.15 | 0.888629 (differs) |
| PTCH_RATE_FF | 0.345 | 0.888629 (differs) |
| ARSPD_TYPE | 0 | 2 (differs) |
| AIRSPEED_CRUISE | 17 | 20.8333 (differs) |
