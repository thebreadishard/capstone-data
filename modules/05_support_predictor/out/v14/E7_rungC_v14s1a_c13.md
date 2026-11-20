# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1a_c13 (2026-11-19 11:08)

recipe: lr 0.000258, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 0 | (a) | 0.67 | 3.73 | 0.18 | 3.17 | 23.37 | 0.166 | 16687 |
| 913 | 0 | (b) | 0.80 | 3.87 | 0.21 | 2.27 | 22.93 | 0.170 | 16687 |
| 913 | 0 | (sel) | 1.66 | 4.09 | 0.40 | 3.36 | 22.92 | 0.270 | 16687 |

wall 17173 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
