# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c10 (2026-11-21 05:21)

recipe: lr 0.000244 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.76 | 3.73 | 0.20 | 3.39 | 23.37 | 0.158 | 24001 |
| 913 | 1 | (b) | 0.87 | 3.87 | 0.22 | 2.43 | 22.93 | 0.185 | 24001 |
| 913 | 1 | (sel) | 1.72 | 4.09 | 0.42 | 3.33 | 22.92 | 0.283 | 24001 |

wall 24427 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
