# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c02_control_target (2026-11-20 02:29)

recipe: lr 0.0003, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.75 | 3.73 | 0.20 | 2.88 | 23.37 | 0.161 | 8490 |
| 913 | 1 | (b) | 0.83 | 3.87 | 0.21 | 2.50 | 22.93 | 0.179 | 8490 |
| 913 | 1 | (sel) | 1.66 | 4.09 | 0.41 | 3.40 | 22.92 | 0.276 | 8490 |

wall 8975 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
