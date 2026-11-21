# The two steps of the low-mode repair: noise or step bias? (TASKS 218)

Small step: `probes/results_m1/low_mode_threshold_2026-11-20/patch_below60`; large step: `probes/results_m1/low_mode_threshold_2026-11-20/patch_step02_below60`. 16 points (re-measured label mode × functional) on 7 molecules; 1 flagged for a coverage or overlap below 0.9 at one of the steps, listed and left out of the summary. 'Noise' is the frequency noise the small step makes of 1e-07 hartree/bohr of gradient noise (`low_mode_threshold_read.noise_sensitivity_cm`); the two steps' difference carries 1.118 times that, and the last two columns set the difference against it at the registration's two values of σ.

## The points

| point | label (cm⁻¹) | small step | large step | large − small | as curvature (cm⁻²) | noise per 1e-07 | diff / noise at σ = 1e-08 | diff / noise at σ = 2e-08 | flag |
|---|---|---|---|---|---|---|---|---|---|
| B_3dcbd985e3 b3lyp mode 0 | 23.71 | 23.788 | 24.224 | +0.436 | +20.92 | 0.24 | 16.0 | 8.0 |  |
| B_0c6c144a7f b3lyp mode 0 | 23.73 | 23.538 | 24.111 | +0.573 | +27.29 | 1.09 | 4.7 | 2.4 |  |
| B_55cca3aaf2 b3lyp mode 0 | 23.83 | 22.266 | 22.756 | +0.489 | +22.04 | 1.04 | 4.2 | 2.1 |  |
| B_3dcbd985e3 b3lyp mode 1 | 30.28 | 29.928 | 30.195 | +0.266 | +16.01 | 0.71 | 3.3 | 1.7 |  |
| B_4ff67f9ea2 b3lyp mode 0 | 32.99 | 32.559 | 32.858 | +0.299 | +19.53 | 0.73 | 3.7 | 1.8 |  |
| B_1726105aae b3lyp mode 0 | 34.30 | 34.703 | 35.120 | +0.417 | +29.11 | 0.14 | 27.2 | 13.6 |  |
| B_0af11315e3 b3lyp mode 0 | 45.74 | 44.366 | 44.592 | +0.226 | +20.14 | 0.11 | 17.9 | 8.9 |  |
| B_1428bc8164 b3lyp mode 0 | 50.50 | 50.654 | 50.948 | +0.294 | +29.84 | 0.07 | 37.6 | 18.8 |  |
| B_55cca3aaf2 wb97x mode 0 | 54.42 | 56.337 | 56.590 | +0.253 | +28.55 | 0.50 | 4.5 | 2.2 |  |
| B_4ff67f9ea2 wb97x mode 0 | 57.64 | 58.507 | 58.743 | +0.236 | +27.72 | 0.49 | 4.3 | 2.1 |  |
| B_3dcbd985e3 wb97x mode 0 | 63.39 | 62.960 | 63.102 | +0.143 | +18.00 | 0.40 | 3.2 | 1.6 |  |
| B_0c6c144a7f wb97x mode 0 | 67.12 | 60.175 | 60.434 | +0.259 | +31.24 | 0.43 | 5.3 | 2.7 |  |
| B_3dcbd985e3 wb97x mode 1 | 77.84 | 77.144 | 77.265 | +0.120 | +18.60 | 0.07 | 14.6 | 7.3 |  |
| B_0af11315e3 wb97x mode 0 | 84.64 | 83.269 | 83.391 | +0.122 | +20.28 | 0.06 | 17.5 | 8.8 |  |
| B_1726105aae wb97x mode 0 | 111.71 | 111.368 | 111.501 | +0.134 | +29.77 | 0.04 | 28.1 | 14.0 |  |
| B_1428bc8164 wb97x mode 2 | 119.99 | 119.986 | 120.095 | +0.109 | +26.23 | 0.04 | 24.8 | 12.4 | overlap |

## The measured curvature along each direction, uᵀC (cm⁻²)

| molecule | functional | direction | small step | large step | large − small | noise of the difference per 1e-07 |
|---|---|---|---|---|---|---|
| B_0af11315e3 | b3lyp | 0 | 1968.59 | 1988.73 | +20.15 | 11.6 |
| B_0af11315e3 | wb97x | 0 | 7005.66 | 7026.56 | +20.90 | 11.6 |
| B_0c6c144a7f | b3lyp | 0 | 554.26 | 581.71 | +27.45 | 57.7 |
| B_0c6c144a7f | wb97x | 0 | 3966.87 | 3993.26 | +26.39 | 57.7 |
| B_1428bc8164 | b3lyp | 0 | 2566.49 | 2596.35 | +29.87 | 7.9 |
| B_1428bc8164 | wb97x | 0 | 12988.58 | 13019.39 | +30.81 | 7.9 |
| B_1726105aae | b3lyp | 0 | 1204.34 | 1233.46 | +29.12 | 10.5 |
| B_1726105aae | wb97x | 0 | 12470.12 | 12500.14 | +30.02 | 10.5 |
| B_3dcbd985e3 | b3lyp | 0 | 566.33 | 911.69 | the steps used other directions | 12.9 |
| B_3dcbd985e3 | b3lyp | 1 | 895.67 | 587.27 | the steps used other directions | 48.2 |
| B_3dcbd985e3 | wb97x | 0 | 5878.50 | 4375.24 | the steps used other directions | 12.9 |
| B_3dcbd985e3 | wb97x | 1 | 4358.75 | 5900.09 | the steps used other directions | 48.2 |
| B_4ff67f9ea2 | b3lyp | 0 | 1191.49 | 1214.52 | +23.03 | 58.6 |
| B_4ff67f9ea2 | wb97x | 0 | 3492.01 | 3518.21 | +26.20 | 58.6 |
| B_55cca3aaf2 | b3lyp | 0 | 568.71 | 592.77 | +24.06 | 58.3 |
| B_55cca3aaf2 | wb97x | 0 | 3254.39 | 3279.60 | +25.21 | 58.3 |

## What the numbers say

Of 15 unflagged points, 15 have the large step above the small one and 0 below; noise without a preferred sign gives one sign on all of them with probability 6.1e-05. The differences run from +0.120 to +0.573 cm⁻¹; as curvatures from +16.0 to +31.2 cm⁻² (mean +23.9, standard deviation 5.2). Against the noise the difference would carry, a point's difference is 1.6 to 18.8 standard deviations at σ = 2e-08 hartree/bohr (median 2.7; 8 point(s) below 3) and 3.2 to 37.6 at σ = 1e-08 (median 5.3; 0 below 3). Along the 6 direction(s) measured along the same vector at both steps, the two functionals' curvature differences stand 0.8 to 3.2 cm⁻² apart, where the differences themselves are +20.1 to +30.8 cm⁻²: two separate SCFs give the same step difference. Two steps cannot show that the error grows as the square of the step; that is the central difference's own error law, and a third step would test it.
