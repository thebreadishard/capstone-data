# Quartic force field from 85 displaced Hessians — C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\s2_xtb_2026-10-18\xtb\B_410ac0fb2f\X\hess

Reference file `ref.json`; 42 vibrational modes; displacement 0.1 in reduced coordinates; assignment residual max 2.14e-14.
Harmonic ω (cm⁻¹): 93.7, 126.6, 227.4, 349.6, 358.4, 390.8, 399.5, 403.9, 455.3, 485.7, 528.8, 610.7, 625.1, 671.0, 681.2, 717.5, 804.6, 856.7, 869.6, 901.6, 915.1, 1014.2, 1025.1, 1138.5, 1188.0, 1228.5, 1274.1, 1321.8, 1333.3, 1423.0, 1484.8, 1518.6, 1562.3, 1612.2, 2256.3, 3065.6, 3068.0, 3084.6, 3086.7, 3395.1, 3462.0, 3516.3

## Noise diagnostics

Off-diagonal semi-diagonal quartic constants φ_iijj have two independent finite-difference routes (displace j and read H_ii; displace i and read H_jj). Their difference is a direct estimate of the numerical error of that constant. Exactly degenerate pairs (a, b) must give equal φ_aa,jj and φ_bb,jj for every totally symmetric j; their difference is a second estimate.

- route disagreement |φ_iijj(a) − φ_iijj(b)|: median 0.0, 90th percentile 0.0, max 1.9 cm⁻¹ (max |φ_iijj| 1195.9)
- cubic route spread (max − min of the three routes): median 0.00, max 4.4 cm⁻¹
- totally symmetric modes (|φ_iii| > 5 cm⁻¹, non-degenerate): [(6, 399.5), (7, 403.9), (9, 485.7), (10, 528.8), (15, 717.5), (18, 869.6), (21, 1014.2), (24, 1188.0), (25, 1228.5), (27, 1321.8), (30, 1484.8), (31, 1518.6), (33, 1612.2), (34, 2256.3), (36, 3068.0), (37, 3084.6), (38, 3086.7), (39, 3395.1), (40, 3462.0)]

| degenerate pair (ω) | j (ω) | φ_aa,jj | φ_bb,jj | difference | route disagreement a / b |
|---|---|---|---|---|---|

## VPT2 fundamentals (deperturbation window 200.0 cm⁻¹, min K 0.0; 2701 resonances deperturbed; polyad diagonalisation not applied)

| mode | ω | ν raw quartics | ν − ω | ν symmetry-averaged quartics | ν − ω | pyVPT2 ν | pair |
|---|---|---|---|---|---|---|---|
| 0 | 93.7 | 92.6 | -1.0 | 92.6 | -1.0 | — |  |
| 1 | 126.6 | 128.3 | +1.8 | 128.3 | +1.8 | — |  |
| 2 | 227.4 | 226.6 | -0.8 | 226.6 | -0.8 | — |  |
| 3 | 349.6 | 349.3 | -0.2 | 349.3 | -0.2 | — |  |
| 4 | 358.4 | 356.3 | -2.1 | 356.3 | -2.1 | — |  |
| 5 | 390.8 | 385.5 | -5.3 | 385.5 | -5.3 | — |  |
| 6 | 399.5 | 397.6 | -1.9 | 397.6 | -1.9 | — |  |
| 7 | 403.9 | 401.4 | -2.5 | 401.4 | -2.5 | — |  |
| 8 | 455.3 | 459.1 | +3.8 | 459.1 | +3.8 | — |  |
| 9 | 485.7 | 459.5 | -26.2 | 459.5 | -26.2 | — |  |
| 10 | 528.8 | 302.1 | -226.7 | 302.1 | -226.7 | — |  |
| 11 | 610.7 | 605.8 | -4.9 | 605.8 | -4.9 | — |  |
| 12 | 625.1 | 619.9 | -5.3 | 619.9 | -5.3 | — |  |
| 13 | 671.0 | 668.8 | -2.2 | 668.8 | -2.2 | — |  |
| 14 | 681.2 | 669.9 | -11.3 | 669.9 | -11.3 | — |  |
| 15 | 717.5 | 705.4 | -12.1 | 705.4 | -12.1 | — |  |
| 16 | 804.6 | 790.6 | -14.1 | 790.6 | -14.1 | — |  |
| 17 | 856.7 | 840.4 | -16.3 | 840.4 | -16.3 | — |  |
| 18 | 869.6 | 857.7 | -12.0 | 857.7 | -12.0 | — |  |
| 19 | 901.6 | 882.8 | -18.9 | 882.8 | -18.9 | — |  |
| 20 | 915.1 | 897.3 | -17.8 | 897.3 | -17.8 | — |  |
| 21 | 1014.2 | 999.1 | -15.1 | 999.1 | -15.1 | — |  |
| 22 | 1025.1 | 984.8 | -40.3 | 984.8 | -40.3 | — |  |
| 23 | 1138.5 | 1125.6 | -12.9 | 1125.6 | -12.9 | — |  |
| 24 | 1188.0 | 1174.1 | -14.0 | 1174.1 | -14.0 | — |  |
| 25 | 1228.5 | 1211.2 | -17.4 | 1211.2 | -17.4 | — |  |
| 26 | 1274.1 | 1252.5 | -21.6 | 1252.5 | -21.6 | — |  |
| 27 | 1321.8 | 1301.9 | -20.0 | 1301.9 | -20.0 | — |  |
| 28 | 1333.3 | 1305.5 | -27.8 | 1305.5 | -27.8 | — |  |
| 29 | 1423.0 | 1397.1 | -25.9 | 1397.1 | -25.9 | — |  |
| 30 | 1484.8 | 1450.8 | -34.0 | 1450.8 | -34.0 | — |  |
| 31 | 1518.6 | 1486.6 | -32.0 | 1486.6 | -32.0 | — |  |
| 32 | 1562.3 | 1525.5 | -36.7 | 1525.5 | -36.7 | — |  |
| 33 | 1612.2 | 1576.4 | -35.8 | 1576.4 | -35.8 | — |  |
| 34 | 2256.3 | 2215.1 | -41.2 | 2215.1 | -41.2 | — |  |
| 35 | 3065.6 | 2902.6 | -163.0 | 2902.6 | -163.0 | — |  |
| 36 | 3068.0 | 2908.8 | -159.1 | 2908.8 | -159.1 | — |  |
| 37 | 3084.6 | 2926.6 | -158.0 | 2926.6 | -158.0 | — |  |
| 38 | 3086.7 | 2929.9 | -156.8 | 2929.9 | -156.8 | — |  |
| 39 | 3395.1 | 3226.8 | -168.2 | 3226.8 | -168.2 | — |  |
| 40 | 3462.0 | 3263.5 | -198.5 | 3263.5 | -198.5 | — |  |
| 41 | 3516.3 | 3309.2 | -207.1 | 3309.2 | -207.1 | — |  |

## Provenance

- timestamp_utc: `2026-11-04 07:39:04`
- host: `Asus18`
- python: `3.14.6`
- numpy: `2.5.1`
- command: `qff.py C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\s2_xtb_2026-10-18\xtb\B_410ac0fb2f\X\hess --disp 0.10 --out C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\s2_xtb_2026-10-18\xtb\B_410ac0fb2f\X\qff_report.md`
- commit: `648a001eb6cfa32df774b73c6e2f0d91dadb87c4`
- dirty: `yes`
