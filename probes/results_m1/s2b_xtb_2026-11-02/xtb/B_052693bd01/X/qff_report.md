# Quartic force field from 43 displaced Hessians — probes/results_m1/s2b_xtb_2026-11-02/xtb/B_052693bd01/X/hess

Reference file `ref.json`; 21 vibrational modes; displacement 0.1 in reduced coordinates; assignment residual max 6.58e-15.
Harmonic ω (cm⁻¹): 161.6, 162.1, 479.8, 532.8, 580.9, 625.7, 683.3, 761.6, 821.9, 903.9, 1004.3, 1044.7, 1117.5, 1144.2, 1244.9, 1289.5, 1504.5, 1532.8, 2391.3, 3190.2, 3192.0

## Noise diagnostics

Off-diagonal semi-diagonal quartic constants φ_iijj have two independent finite-difference routes (displace j and read H_ii; displace i and read H_jj). Their difference is a direct estimate of the numerical error of that constant. Exactly degenerate pairs (a, b) must give equal φ_aa,jj and φ_bb,jj for every totally symmetric j; their difference is a second estimate.

- route disagreement |φ_iijj(a) − φ_iijj(b)|: median 0.0, 90th percentile 0.0, max 1.1 cm⁻¹ (max |φ_iijj| 789.5)
- cubic route spread (max − min of the three routes): median 0.00, max 2.9 cm⁻¹
- totally symmetric modes (|φ_iii| > 5 cm⁻¹, non-degenerate): [(4, 580.9), (10, 1004.3), (11, 1044.7), (12, 1117.5), (13, 1144.2), (14, 1244.9), (15, 1289.5), (16, 1504.5), (17, 1532.8), (18, 2391.3), (19, 3190.2), (20, 3192.0)]

| degenerate pair (ω) | j (ω) | φ_aa,jj | φ_bb,jj | difference | route disagreement a / b |
|---|---|---|---|---|---|

## VPT2 fundamentals (deperturbation window 200.0 cm⁻¹, min K 0.0; 353 resonances deperturbed; polyad diagonalisation not applied)

| mode | ω | ν raw quartics | ν − ω | ν symmetry-averaged quartics | ν − ω | pyVPT2 ν | pair |
|---|---|---|---|---|---|---|---|
| 0 | 161.6 | 161.5 | -0.1 | 161.5 | -0.1 | — |  |
| 1 | 162.1 | 161.5 | -0.6 | 161.5 | -0.6 | — |  |
| 2 | 479.8 | 476.0 | -3.8 | 476.0 | -3.8 | — |  |
| 3 | 532.8 | 530.1 | -2.7 | 530.1 | -2.7 | — |  |
| 4 | 580.9 | 576.0 | -4.9 | 576.0 | -4.9 | — |  |
| 5 | 625.7 | 615.6 | -10.0 | 615.6 | -10.0 | — |  |
| 6 | 683.3 | 675.8 | -7.5 | 675.8 | -7.5 | — |  |
| 7 | 761.6 | 749.1 | -12.5 | 749.1 | -12.5 | — |  |
| 8 | 821.9 | 806.8 | -15.1 | 806.8 | -15.1 | — |  |
| 9 | 903.9 | 893.8 | -10.1 | 893.8 | -10.1 | — |  |
| 10 | 1004.3 | 991.2 | -13.1 | 991.2 | -13.1 | — |  |
| 11 | 1044.7 | 1026.1 | -18.7 | 1026.1 | -18.7 | — |  |
| 12 | 1117.5 | 1098.4 | -19.1 | 1098.4 | -19.1 | — |  |
| 13 | 1144.2 | 1113.4 | -30.7 | 1113.4 | -30.7 | — |  |
| 14 | 1244.9 | 1221.1 | -23.8 | 1221.1 | -23.8 | — |  |
| 15 | 1289.5 | 1261.5 | -28.0 | 1261.5 | -28.0 | — |  |
| 16 | 1504.5 | 1474.7 | -29.9 | 1474.7 | -29.9 | — |  |
| 17 | 1532.8 | 1500.0 | -32.8 | 1500.0 | -32.8 | — |  |
| 18 | 2391.3 | 2356.6 | -34.7 | 2356.6 | -34.7 | — |  |
| 19 | 3190.2 | 3031.7 | -158.5 | 3031.7 | -158.5 | — |  |
| 20 | 3192.0 | 3033.8 | -158.2 | 3033.8 | -158.2 | — |  |

## Provenance

- timestamp_utc: `2026-11-12 00:42:42`
- host: `Asus18`
- python: `3.13.15`
- numpy: `2.5.3`
- command: `qff.py probes/results_m1/s2b_xtb_2026-11-02/xtb/B_052693bd01/X/hess --disp 0.10 --out probes/results_m1/s2b_xtb_2026-11-02/xtb/B_052693bd01/X/qff_report.md`
