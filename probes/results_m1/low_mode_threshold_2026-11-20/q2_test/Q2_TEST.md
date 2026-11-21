# Does the step error of the low-mode repair grow as q²? (TASKS 218; amendment 3, point 7)

Steps: `probes/results_m1/low_mode_threshold_2026-11-20/patch_below60`, `probes/results_m1/low_mode_threshold_2026-11-20/patch_step02_below60` and `probes/results_m1/low_mode_threshold_2026-11-20/patch_step04_q2test`, each twice the one before, along the same directions. For an error a·q² the ratio R = [c(4q) − c(q)] / [c(2q) − c(q)] of a direction's measured curvatures c = uᵀC is 5; an error linear in q gives 3, one that grows as q⁴ gives 17. The law is taken to hold when every R lies in 4–6. 'Noise of R' is one standard deviation at σ = 2e-08 hartree/bohr.

**The law holds.**

| molecule | functional | direction | c(q) (cm⁻²) | c(2q) | c(4q) | R | noise of R | inside | zero step, two points | zero step, three points | difference |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B_1428bc8164 | b3lyp | 0 | 2566.49 | 2596.35 | 2715.60 | 4.993 | 0.223 | yes | 2556.53 | 2556.53 | -0.00 |
| B_1428bc8164 | wb97x | 0 | 12988.58 | 13019.39 | 13142.61 | 5.000 | 0.216 | yes | 12978.31 | 12978.31 | -0.00 |
| B_1726105aae | b3lyp | 0 | 1204.34 | 1233.46 | 1349.67 | 4.991 | 0.304 | yes | 1194.63 | 1194.63 | -0.01 |
| B_1726105aae | wb97x | 0 | 12470.12 | 12500.14 | 12620.11 | 4.996 | 0.295 | yes | 12460.12 | 12460.12 | -0.00 |

The last three columns are a description and carry no rule: the three-point value fits c₀ + a·q² + b·q⁴ through the three steps exactly, so it has no degree of freedom left and more noise than the two-point one.
