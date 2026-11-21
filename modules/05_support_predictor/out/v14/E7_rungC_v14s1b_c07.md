# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c07 (2026-11-20 17:43)

recipe: lr 0.000489 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.64 | 3.73 | 0.17 | 3.62 | 23.37 | 0.160 | 19310 |
| 913 | 1 | (b) | 0.77 | 3.87 | 0.20 | 2.10 | 22.93 | 0.163 | 19310 |
| 913 | 1 | (sel) | 1.61 | 4.09 | 0.39 | 3.56 | 22.92 | 0.275 | 19310 |

wall 19737 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
