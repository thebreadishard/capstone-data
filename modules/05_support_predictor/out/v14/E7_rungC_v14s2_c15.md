# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s2_c15 (2026-11-23 00:13)

recipe: lr 0.000178, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 2 | (a) | 0.72 | 3.73 | 0.19 | 3.36 | 23.37 | 0.170 | 9751 |
| 913 | 2 | (b) | 0.83 | 3.87 | 0.21 | 2.30 | 22.93 | 0.175 | 9751 |
| 913 | 2 | (sel) | 1.70 | 4.09 | 0.42 | 3.74 | 22.92 | 0.288 | 9751 |

wall 10266 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
