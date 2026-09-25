# PID vs INDI - campaign summary

Runs: 14 (indi_w6_s1, indi_w6_s2, indi_w6_s3, indi_w9_s1, indi_w9_s2, indi_w9_s3, pid_calm_s1, pid_calm_s2, pid_w6_s1, pid_w6_s2, pid_w6_s3, pid_w9_s1, pid_w9_s2, pid_w9_s3). Mean over seeds, [min, max] in brackets. Δ = INDI - PID; "clear" = |Δ| larger than the seed spread of both controllers.

## Missions completed

| ctrl | case | completed / runs |
|---|---|---|
| indi | w6 | 3 / 3 |
| indi | w9 | 3 / 3 |
| pid | calm | 2 / 2 |
| pid | w6 | 3 / 3 |
| pid | w9 | 3 / 3 |

## Per-phase metrics (deg, m, %)

| case | metric | PID | INDI | Δ | clear |
|---|---|---|---|---|---|---|
| calm | hover_takeoff_roll_rms | 0.03 [0.03, 0.03] | - | - | - |
| calm | hover_takeoff_pitch_rms | 0.54 [0.54, 0.54] | - | - | - |
| calm | hover_land_roll_rms | 0.19 [0.05, 0.33] | - | - | - |
| calm | hover_land_pitch_rms | 0.46 [0.35, 0.58] | - | - | - |
| calm | transition_roll_rms | 0.07 [0.07, 0.07] | - | - | - |
| calm | transition_pitch_rms | 1.12 [1.10, 1.14] | - | - | - |
| calm | fixed_wing_roll_rms | 14.87 [14.58, 15.16] | - | - | - |
| calm | fixed_wing_pitch_rms | 1.77 [1.76, 1.79] | - | - | - |
| calm | hover_takeoff_alt_rms | 0.18 [0.18, 0.18] | - | - | - |
| calm | hover_land_alt_rms | 0.66 [0.64, 0.69] | - | - | - |
| calm | hover_land_motor_max_pct | 0.00 [0.00, 0.00] | - | - | - |
| calm | fw_tecs_alt_rms | 1.87 [1.87, 1.87] | - | - | - |
| calm | fw_crosstrack_rms | 11.69 [11.64, 11.74] | - | - | - |
| calm | fw_assist_pct | 0.00 [0.00, 0.00] | - | - | - |
| calm | fw_airspeed_mean | 17.01 [17.00, 17.02] | - | - | - |
| w6 | hover_takeoff_roll_rms | 0.22 [0.15, 0.34] | 0.25 [0.13, 0.34] | +0.03 | no |
| w6 | hover_takeoff_pitch_rms | 1.23 [1.22, 1.24] | 0.32 [0.30, 0.34] | -0.91 | yes |
| w6 | hover_land_roll_rms | 0.27 [0.26, 0.27] | 0.13 [0.13, 0.13] | -0.14 | yes |
| w6 | hover_land_pitch_rms | 0.93 [0.92, 0.94] | 0.48 [0.46, 0.49] | -0.45 | yes |
| w6 | transition_roll_rms | 1.30 [1.29, 1.32] | 1.51 [1.39, 1.75] | +0.21 | no |
| w6 | transition_pitch_rms | 1.76 [1.72, 1.80] | 0.96 [0.77, 1.10] | -0.79 | yes |
| w6 | fixed_wing_roll_rms | 8.81 [8.76, 8.89] | 13.23 [13.16, 13.36] | +4.42 | yes |
| w6 | fixed_wing_pitch_rms | 3.43 [3.38, 3.50] | 4.33 [4.25, 4.50] | +0.90 | yes |
| w6 | hover_takeoff_alt_rms | 0.08 [0.07, 0.08] | 0.08 [0.07, 0.08] | -0.00 | no |
| w6 | hover_land_alt_rms | 0.82 [0.81, 0.82] | 0.70 [0.67, 0.73] | -0.12 | yes |
| w6 | hover_land_motor_max_pct | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | +0.00 | no |
| w6 | fw_tecs_alt_rms | 1.82 [1.80, 1.85] | 2.91 [2.89, 2.93] | +1.09 | yes |
| w6 | fw_crosstrack_rms | 13.95 [13.48, 14.30] | 17.49 [16.98, 18.07] | +3.54 | yes |
| w6 | fw_assist_pct | 57.83 [56.10, 59.50] | 0.00 [0.00, 0.00] | -57.83 | yes |
| w6 | fw_airspeed_mean | 13.55 [13.53, 13.58] | 16.57 [16.53, 16.59] | +3.02 | yes |
| w6 | hover_takeoff_indi_pct | - | 92.87 [92.50, 93.10] | - | - |
| w6 | transition_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w6 | fixed_wing_indf_pct | - | 100.00 [100.00, 100.00] | - | - |
| w6 | hover_land_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w9 | hover_takeoff_roll_rms | 0.29 [0.18, 0.43] | 0.25 [0.14, 0.46] | -0.04 | no |
| w9 | hover_takeoff_pitch_rms | 2.02 [2.00, 2.04] | 0.32 [0.31, 0.32] | -1.71 | yes |
| w9 | hover_land_roll_rms | 0.95 [0.54, 1.16] | 0.98 [0.84, 1.13] | +0.03 | no |
| w9 | hover_land_pitch_rms | 2.58 [2.56, 2.61] | 1.16 [1.07, 1.25] | -1.42 | yes |
| w9 | transition_roll_rms | 2.71 [2.66, 2.75] | 1.70 [1.61, 1.76] | -1.01 | yes |
| w9 | transition_pitch_rms | 3.53 [3.49, 3.59] | 2.25 [2.07, 2.36] | -1.28 | yes |
| w9 | fixed_wing_roll_rms | 11.91 [11.61, 12.20] | 10.45 [10.44, 10.48] | -1.45 | yes |
| w9 | fixed_wing_pitch_rms | 5.45 [5.37, 5.56] | 4.19 [4.04, 4.28] | -1.26 | yes |
| w9 | hover_takeoff_alt_rms | 0.09 [0.08, 0.09] | 0.08 [0.08, 0.09] | -0.00 | no |
| w9 | hover_land_alt_rms | 0.59 [0.58, 0.60] | 0.68 [0.67, 0.70] | +0.09 | yes |
| w9 | hover_land_motor_max_pct | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | +0.00 | no |
| w9 | fw_tecs_alt_rms | 3.46 [3.21, 3.66] | 2.83 [2.75, 2.87] | -0.63 | yes |
| w9 | fw_crosstrack_rms | 37.86 [36.61, 39.68] | 25.45 [25.26, 25.67] | -12.41 | yes |
| w9 | fw_assist_pct | 33.40 [32.40, 34.10] | 10.57 [10.20, 11.10] | -22.83 | yes |
| w9 | fw_airspeed_mean | 14.78 [14.69, 14.88] | 16.02 [15.99, 16.04] | +1.24 | yes |
| w9 | hover_takeoff_indi_pct | - | 92.70 [92.60, 92.80] | - | - |
| w9 | transition_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w9 | fixed_wing_indf_pct | - | 89.43 [88.90, 89.80] | - | - |
| w9 | hover_land_indi_pct | - | 100.00 [100.00, 100.00] | - | - |

## Moment-pulse response (deg, deg·s, s, 0-1; window = where the pulse was fired)

| case | window | axis | metric | PID | INDI | Δ | clear |
|---|---|---|---|---|---|---|---|---|
| w6 | cruise | pitch | peak_dev_deg | 12.28 [11.88, 13.06] | 18.42 [18.06, 18.60] | +6.14 | yes |
| w6 | cruise | pitch | iae_deg_s | 14.05 [11.96, 16.80] | 46.75 [45.74, 47.39] | +32.71 | yes |
| w6 | cruise | pitch | settle_s | 1.27 [1.16, 1.33] | 5.00 [5.00, 5.00] | +3.73 | yes |
| w6 | cruise | pitch | motor_peak | 0.55 [0.54, 0.57] | 0.00 [0.00, 0.00] | -0.55 | yes |
| w6 | cruise | pitch | surface_peak | 0.63 [0.60, 0.65] | 0.80 [0.73, 0.86] | +0.16 | yes |
| w6 | cruise | pitch | moment_est | - | 0.94 [0.90, 1.01] | - | - |
| w6 | cruise | roll | peak_dev_deg | 27.55 [26.96, 28.63] | 35.84 [35.29, 36.61] | +8.29 | yes |
| w6 | cruise | roll | iae_deg_s | 47.83 [46.96, 48.60] | 64.69 [63.05, 66.54] | +16.86 | yes |
| w6 | cruise | roll | settle_s | 5.00 [5.00, 5.00] | 5.00 [5.00, 5.00] | +0.00 | no |
| w6 | cruise | roll | motor_peak | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | +0.00 | no |
| w6 | cruise | roll | surface_peak | 0.42 [0.41, 0.43] | 0.43 [0.38, 0.47] | +0.01 | no |
| w6 | cruise | roll | moment_est | - | 0.87 [0.85, 0.90] | - | - |
| w6 | hover_land | pitch | peak_dev_deg | 2.96 [2.87, 3.04] | 0.78 [0.77, 0.79] | -2.18 | yes |
| w6 | hover_land | pitch | iae_deg_s | 5.39 [5.26, 5.55] | 0.77 [0.76, 0.77] | -4.63 | yes |
| w6 | hover_land | pitch | settle_s | 2.56 [2.53, 2.62] | 0.00 [0.00, 0.00] | -2.56 | yes |
| w6 | hover_land | pitch | motor_peak | 0.59 [0.59, 0.60] | 0.60 [0.59, 0.61] | +0.00 | no |
| w6 | hover_land | pitch | surface_peak | 0.44 [0.44, 0.45] | 0.34 [0.33, 0.35] | -0.11 | yes |
| w6 | hover_land | pitch | moment_est | - | 0.71 [0.70, 0.73] | - | - |
| w6 | hover_land | roll | peak_dev_deg | 1.75 [1.75, 1.75] | 1.33 [1.29, 1.35] | -0.42 | yes |
| w6 | hover_land | roll | iae_deg_s | 2.89 [2.77, 3.09] | 0.87 [0.84, 0.89] | -2.02 | yes |
| w6 | hover_land | roll | settle_s | 1.76 [1.70, 1.82] | 1.21 [1.20, 1.22] | -0.55 | yes |
| w6 | hover_land | roll | motor_peak | 0.75 [0.74, 0.76] | 0.73 [0.73, 0.73] | -0.02 | yes |
| w6 | hover_land | roll | surface_peak | 0.06 [0.05, 0.06] | 0.06 [0.06, 0.07] | +0.00 | no |
| w6 | hover_land | roll | moment_est | - | 0.83 [0.83, 0.84] | - | - |
| w6 | hover_takeoff | pitch | peak_dev_deg | 4.36 [4.32, 4.41] | 0.86 [0.81, 0.93] | -3.50 | yes |
| w6 | hover_takeoff | pitch | iae_deg_s | 6.29 [6.18, 6.35] | 0.95 [0.82, 1.09] | -5.34 | yes |
| w6 | hover_takeoff | pitch | settle_s | 2.33 [2.31, 2.36] | 0.00 [0.00, 0.00] | -2.33 | yes |
| w6 | hover_takeoff | pitch | motor_peak | 0.95 [0.95, 0.95] | 0.94 [0.92, 0.95] | -0.01 | no |
| w6 | hover_takeoff | pitch | surface_peak | 0.22 [0.21, 0.23] | 0.27 [0.26, 0.28] | +0.04 | yes |
| w6 | hover_takeoff | pitch | moment_est | - | 0.89 [0.84, 0.94] | - | - |
| w6 | hover_takeoff | roll | peak_dev_deg | 2.10 [2.10, 2.10] | 1.45 [1.44, 1.46] | -0.65 | yes |
| w6 | hover_takeoff | roll | iae_deg_s | 2.14 [2.14, 2.14] | 1.66 [1.30, 2.01] | -0.48 | no |
| w6 | hover_takeoff | roll | settle_s | 0.52 [0.52, 0.52] | 0.96 [0.85, 1.07] | +0.44 | yes |
| w6 | hover_takeoff | roll | motor_peak | 0.95 [0.95, 0.95] | 0.95 [0.95, 0.95] | +0.00 | no |
| w6 | hover_takeoff | roll | surface_peak | 0.04 [0.04, 0.04] | 0.07 [0.07, 0.08] | +0.03 | yes |
| w6 | hover_takeoff | roll | moment_est | - | 0.59 [0.35, 0.83] | - | - |
| w6 | transition | pitch | peak_dev_deg | 4.58 [4.43, 4.76] | 0.96 [0.91, 1.01] | -3.61 | yes |
| w6 | transition | pitch | iae_deg_s | 6.75 [6.50, 6.87] | 1.58 [1.41, 1.71] | -5.16 | yes |
| w6 | transition | pitch | settle_s | 2.42 [2.36, 2.46] | 0.08 [0.00, 0.25] | -2.33 | yes |
| w6 | transition | pitch | motor_peak | 0.68 [0.68, 0.69] | 0.69 [0.67, 0.70] | +0.01 | no |
| w6 | transition | pitch | surface_peak | 0.25 [0.25, 0.26] | 0.28 [0.28, 0.29] | +0.03 | yes |
| w6 | transition | pitch | moment_est | - | 0.85 [0.80, 0.89] | - | - |
| w6 | transition | roll | peak_dev_deg | 5.08 [5.05, 5.12] | 5.63 [5.09, 6.43] | +0.55 | no |
| w6 | transition | roll | iae_deg_s | 15.50 [15.41, 15.61] | 14.78 [13.93, 15.95] | -0.73 | no |
| w6 | transition | roll | settle_s | 5.00 [5.00, 5.00] | 5.00 [5.00, 5.00] | +0.00 | no |
| w6 | transition | roll | motor_peak | 0.82 [0.81, 0.84] | 0.79 [0.76, 0.82] | -0.03 | no |
| w6 | transition | roll | surface_peak | 0.06 [0.05, 0.06] | 0.09 [0.08, 0.09] | +0.03 | yes |
| w6 | transition | roll | moment_est | - | 0.83 [0.79, 0.88] | - | - |
| w9 | cruise | pitch | peak_dev_deg | 37.13 [34.90, 41.23] | 28.53 [26.13, 30.89] | -8.60 | yes |
| w9 | cruise | pitch | iae_deg_s | 36.60 [34.78, 37.79] | 42.12 [40.16, 43.11] | +5.51 | yes |
| w9 | cruise | pitch | settle_s | 5.00 [5.00, 5.00] | 5.00 [5.00, 5.00] | -0.00 | no |
| w9 | cruise | pitch | motor_peak | 0.56 [0.56, 0.57] | 0.55 [0.55, 0.55] | -0.01 | no |
| w9 | cruise | pitch | surface_peak | 1.00 [1.00, 1.00] | 1.00 [1.00, 1.00] | +0.00 | no |
| w9 | cruise | pitch | moment_est | - | 0.52 [0.50, 0.54] | - | - |
| w9 | cruise | roll | peak_dev_deg | 100.67 [95.18, 105.21] | 35.03 [34.78, 35.23] | -65.64 | yes |
| w9 | cruise | roll | iae_deg_s | 122.51 [117.05, 128.18] | 66.66 [66.53, 66.87] | -55.86 | yes |
| w9 | cruise | roll | settle_s | 5.00 [5.00, 5.00] | 5.00 [5.00, 5.00] | -0.00 | no |
| w9 | cruise | roll | motor_peak | 0.95 [0.95, 0.95] | 0.00 [0.00, 0.00] | -0.95 | yes |
| w9 | cruise | roll | surface_peak | 0.97 [0.91, 1.00] | 1.00 [1.00, 1.00] | +0.03 | no |
| w9 | cruise | roll | moment_est | - | 0.82 [0.82, 0.83] | - | - |
| w9 | hover_land | pitch | peak_dev_deg | 12.72 [8.52, 14.91] | 10.24 [8.75, 11.65] | -2.48 | no |
| w9 | hover_land | pitch | iae_deg_s | 17.71 [15.83, 20.99] | 6.57 [5.57, 7.46] | -11.14 | yes |
| w9 | hover_land | pitch | settle_s | 4.83 [4.49, 5.00] | 1.46 [1.25, 1.87] | -3.37 | yes |
| w9 | hover_land | pitch | motor_peak | 0.66 [0.59, 0.74] | 0.55 [0.54, 0.56] | -0.12 | no |
| w9 | hover_land | pitch | surface_peak | 0.80 [0.68, 1.00] | 0.37 [0.31, 0.46] | -0.43 | yes |
| w9 | hover_land | pitch | moment_est | - | 0.28 [0.23, 0.33] | - | - |
| w9 | hover_land | roll | peak_dev_deg | 6.06 [3.88, 7.31] | 8.47 [7.16, 9.90] | +2.41 | no |
| w9 | hover_land | roll | iae_deg_s | 7.81 [5.58, 8.94] | 7.26 [6.15, 8.56] | -0.55 | no |
| w9 | hover_land | roll | settle_s | 2.47 [2.30, 2.61] | 1.15 [1.09, 1.22] | -1.32 | yes |
| w9 | hover_land | roll | motor_peak | 0.83 [0.79, 0.86] | 0.79 [0.79, 0.81] | -0.04 | no |
| w9 | hover_land | roll | surface_peak | 0.17 [0.12, 0.20] | 0.22 [0.19, 0.25] | +0.05 | no |
| w9 | hover_land | roll | moment_est | - | 0.86 [0.86, 0.87] | - | - |
| w9 | hover_takeoff | pitch | peak_dev_deg | 7.16 [7.04, 7.26] | 1.78 [1.77, 1.79] | -5.38 | yes |
| w9 | hover_takeoff | pitch | iae_deg_s | 11.77 [11.64, 11.92] | 1.38 [1.31, 1.47] | -10.39 | yes |
| w9 | hover_takeoff | pitch | settle_s | 3.39 [2.26, 4.14] | 1.35 [1.33, 1.36] | -2.04 | yes |
| w9 | hover_takeoff | pitch | motor_peak | 0.95 [0.95, 0.95] | 0.94 [0.93, 0.95] | -0.01 | no |
| w9 | hover_takeoff | pitch | surface_peak | 0.72 [0.72, 0.73] | 0.33 [0.32, 0.34] | -0.39 | yes |
| w9 | hover_takeoff | pitch | moment_est | - | 0.87 [0.85, 0.88] | - | - |
| w9 | hover_takeoff | roll | peak_dev_deg | 1.90 [0.50, 3.48] | 1.67 [0.44, 2.89] | -0.23 | no |
| w9 | hover_takeoff | roll | iae_deg_s | 1.76 [1.27, 2.49] | 1.16 [0.46, 1.86] | -0.60 | no |
| w9 | hover_takeoff | roll | settle_s | 0.26 [0.00, 0.47] | 0.40 [0.00, 0.80] | +0.14 | no |
| w9 | hover_takeoff | roll | motor_peak | 0.95 [0.95, 0.95] | 0.95 [0.95, 0.95] | -0.00 | no |
| w9 | hover_takeoff | roll | surface_peak | 0.08 [0.05, 0.10] | 0.10 [0.02, 0.18] | +0.02 | no |
| w9 | hover_takeoff | roll | moment_est | - | 0.05 [0.00, 0.09] | - | - |
| w9 | transition | pitch | peak_dev_deg | 17.94 [17.84, 18.13] | 11.55 [10.46, 12.14] | -6.39 | yes |
| w9 | transition | pitch | iae_deg_s | 21.43 [21.08, 21.89] | 13.97 [12.63, 14.79] | -7.46 | yes |
| w9 | transition | pitch | settle_s | 3.46 [3.46, 3.47] | 2.67 [2.59, 2.71] | -0.79 | yes |
| w9 | transition | pitch | motor_peak | 0.77 [0.76, 0.78] | 0.79 [0.78, 0.80] | +0.02 | no |
| w9 | transition | pitch | surface_peak | 0.69 [0.68, 0.70] | 0.52 [0.46, 0.55] | -0.18 | yes |
| w9 | transition | pitch | moment_est | - | 0.51 [0.48, 0.55] | - | - |
| w9 | transition | roll | peak_dev_deg | 8.45 [8.32, 8.54] | 4.82 [4.41, 5.14] | -3.63 | yes |
| w9 | transition | roll | iae_deg_s | 15.80 [15.73, 15.84] | 8.22 [7.76, 8.74] | -7.58 | yes |
| w9 | transition | roll | settle_s | 5.00 [5.00, 5.00] | 5.00 [5.00, 5.00] | +0.00 | no |
| w9 | transition | roll | motor_peak | 0.92 [0.90, 0.94] | 0.81 [0.80, 0.81] | -0.11 | yes |
| w9 | transition | roll | surface_peak | 0.14 [0.14, 0.15] | 0.17 [0.16, 0.17] | +0.03 | yes |
| w9 | transition | roll | moment_est | - | 0.90 [0.90, 0.90] | - | - |
