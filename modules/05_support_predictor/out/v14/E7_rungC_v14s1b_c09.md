# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c09 (2026-11-21 01:19)

recipe: lr 0.000394 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.70 | 3.73 | 0.19 | 2.94 | 23.37 | 0.144 | 14054 |
| 913 | 1 | (b) | 0.83 | 3.87 | 0.21 | 2.20 | 22.93 | 0.178 | 14054 |
| 913 | 1 | (sel) | 1.71 | 4.09 | 0.42 | 3.46 | 22.92 | 0.285 | 14054 |

wall 14476 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
