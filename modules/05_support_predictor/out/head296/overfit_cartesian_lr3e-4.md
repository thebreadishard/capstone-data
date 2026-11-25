# Rung C (equivariant ΔH, C1 from scratch) — out/head296/overfit_cartesian_lr3e-4 (2026-11-23 13:39)

recipe: lr 0.0003, epochs 5000, loss registered, aux weight 0.1, internal term all, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; overfit-one A_8448043181 (diagnostic 2)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | (a) | 1.68 | 3.30 | 0.51 | 15.28 | 25.01 | 0.682 | 73 |
| 1 | 0 | (b) | 1.68 | 3.30 | 0.51 | 15.28 | 25.01 | 0.682 | 73 |

wall 132 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
