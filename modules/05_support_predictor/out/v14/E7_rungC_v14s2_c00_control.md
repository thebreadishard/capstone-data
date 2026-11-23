# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s2_c00_control (2026-11-22 17:18)

recipe: lr 0.0003, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 2 | (a) | 0.72 | 3.73 | 0.19 | 2.70 | 23.37 | 0.146 | 4112 |
| 913 | 2 | (b) | 0.90 | 3.87 | 0.23 | 2.35 | 22.93 | 0.187 | 4112 |
| 913 | 2 | (sel) | 1.66 | 4.09 | 0.41 | 3.30 | 22.92 | 0.273 | 4112 |

wall 4634 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
