# E7 / rung B — pairwise local force-constant terms, learned and projected (2026-09-27 08:44) — SMOKE, NOT A RESULT

443 molecules; hold-out (a) 42 layer-A molecules, (b) scaffold cores ['fluoranthene', 'fluorene'] (39); pool 219; sizes [219]; seeds [0]; 2 epochs; 66 pair features; pattern pairs per molecule 414–4712. RMS in cm⁻¹; MLP mean over seeds.

| n | hold-out | model | diag CH-stretch | diag CH-oop | diag ring-ip | diag other | ring coupling RMS / zero | ratio | ring block / median | corrected ω RMS (zero) | overlap | ΔH residual |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 219 | (a) | zero rule | 43.71 | 23.88 | 20.09 | 19.95 | 4.35 / 4.35 | **1.00** | 10.97 / 4.08 | 23.45 (23.45) | 0.997 | 1.00 |
| 219 | (a) | B1 MLP | 7.32 | 14.59 | 10.57 | 13.02 | 3.02 / 4.35 | **0.69** | 5.14 / 4.08 | 9.14 (23.45) | 0.997 | 0.52 |
| 219 | (a) | B2 GBT | 8.02 | 10.41 | 9.64 | 15.32 | 2.83 / 4.35 | **0.65** | 2.98 / 4.08 | 8.25 (23.45) | 0.998 | 0.50 |
| 219 | (b) | zero rule | 44.30 | 25.32 | 19.93 | 19.18 | 3.74 / 3.74 | **1.00** | 13.23 / 1.21 | 23.09 (23.09) | 0.986 | 1.00 |
| 219 | (b) | B1 MLP | 6.80 | 15.23 | 9.28 | 11.52 | 2.27 / 3.74 | **0.61** | 5.34 / 1.21 | 8.18 (23.09) | 0.990 | 0.45 |
| 219 | (b) | B2 GBT | 8.76 | 11.32 | 7.76 | 12.40 | 2.24 / 3.74 | **0.60** | 3.22 / 1.21 | 7.75 (23.09) | 0.992 | 0.45 |
| 219 | (c) | zero rule | 44.09 | 22.68 | 20.39 | 19.12 | 3.95 / 3.95 | **1.00** | 13.80 / 1.32 | 22.85 (22.85) | 0.989 | 1.00 |
| 219 | (c) | B1 MLP | 6.60 | 12.89 | 11.10 | 7.37 | 3.02 / 3.95 | **0.76** | 5.11 / 1.32 | 8.56 (22.85) | 0.989 | 0.57 |
| 219 | (c) | B2 GBT | 8.21 | 9.52 | 9.46 | 12.75 | 2.84 / 3.95 | **0.72** | 3.50 / 1.32 | 8.13 (22.85) | 0.992 | 0.54 |

## Readings (pre-registered)

- B1 MLP ring coupling ratio vs n: (a) 219: 0.69 (slope +nan); (b) 219: 0.61 (slope +nan)
- Verdict at n = 219: ratio (a) 0.69, (b) 0.61, slope (a) +nan → **between** (win: ≤ 0.6 on both and a negative slope; lose: ≥ 0.9 on (a))

Total 49 s.
