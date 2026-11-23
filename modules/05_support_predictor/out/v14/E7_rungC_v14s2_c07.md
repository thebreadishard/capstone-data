# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s2_c07 (2026-11-22 18:34)

recipe: lr 0.000489 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 2 | (a) | 0.70 | 3.73 | 0.19 | 2.68 | 23.37 | 0.139 | 19824 |
| 913 | 2 | (b) | 0.79 | 3.87 | 0.20 | 2.15 | 22.93 | 0.167 | 19824 |
| 913 | 2 | (sel) | 1.62 | 4.09 | 0.40 | 3.17 | 22.92 | 0.265 | 19824 |

wall 20258 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
