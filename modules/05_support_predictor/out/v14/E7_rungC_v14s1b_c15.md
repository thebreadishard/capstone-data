# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c15 (2026-11-22 08:45)

recipe: lr 0.000178, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.78 | 3.73 | 0.21 | 3.47 | 23.37 | 0.187 | 13994 |
| 913 | 1 | (b) | 0.86 | 3.87 | 0.22 | 2.38 | 22.93 | 0.177 | 13994 |
| 913 | 1 | (sel) | 1.67 | 4.09 | 0.41 | 3.28 | 22.92 | 0.275 | 13994 |

wall 14445 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
