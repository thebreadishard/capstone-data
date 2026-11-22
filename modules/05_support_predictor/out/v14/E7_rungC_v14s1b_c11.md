# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c11 (2026-11-21 12:08)

recipe: lr 0.000352 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.94 | 3.73 | 0.25 | 3.95 | 23.37 | 0.216 | 8610 |
| 913 | 1 | (b) | 1.03 | 3.87 | 0.27 | 2.82 | 22.93 | 0.221 | 8610 |
| 913 | 1 | (sel) | 1.82 | 4.09 | 0.45 | 4.06 | 22.92 | 0.321 | 8610 |

wall 9036 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
