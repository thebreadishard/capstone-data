# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s2_c10 (2026-11-23 03:03)

recipe: lr 0.000244 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 2 | (a) | 0.74 | 3.73 | 0.20 | 4.53 | 23.37 | 0.194 | 24092 |
| 913 | 2 | (b) | 0.83 | 3.87 | 0.21 | 2.33 | 22.93 | 0.184 | 24092 |
| 913 | 2 | (sel) | 1.67 | 4.09 | 0.41 | 3.80 | 22.92 | 0.292 | 24092 |

wall 24560 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
