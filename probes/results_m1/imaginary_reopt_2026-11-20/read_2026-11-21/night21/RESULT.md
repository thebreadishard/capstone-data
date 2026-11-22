# Imaginary-label re-optimisation: the acceptance read (TASKS 215)

14 molecules read, 10 accepted, 4 stay out (2 refused, 1 failed, 1 unfinished); 2 flagged for a heavy-atom distance above 0.5 bohr.

| id | lowest before (b3lyp / wb97x, cm⁻¹) | lowest after | rms all / heavy (bohr) | verdict |
|---|---|---|---|---|
| B_1e0fa2d7f0 | -11.95 / 48.62 | -10.55 / 49.82 | 0.021 / 0.009 | stays out: still imaginary: lowest mode b3lyp -10.55 cm-1 |
| B_0e50d7b85c | -20.72 / 29.49 | -20.57 / 33.49 | 0.018 / 0.010 | stays out: still imaginary: lowest mode b3lyp -20.57 cm-1 |
| B_84485091e3 | -3.53 / 49.66 | 13.41 / 54.07 | 0.022 / 0.011 | accepted |
| A2_20747fd501 | -110.04 / -113.09 | 60.49 / 72.75 | 0.433 / 0.190 | accepted |
| B_0617e12945 | -76.21 / -13.98 | 77.10 / 100.50 | 0.846 / 0.009 | accepted |
| B_0040149ee1 | -136.81 / -113.43 | 115.79 / 135.85 | 0.753 / 0.016 | accepted |
| B_32a4ec61cd | -41.36 / 28.57 | 53.21 / 73.98 | 0.948 / 0.685 CONFORMER | accepted |
| P3_2aa4adcc95 | -27.63 / 15.86 | 31.42 / — | 0.489 / 0.370 | stays out: unfinished: started and cut off in the labels; on disk: no label file for wb97x |
| B_0ec10fe103 | -225.69 / -181.85 | 163.09 / 193.28 | 0.406 / 0.066 | accepted |
| A_78896cfe24 | -50.79 / -48.61 | — / — | — | stays out: failed in the optimisation: RuntimeError: /root/night_215/in/molecules/A_78896cfe24: geomeTRIC did not converge to (dmax 0.0002, drms 0.0001, energy 1e-07, gmax 2e-05, grms 1e-05) within 100 steps (101 gradient calls); no geomet; on disk: no geometry.json |
| B_663eaca2f1 | -64.16 / 76.05 | 62.12 / 77.91 | 0.359 / 0.445 | accepted |
| B_1274d1530a | -41.07 / 48.13 | 44.54 / 89.11 | 0.818 / 0.009 | accepted |
| A2_3802542cb6 | -81.21 / -79.16 | 72.76 / 92.76 | 0.423 / 0.194 | accepted |
| A2_2a0b78bd2b | -35.37 / 44.13 | 28.28 / 62.77 | 0.550 / 0.649 CONFORMER | accepted |
