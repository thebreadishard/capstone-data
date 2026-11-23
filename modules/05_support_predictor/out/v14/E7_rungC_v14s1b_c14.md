# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c14 (2026-11-22 07:22)

recipe: lr 0.000188, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.72 | 3.73 | 0.19 | 3.27 | 23.37 | 0.160 | 4546 |
| 913 | 1 | (b) | 0.85 | 3.87 | 0.22 | 2.42 | 22.93 | 0.183 | 4546 |
| 913 | 1 | (sel) | 1.65 | 4.09 | 0.40 | 3.56 | 22.92 | 0.280 | 4546 |

wall 4969 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
