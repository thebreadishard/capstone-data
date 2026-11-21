# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c04 (2026-11-20 07:49)

recipe: lr 0.000612 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.83 | 3.73 | 0.22 | 2.75 | 23.37 | 0.173 | 9401 |
| 913 | 1 | (b) | 0.93 | 3.87 | 0.24 | 2.48 | 22.93 | 0.202 | 9401 |
| 913 | 1 | (sel) | 1.75 | 4.09 | 0.43 | 3.49 | 22.92 | 0.299 | 9401 |

wall 9832 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
