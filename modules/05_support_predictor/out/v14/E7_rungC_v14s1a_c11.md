# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1a_c11 (2026-11-19 01:49)

recipe: lr 0.000352 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 0 | (a) | 0.89 | 3.73 | 0.24 | 3.26 | 23.37 | 0.186 | 8306 |
| 913 | 0 | (b) | 0.95 | 3.87 | 0.24 | 2.52 | 22.93 | 0.199 | 8306 |
| 913 | 0 | (sel) | 1.75 | 4.09 | 0.43 | 3.77 | 22.92 | 0.300 | 8306 |

wall 8786 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
