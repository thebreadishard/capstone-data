# Rung C (equivariant ΔH, C1 from scratch) — out/v14_smoke/c03_control_schedule (2026-11-15 21:51) — SMOKE, not a result

recipe: lr 0.0003 (cosine schedule), epochs 7, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 7; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 2.62 | 3.04 | 0.86 | 12.34 | 23.80 | 0.637 | 4 |
| 5 | 0 | (b) | 3.53 | 3.94 | 0.89 | 10.92 | 22.75 | 0.656 | 4 |
| 5 | 0 | (sel) | 3.74 | 4.09 | 0.91 | 11.81 | 22.92 | 0.669 | 4 |

wall 162 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
