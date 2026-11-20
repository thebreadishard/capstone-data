# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1a_c15 (2026-11-19 18:03)

recipe: lr 0.000178, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 0 | (a) | 0.73 | 3.73 | 0.20 | 2.46 | 23.37 | 0.136 | 18196 |
| 913 | 0 | (b) | 0.85 | 3.87 | 0.22 | 2.31 | 22.93 | 0.179 | 18196 |
| 913 | 0 | (sel) | 1.72 | 4.09 | 0.42 | 3.14 | 22.92 | 0.277 | 18196 |

wall 18697 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
