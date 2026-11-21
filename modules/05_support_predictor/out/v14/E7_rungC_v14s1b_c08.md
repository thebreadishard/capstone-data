# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c08 (2026-11-20 23:13)

recipe: lr 0.000986, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.82 | 3.73 | 0.22 | 2.92 | 23.37 | 0.168 | 7128 |
| 913 | 1 | (b) | 0.86 | 3.87 | 0.22 | 2.50 | 22.93 | 0.183 | 7128 |
| 913 | 1 | (sel) | 1.69 | 4.09 | 0.41 | 3.39 | 22.92 | 0.280 | 7128 |

wall 7600 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
