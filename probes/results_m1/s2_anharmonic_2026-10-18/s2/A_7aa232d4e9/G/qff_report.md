# Quartic force field from 85 displaced Hessians — C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\s2_anharmonic_2026-10-18\s2\A_7aa232d4e9\G\hess

Reference file `ref.json`; 42 vibrational modes; displacement 0.1 in reduced coordinates; assignment residual max 2.74e-14.
Harmonic ω (cm⁻¹): 179.4, 186.7, 396.8, 417.2, 482.1, 504.6, 534.8, 544.2, 615.7, 654.6, 773.8, 779.6, 818.7, 849.8, 888.8, 900.5, 965.1, 977.6, 986.5, 1005.3, 1039.0, 1057.4, 1154.9, 1173.2, 1243.2, 1251.2, 1297.5, 1340.5, 1402.1, 1425.6, 1464.6, 1515.2, 1549.4, 1618.5, 1621.0, 1672.0, 3163.9, 3182.0, 3192.3, 3205.0, 3218.6, 3222.7

## Noise diagnostics

Off-diagonal semi-diagonal quartic constants φ_iijj have two independent finite-difference routes (displace j and read H_ii; displace i and read H_jj). Their difference is a direct estimate of the numerical error of that constant. Exactly degenerate pairs (a, b) must give equal φ_aa,jj and φ_bb,jj for every totally symmetric j; their difference is a second estimate.

- route disagreement |φ_iijj(a) − φ_iijj(b)|: median 0.1, 90th percentile 0.3, max 3.6 cm⁻¹ (max |φ_iijj| 554.7)
- cubic route spread (max − min of the three routes): median 0.02, max 1.6 cm⁻¹
- totally symmetric modes (|φ_iii| > 5 cm⁻¹, non-degenerate): [(6, 534.8), (8, 615.7), (10, 773.8), (20, 1039.0), (21, 1057.4), (25, 1251.2), (27, 1340.5), (28, 1402.1), (30, 1464.6), (32, 1549.4), (33, 1618.5), (34, 1621.0), (37, 3182.0), (39, 3205.0), (41, 3222.7)]

| degenerate pair (ω) | j (ω) | φ_aa,jj | φ_bb,jj | difference | route disagreement a / b |
|---|---|---|---|---|---|

## VPT2 fundamentals (deperturbation window 200.0 cm⁻¹, min K 0.0; 2390 resonances deperturbed; polyad diagonalisation not applied)

| mode | ω | ν raw quartics | ν − ω | ν symmetry-averaged quartics | ν − ω | pyVPT2 ν | pair |
|---|---|---|---|---|---|---|---|
| 0 | 179.4 | 173.2 | -6.2 | 173.2 | -6.2 | — |  |
| 1 | 186.7 | 182.6 | -4.1 | 182.6 | -4.1 | — |  |
| 2 | 396.8 | 394.2 | -2.7 | 394.2 | -2.7 | — |  |
| 3 | 417.2 | 408.4 | -8.8 | 408.4 | -8.8 | — |  |
| 4 | 482.1 | 473.3 | -8.9 | 473.3 | -8.9 | — |  |
| 5 | 504.6 | 495.6 | -9.0 | 495.6 | -9.0 | — |  |
| 6 | 534.8 | 529.0 | -5.8 | 529.0 | -5.8 | — |  |
| 7 | 544.2 | 538.2 | -5.9 | 538.2 | -5.9 | — |  |
| 8 | 615.7 | 609.0 | -6.7 | 609.0 | -6.7 | — |  |
| 9 | 654.6 | 643.4 | -11.3 | 643.4 | -11.3 | — |  |
| 10 | 773.8 | 762.4 | -11.4 | 762.4 | -11.4 | — |  |
| 11 | 779.6 | 766.7 | -12.8 | 766.7 | -12.8 | — |  |
| 12 | 818.7 | 804.0 | -14.7 | 804.0 | -14.7 | — |  |
| 13 | 849.8 | 839.7 | -10.1 | 839.7 | -10.1 | — |  |
| 14 | 888.8 | 872.7 | -16.2 | 872.7 | -16.2 | — |  |
| 15 | 900.5 | 884.1 | -16.4 | 884.1 | -16.4 | — |  |
| 16 | 965.1 | 952.2 | -12.9 | 952.2 | -12.9 | — |  |
| 17 | 977.6 | 965.0 | -12.7 | 965.0 | -12.7 | — |  |
| 18 | 986.5 | 969.3 | -17.3 | 969.3 | -17.3 | — |  |
| 19 | 1005.3 | 988.0 | -17.3 | 988.0 | -17.3 | — |  |
| 20 | 1039.0 | 1022.3 | -16.7 | 1022.3 | -16.7 | — |  |
| 21 | 1057.4 | 1037.9 | -19.5 | 1037.9 | -19.5 | — |  |
| 22 | 1154.9 | 1138.7 | -16.2 | 1138.7 | -16.2 | — |  |
| 23 | 1173.2 | 1157.8 | -15.4 | 1157.8 | -15.4 | — |  |
| 24 | 1243.2 | 1222.3 | -20.8 | 1222.3 | -20.8 | — |  |
| 25 | 1251.2 | 1227.1 | -24.1 | 1227.1 | -24.1 | — |  |
| 26 | 1297.5 | 1276.5 | -21.0 | 1276.5 | -21.0 | — |  |
| 27 | 1340.5 | 1314.1 | -26.5 | 1314.1 | -26.5 | — |  |
| 28 | 1402.1 | 1369.2 | -32.9 | 1369.2 | -32.9 | — |  |
| 29 | 1425.6 | 1398.3 | -27.2 | 1398.3 | -27.2 | — |  |
| 30 | 1464.6 | 1434.6 | -30.1 | 1434.6 | -30.1 | — |  |
| 31 | 1515.2 | 1484.5 | -30.7 | 1484.5 | -30.7 | — |  |
| 32 | 1549.4 | 1513.9 | -35.4 | 1513.9 | -35.4 | — |  |
| 33 | 1618.5 | 1579.8 | -38.7 | 1579.8 | -38.7 | — |  |
| 34 | 1621.0 | 1583.0 | -38.0 | 1583.0 | -38.0 | — |  |
| 35 | 1672.0 | 1635.2 | -36.8 | 1635.2 | -36.8 | — |  |
| 36 | 3163.9 | 3015.8 | -148.2 | 3015.8 | -148.2 | — |  |
| 37 | 3182.0 | 3036.1 | -145.9 | 3036.1 | -145.9 | — |  |
| 38 | 3192.3 | 3051.8 | -140.5 | 3051.8 | -140.5 | — |  |
| 39 | 3205.0 | 3065.7 | -139.3 | 3065.7 | -139.3 | — |  |
| 40 | 3218.6 | 3079.9 | -138.7 | 3079.9 | -138.7 | — |  |
| 41 | 3222.7 | 3084.7 | -138.1 | 3084.7 | -138.1 | — |  |

## Provenance

- timestamp_utc: `2026-11-04 07:38:25`
- host: `Asus18`
- python: `3.14.6`
- numpy: `2.5.1`
- command: `qff.py C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\s2_anharmonic_2026-10-18\s2\A_7aa232d4e9\G\hess --disp 0.10 --out C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\s2_anharmonic_2026-10-18\s2\A_7aa232d4e9\G\qff_report.md`
- commit: `648a001eb6cfa32df774b73c6e2f0d91dadb87c4`
- dirty: `yes`
