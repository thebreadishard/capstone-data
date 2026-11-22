# Imaginary-label re-optimisation: the acceptance read (TASKS 215)

12 molecules read, 10 accepted, 2 stay out (1 refused, 1 failed); 4 flagged for a heavy-atom distance above 0.5 bohr.

| id | lowest before (b3lyp / wb97x, cm⁻¹) | lowest after | rms all / heavy (bohr) | verdict |
|---|---|---|---|---|
| B_0cb4d08a36 | -53.97 / 60.71 | — / — | — | stays out: failed in the optimisation: RuntimeError: /root/night_215/in/molecules/B_0cb4d08a36: geomeTRIC did not converge to (dmax 0.0002, drms 0.0001, energy 1e-07, gmax 2e-05, grms 1e-05) within 100 steps (101 gradient calls); no geomet; on disk: no geometry.json |
| A_b90527ca2d | -37.73 / 37.31 | 45.32 / 71.63 | 0.470 / 0.313 | accepted |
| A2_2c22216564 | -35.63 / 92.23 | 32.28 / 91.17 | 0.443 / 0.542 CONFORMER | accepted |
| B_08267d7c1c | -73.88 / -34.04 | 72.93 / 109.98 | 0.770 / 0.008 | accepted |
| A_014f8519af | -22.20 / 54.48 | 22.73 / 66.31 | 2.062 / 1.324 CONFORMER | accepted |
| A2_197913eb9c | -86.65 / -81.97 | 64.36 / 86.51 | 0.399 / 0.178 | accepted |
| B_04f049ae58 | -7.17 / 73.11 | 6.55 / 74.86 | 0.019 / 0.001 | accepted |
| B_1e9434eced | -36.15 / 29.69 | 48.59 / 69.08 | 0.950 / 0.634 CONFORMER | accepted |
| A2_0420908ebe | -33.57 / 40.95 | 41.07 / 64.24 | 0.482 / 0.394 | accepted |
| B_130c5d839d | -363.68 / -303.10 | 49.43 / 73.26 | 0.909 / 0.153 | accepted |
| B_5bf791b132 | -66.33 / 36.42 | 71.34 / 103.78 | 0.491 / 0.533 CONFORMER | accepted |
| A2_187a20beab | -8.11 / 55.70 | -4.74 / 56.01 | 0.022 / 0.025 | stays out: still imaginary: lowest mode b3lyp -4.74 cm-1 |
