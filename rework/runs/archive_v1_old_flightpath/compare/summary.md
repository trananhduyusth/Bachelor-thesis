# PID vs INDI - campaign summary

Runs: 18 (indi_calm_s1, indi_calm_s2, indi_calm_s3, indi_w6_s1, indi_w6_s2, indi_w6_s3, indi_w9_s1, indi_w9_s2, indi_w9_s3, pid_calm_s1, pid_calm_s2, pid_calm_s3, pid_w6_s1, pid_w6_s2, pid_w6_s3, pid_w9_s1, pid_w9_s2, pid_w9_s3). Mean over seeds, [min, max] in brackets. Δ = INDI - PID; "clear" = |Δ| larger than the seed spread of both controllers.

## Missions completed

| ctrl | case | completed / runs |
|---|---|---|
| indi | calm | 3 / 3 |
| indi | w6 | 3 / 3 |
| indi | w9 | 3 / 3 |
| pid | calm | 3 / 3 |
| pid | w6 | 3 / 3 |
| pid | w9 | 3 / 3 |

## Per-phase metrics (deg, m, %)

| case | metric | PID | INDI | Δ | clear |
|---|---|---|---|---|---|---|
| calm | hover_takeoff_roll_rms | 0.01 [0.01, 0.02] | 0.02 [0.01, 0.02] | +0.00 | no |
| calm | hover_takeoff_pitch_rms | 0.53 [0.53, 0.54] | 0.06 [0.06, 0.06] | -0.48 | yes |
| calm | hover_land_roll_rms | 0.04 [0.03, 0.05] | 0.03 [0.03, 0.03] | -0.01 | no |
| calm | hover_land_pitch_rms | 0.48 [0.47, 0.48] | 0.26 [0.26, 0.26] | -0.21 | yes |
| calm | transition_roll_rms | 4.13 [4.08, 4.16] | 4.24 [4.23, 4.26] | +0.11 | yes |
| calm | transition_pitch_rms | 1.53 [1.52, 1.55] | 1.22 [1.11, 1.36] | -0.30 | yes |
| calm | fixed_wing_roll_rms | 12.03 [11.82, 12.29] | 12.10 [11.85, 12.26] | +0.06 | no |
| calm | fixed_wing_pitch_rms | 3.80 [3.74, 3.91] | 4.09 [3.96, 4.18] | +0.29 | yes |
| calm | hover_takeoff_alt_rms | 0.18 [0.18, 0.18] | 0.18 [0.18, 0.18] | +0.00 | yes |
| calm | hover_land_alt_rms | 0.54 [0.54, 0.54] | 0.53 [0.52, 0.54] | -0.01 | no |
| calm | hover_land_motor_max_pct | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | +0.00 | no |
| calm | fw_tecs_alt_rms | 6.85 [6.79, 6.89] | 7.43 [7.35, 7.52] | +0.58 | yes |
| calm | fw_crosstrack_rms | 28.28 [28.07, 28.51] | 29.32 [28.91, 29.54] | +1.05 | yes |
| calm | fw_assist_pct | 0.00 [0.00, 0.00] | 0.07 [0.00, 0.20] | +0.07 | no |
| calm | fw_airspeed_mean | 20.28 [20.26, 20.30] | 20.29 [20.28, 20.31] | +0.02 | no |
| calm | hover_takeoff_indi_pct | - | 87.70 [87.70, 87.70] | - | - |
| calm | transition_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| calm | fixed_wing_indf_pct | - | 100.00 [100.00, 100.00] | - | - |
| calm | hover_land_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w6 | hover_takeoff_roll_rms | 0.57 [0.53, 0.59] | 0.37 [0.37, 0.37] | -0.20 | yes |
| w6 | hover_takeoff_pitch_rms | 1.24 [1.21, 1.28] | 0.34 [0.34, 0.34] | -0.89 | yes |
| w6 | hover_land_roll_rms | 0.32 [0.31, 0.33] | 0.12 [0.09, 0.14] | -0.20 | yes |
| w6 | hover_land_pitch_rms | 1.08 [1.07, 1.12] | 0.31 [0.26, 0.34] | -0.77 | yes |
| w6 | transition_roll_rms | 6.50 [6.43, 6.54] | 6.82 [6.78, 6.86] | +0.32 | yes |
| w6 | transition_pitch_rms | 3.12 [3.05, 3.17] | 3.40 [3.37, 3.44] | +0.29 | yes |
| w6 | fixed_wing_roll_rms | 9.58 [9.38, 9.77] | 9.21 [5.84, 11.04] | -0.37 | no |
| w6 | fixed_wing_pitch_rms | 5.52 [5.41, 5.59] | 3.98 [2.80, 4.57] | -1.54 | no |
| w6 | hover_takeoff_alt_rms | 0.08 [0.08, 0.08] | 0.08 [0.08, 0.08] | +0.00 | no |
| w6 | hover_land_alt_rms | 0.70 [0.65, 0.77] | 0.68 [0.52, 0.77] | -0.01 | no |
| w6 | hover_land_motor_max_pct | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | +0.00 | no |
| w6 | fw_tecs_alt_rms | 9.01 [8.84, 9.20] | 6.39 [2.51, 8.36] | -2.62 | no |
| w6 | fw_crosstrack_rms | 23.54 [23.33, 23.66] | 21.57 [16.23, 24.61] | -1.97 | no |
| w6 | fw_assist_pct | 0.07 [0.00, 0.20] | 7.53 [0.00, 22.40] | +7.47 | no |
| w6 | fw_airspeed_mean | 19.76 [19.66, 19.82] | 19.12 [17.95, 19.71] | -0.65 | no |
| w6 | hover_takeoff_indi_pct | - | 88.70 [88.60, 88.80] | - | - |
| w6 | transition_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w6 | fixed_wing_indf_pct | - | 92.53 [77.60, 100.00] | - | - |
| w6 | hover_land_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w9 | hover_takeoff_roll_rms | 1.05 [1.05, 1.05] | 0.48 [0.48, 0.48] | -0.58 | yes |
| w9 | hover_takeoff_pitch_rms | 2.08 [2.07, 2.08] | 0.32 [0.32, 0.32] | -1.76 | yes |
| w9 | hover_land_roll_rms | 0.59 [0.56, 0.64] | 0.27 [0.25, 0.30] | -0.32 | yes |
| w9 | hover_land_pitch_rms | 1.69 [1.37, 1.92] | 1.12 [0.92, 1.23] | -0.57 | yes |
| w9 | transition_roll_rms | 4.37 [4.34, 4.41] | 4.45 [4.41, 4.50] | +0.08 | no |
| w9 | transition_pitch_rms | 4.04 [4.03, 4.06] | 4.01 [3.97, 4.06] | -0.03 | no |
| w9 | fixed_wing_roll_rms | 14.39 [14.08, 14.70] | 5.23 [5.21, 5.24] | -9.17 | yes |
| w9 | fixed_wing_pitch_rms | 7.03 [6.81, 7.38] | 4.30 [4.23, 4.43] | -2.73 | yes |
| w9 | hover_takeoff_alt_rms | 0.09 [0.09, 0.09] | 0.08 [0.08, 0.08] | -0.01 | yes |
| w9 | hover_land_alt_rms | 0.65 [0.63, 0.69] | 0.62 [0.59, 0.66] | -0.03 | no |
| w9 | hover_land_motor_max_pct | 0.00 [0.00, 0.00] | 0.00 [0.00, 0.00] | +0.00 | no |
| w9 | fw_tecs_alt_rms | 4.49 [4.26, 4.75] | 3.75 [3.71, 3.80] | -0.74 | yes |
| w9 | fw_crosstrack_rms | 19.71 [18.86, 20.79] | 17.99 [17.44, 18.96] | -1.72 | no |
| w9 | fw_assist_pct | 75.53 [62.00, 83.50] | 79.03 [75.80, 83.80] | +3.50 | no |
| w9 | fw_airspeed_mean | 15.92 [15.75, 16.23] | 16.20 [15.63, 16.59] | +0.27 | no |
| w9 | hover_takeoff_indi_pct | - | 88.60 [88.60, 88.60] | - | - |
| w9 | transition_indi_pct | - | 100.00 [100.00, 100.00] | - | - |
| w9 | fixed_wing_indf_pct | - | 21.00 [16.30, 24.20] | - | - |
| w9 | hover_land_indi_pct | - | 100.00 [100.00, 100.00] | - | - |

## Moment-pulse response (deg, deg·s, s, 0-1; window = where the pulse was fired)

| case | window | axis | metric | PID | INDI | Δ | clear |
|---|---|---|---|---|---|---|---|---|
| w6 | cruise | pitch | peak_dev_deg | 17.41 [15.82, 19.97] | 13.01 [9.22, 14.99] | -4.40 | no |
| w6 | cruise | pitch | iae_deg_s | 50.73 [47.67, 56.44] | 34.11 [22.87, 40.04] | -16.62 | no |
| w6 | cruise | pitch | settle_s | 4.97 [4.96, 5.00] | 4.96 [4.96, 4.96] | -0.01 | no |
| w6 | cruise | pitch | motor_peak | 0.00 [0.00, 0.00] | 0.29 [0.15, 0.58] | +0.29 | no |
| w6 | cruise | pitch | surface_peak | 0.80 [0.77, 0.82] | 0.87 [0.85, 0.89] | +0.07 | yes |
| w6 | cruise | pitch | moment_est | - | 1.16 [1.06, 1.27] | - | - |
| w6 | cruise | roll | peak_dev_deg | 9.31 [9.14, 9.41] | 11.01 [10.31, 11.48] | +1.70 | yes |
| w6 | cruise | roll | iae_deg_s | 29.44 [27.93, 30.45] | 30.49 [29.58, 31.64] | +1.05 | no |
| w6 | cruise | roll | settle_s | 4.97 [4.96, 5.00] | 4.96 [4.96, 4.96] | -0.01 | no |
| w6 | cruise | roll | motor_peak | 0.67 [0.63, 0.71] | 0.65 [0.64, 0.67] | -0.02 | no |
| w6 | cruise | roll | surface_peak | 0.11 [0.08, 0.12] | 0.14 [0.12, 0.15] | +0.04 | no |
| w6 | cruise | roll | moment_est | - | 0.70 [0.69, 0.71] | - | - |
| w6 | hover_land | pitch | peak_dev_deg | 4.55 [4.54, 4.56] | 0.81 [0.80, 0.82] | -3.74 | yes |
| w6 | hover_land | pitch | iae_deg_s | 6.68 [6.43, 6.81] | 0.64 [0.59, 0.68] | -6.05 | yes |
| w6 | hover_land | pitch | settle_s | 1.55 [1.20, 1.72] | 0.00 [0.00, 0.00] | -1.55 | yes |
| w6 | hover_land | pitch | motor_peak | 0.69 [0.68, 0.70] | 0.68 [0.68, 0.68] | -0.02 | no |
| w6 | hover_land | pitch | surface_peak | 0.22 [0.21, 0.22] | 0.22 [0.20, 0.25] | +0.00 | no |
| w6 | hover_land | pitch | moment_est | - | 0.89 [0.86, 0.91] | - | - |
| w6 | hover_land | roll | peak_dev_deg | 2.02 [1.99, 2.07] | 1.33 [1.29, 1.36] | -0.69 | yes |
| w6 | hover_land | roll | iae_deg_s | 3.69 [3.56, 3.86] | 0.91 [0.80, 0.97] | -2.78 | yes |
| w6 | hover_land | roll | settle_s | 1.93 [1.92, 1.96] | 1.21 [1.20, 1.24] | -0.72 | yes |
| w6 | hover_land | roll | motor_peak | 0.77 [0.76, 0.78] | 0.75 [0.73, 0.77] | -0.01 | no |
| w6 | hover_land | roll | surface_peak | 0.03 [0.03, 0.03] | 0.04 [0.03, 0.04] | +0.01 | no |
| w6 | hover_land | roll | moment_est | - | 0.88 [0.86, 0.89] | - | - |
| w6 | hover_takeoff | pitch | peak_dev_deg | 4.00 [3.59, 4.25] | 0.80 [0.80, 0.81] | -3.20 | yes |
| w6 | hover_takeoff | pitch | iae_deg_s | 6.39 [6.25, 6.49] | 0.76 [0.73, 0.78] | -5.63 | yes |
| w6 | hover_takeoff | pitch | settle_s | 2.31 [2.24, 2.36] | 0.00 [0.00, 0.00] | -2.31 | yes |
| w6 | hover_takeoff | pitch | motor_peak | 0.94 [0.94, 0.95] | 0.95 [0.95, 0.95] | +0.01 | no |
| w6 | hover_takeoff | pitch | surface_peak | 0.22 [0.21, 0.25] | 0.23 [0.22, 0.23] | +0.00 | no |
| w6 | hover_takeoff | pitch | moment_est | - | 0.81 [0.80, 0.82] | - | - |
| w6 | hover_takeoff | roll | peak_dev_deg | 2.07 [1.93, 2.16] | 1.56 [1.51, 1.59] | -0.52 | yes |
| w6 | hover_takeoff | roll | iae_deg_s | 4.30 [3.82, 4.57] | 1.34 [1.30, 1.38] | -2.96 | yes |
| w6 | hover_takeoff | roll | settle_s | 2.37 [2.12, 2.52] | 1.27 [1.24, 1.28] | -1.11 | yes |
| w6 | hover_takeoff | roll | motor_peak | 0.95 [0.95, 0.95] | 0.95 [0.95, 0.95] | +0.00 | no |
| w6 | hover_takeoff | roll | surface_peak | 0.04 [0.04, 0.04] | 0.03 [0.03, 0.03] | -0.01 | yes |
| w6 | hover_takeoff | roll | moment_est | - | 0.99 [0.98, 1.00] | - | - |
| w6 | transition | pitch | peak_dev_deg | 4.84 [4.58, 5.24] | 1.17 [1.02, 1.45] | -3.67 | yes |
| w6 | transition | pitch | iae_deg_s | 6.75 [6.57, 7.04] | 1.93 [1.86, 2.00] | -4.82 | yes |
| w6 | transition | pitch | settle_s | 2.47 [2.36, 2.52] | 1.80 [0.20, 4.96] | -0.67 | no |
| w6 | transition | pitch | motor_peak | 0.63 [0.61, 0.64] | 0.67 [0.66, 0.68] | +0.04 | yes |
| w6 | transition | pitch | surface_peak | 0.24 [0.23, 0.24] | 0.25 [0.25, 0.25] | +0.01 | no |
| w6 | transition | pitch | moment_est | - | 0.86 [0.85, 0.87] | - | - |
| w6 | transition | roll | peak_dev_deg | 5.24 [4.69, 6.25] | 5.85 [5.77, 5.92] | +0.62 | no |
| w6 | transition | roll | iae_deg_s | 14.56 [12.84, 17.43] | 14.28 [14.06, 14.50] | -0.28 | no |
| w6 | transition | roll | settle_s | 4.96 [4.96, 4.96] | 4.96 [4.96, 4.96] | -0.00 | no |
| w6 | transition | roll | motor_peak | 0.75 [0.73, 0.77] | 0.71 [0.71, 0.72] | -0.03 | no |
| w6 | transition | roll | surface_peak | 0.03 [0.03, 0.03] | 0.05 [0.05, 0.06] | +0.02 | yes |
| w6 | transition | roll | moment_est | - | 0.86 [0.85, 0.87] | - | - |
| w9 | cruise | pitch | peak_dev_deg | 15.57 [15.29, 15.75] | 16.69 [15.86, 17.47] | +1.12 | no |
| w9 | cruise | pitch | iae_deg_s | 53.92 [52.00, 54.95] | 39.43 [30.56, 45.03] | -14.49 | yes |
| w9 | cruise | pitch | settle_s | 4.96 [4.96, 4.96] | 4.97 [4.96, 5.00] | +0.01 | no |
| w9 | cruise | pitch | motor_peak | 0.56 [0.53, 0.58] | 0.52 [0.49, 0.55] | -0.04 | no |
| w9 | cruise | pitch | surface_peak | 0.96 [0.88, 1.00] | 0.92 [0.77, 1.00] | -0.04 | no |
| w9 | cruise | pitch | moment_est | - | 0.51 [0.28, 0.62] | - | - |
| w9 | cruise | roll | peak_dev_deg | 100.06 [93.98, 103.80] | 17.67 [15.23, 19.44] | -82.39 | yes |
| w9 | cruise | roll | iae_deg_s | 174.47 [169.14, 179.98] | 39.65 [37.03, 42.39] | -134.82 | yes |
| w9 | cruise | roll | settle_s | 4.96 [4.96, 4.96] | 1.16 [1.04, 1.28] | -3.80 | yes |
| w9 | cruise | roll | motor_peak | 0.78 [0.62, 0.95] | 0.00 [0.00, 0.00] | -0.78 | yes |
| w9 | cruise | roll | surface_peak | 0.74 [0.66, 0.81] | 0.70 [0.69, 0.71] | -0.04 | no |
| w9 | cruise | roll | moment_est | - | 0.94 [0.90, 0.98] | - | - |
| w9 | hover_land | pitch | peak_dev_deg | 15.10 [6.80, 19.82] | 7.55 [1.94, 10.53] | -7.55 | no |
| w9 | hover_land | pitch | iae_deg_s | 15.85 [12.96, 18.26] | 6.10 [1.64, 8.49] | -9.75 | yes |
| w9 | hover_land | pitch | settle_s | 3.09 [2.12, 4.96] | 1.19 [1.16, 1.20] | -1.91 | no |
| w9 | hover_land | pitch | motor_peak | 0.70 [0.65, 0.73] | 0.62 [0.60, 0.65] | -0.08 | no |
| w9 | hover_land | pitch | surface_peak | 0.68 [0.43, 0.80] | 0.42 [0.29, 0.49] | -0.26 | no |
| w9 | hover_land | pitch | moment_est | - | 0.68 [0.53, 0.96] | - | - |
| w9 | hover_land | roll | peak_dev_deg | 5.14 [4.96, 5.30] | 3.00 [2.95, 3.09] | -2.14 | yes |
| w9 | hover_land | roll | iae_deg_s | 8.68 [8.03, 9.46] | 2.49 [2.17, 3.10] | -6.19 | yes |
| w9 | hover_land | roll | settle_s | 2.68 [2.48, 2.96] | 1.24 [1.00, 1.36] | -1.44 | yes |
| w9 | hover_land | roll | motor_peak | 0.91 [0.89, 0.94] | 0.89 [0.86, 0.95] | -0.02 | no |
| w9 | hover_land | roll | surface_peak | 0.08 [0.07, 0.09] | 0.08 [0.07, 0.09] | +0.00 | no |
| w9 | hover_land | roll | moment_est | - | 0.91 [0.90, 0.92] | - | - |
| w9 | hover_takeoff | pitch | peak_dev_deg | 7.71 [7.68, 7.73] | 1.75 [1.75, 1.76] | -5.96 | yes |
| w9 | hover_takeoff | pitch | iae_deg_s | 12.09 [11.98, 12.20] | 1.25 [1.25, 1.25] | -10.84 | yes |
| w9 | hover_takeoff | pitch | settle_s | 2.29 [2.28, 2.32] | 1.32 [1.32, 1.32] | -0.97 | yes |
| w9 | hover_takeoff | pitch | motor_peak | 0.95 [0.95, 0.95] | 0.92 [0.91, 0.92] | -0.03 | yes |
| w9 | hover_takeoff | pitch | surface_peak | 0.44 [0.43, 0.44] | 0.27 [0.27, 0.27] | -0.17 | yes |
| w9 | hover_takeoff | pitch | moment_est | - | 0.87 [0.87, 0.87] | - | - |
| w9 | hover_takeoff | roll | peak_dev_deg | 4.73 [4.73, 4.73] | 2.95 [2.95, 2.95] | -1.78 | yes |
| w9 | hover_takeoff | roll | iae_deg_s | 6.72 [6.71, 6.73] | 2.01 [2.00, 2.02] | -4.72 | yes |
| w9 | hover_takeoff | roll | settle_s | 2.28 [2.28, 2.28] | 1.37 [1.36, 1.40] | -0.91 | yes |
| w9 | hover_takeoff | roll | motor_peak | 0.95 [0.95, 0.95] | 0.95 [0.95, 0.95] | +0.00 | no |
| w9 | hover_takeoff | roll | surface_peak | 0.09 [0.09, 0.09] | 0.09 [0.09, 0.09] | +0.01 | yes |
| w9 | hover_takeoff | roll | moment_est | - | 0.90 [0.90, 0.91] | - | - |
| w9 | transition | pitch | peak_dev_deg | 21.11 [20.90, 21.34] | 19.19 [19.08, 19.27] | -1.92 | yes |
| w9 | transition | pitch | iae_deg_s | 30.13 [30.08, 30.17] | 30.31 [29.50, 30.98] | +0.17 | no |
| w9 | transition | pitch | settle_s | 4.96 [4.96, 4.96] | 4.19 [3.28, 4.68] | -0.77 | no |
| w9 | transition | pitch | motor_peak | 0.68 [0.68, 0.68] | 0.70 [0.68, 0.72] | +0.02 | no |
| w9 | transition | pitch | surface_peak | 0.68 [0.67, 0.69] | 0.63 [0.61, 0.64] | -0.05 | yes |
| w9 | transition | pitch | moment_est | - | 0.18 [0.14, 0.19] | - | - |
| w9 | transition | roll | peak_dev_deg | 10.99 [10.88, 11.18] | 11.58 [10.94, 11.91] | +0.59 | no |
| w9 | transition | roll | iae_deg_s | 17.57 [17.39, 17.73] | 17.49 [16.67, 17.92] | -0.08 | no |
| w9 | transition | roll | settle_s | 4.96 [4.96, 4.96] | 4.96 [4.96, 4.96] | +0.00 | no |
| w9 | transition | roll | motor_peak | 0.89 [0.88, 0.90] | 0.80 [0.80, 0.81] | -0.08 | yes |
| w9 | transition | roll | surface_peak | 0.11 [0.11, 0.12] | 0.15 [0.14, 0.15] | +0.03 | yes |
| w9 | transition | roll | moment_est | - | 0.90 [0.89, 0.90] | - | - |
