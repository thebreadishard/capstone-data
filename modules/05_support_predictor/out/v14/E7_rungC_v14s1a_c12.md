# Rung C (equivariant ΔH, C1 from scratch) — out/v14/E7_rungC_v14s1a_c12 (2026-11-19 04:14)

recipe: lr 0.000247 (cosine schedule), epochs 300, loss registered, aux weight 1.0, internal term both, output scale rms, inner validation 0.15, patience 300; pool layers A,A2,B,P3,P3c; sum aggregation; hybrid head + SQM α; pattern f; ls pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 913 | 0 | (a) | 0.88 | 3.73 | 0.24 | 4.16 | 23.37 | 0.198 | 24318 |
| 913 | 0 | (b) | 0.93 | 3.87 | 0.24 | 2.31 | 22.93 | 0.196 | 24318 |
| 913 | 0 | (sel) | 1.84 | 4.09 | 0.45 | 4.04 | 22.92 | 0.319 | 24318 |

wall 24745 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
