# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1b_c05 (2026-11-20 10:34)

recipe: lr 0.000105, epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 20; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 1 | (a) | 0.95 | 3.73 | 0.25 | 3.00 | 23.37 | 0.207 | 19397 |
| 913 | 1 | (b) | 1.06 | 3.87 | 0.27 | 2.84 | 22.93 | 0.225 | 19397 |
| 913 | 1 | (sel) | 1.86 | 4.09 | 0.46 | 3.74 | 22.92 | 0.315 | 19397 |

wall 19865 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
