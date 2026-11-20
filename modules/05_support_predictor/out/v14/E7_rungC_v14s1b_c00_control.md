# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c00_control (2026-11-19 23:14)

recipe: lr 0.0003, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.74 | 3.73 | 0.20 | 3.10 | 23.37 | 0.163 | 5739 |
| 913 | 1 | (b) | 0.82 | 3.87 | 0.21 | 2.20 | 22.93 | 0.169 | 5739 |
| 913 | 1 | (sel) | 1.60 | 4.09 | 0.39 | 3.41 | 22.92 | 0.265 | 5739 |

wall 6185 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
