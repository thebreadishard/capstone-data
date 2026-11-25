# Rung C (equivariant ΔH, C1 from scratch) — out/head296/overfit_cartesian_lr1e-3 (2026-11-23 13:37)

recipe: lr 0.001, epochs 5000, loss registered, aux weight 0.1, internal term all, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; overfit-one A_8448043181 (diagnostic 2)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | (a) | 1.90 | 3.30 | 0.58 | 16.61 | 25.01 | 0.592 | 79 |
| 1 | 0 | (b) | 1.90 | 3.30 | 0.58 | 16.61 | 25.01 | 0.592 | 79 |

wall 146 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
