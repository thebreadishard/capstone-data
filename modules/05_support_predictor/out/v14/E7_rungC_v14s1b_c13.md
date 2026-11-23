# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c13 (2026-11-22 02:49)

recipe: lr 0.000258, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.61 | 3.73 | 0.16 | 2.72 | 23.37 | 0.137 | 15981 |
| 913 | 1 | (b) | 0.78 | 3.87 | 0.20 | 2.19 | 22.93 | 0.165 | 15981 |
| 913 | 1 | (sel) | 1.62 | 4.09 | 0.40 | 3.34 | 22.92 | 0.266 | 15981 |

wall 16446 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
