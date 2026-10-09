# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_overfit (2026-09-30 22:46)

recipe: lr 0.001, epochs 3, loss registered, aux weight 1.0, internal term all, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; overfit-one A_8448043181 (diagnostic 2)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | (a) | 7.09 | 3.30 | 2.15 | 52.92 | 25.01 | 0.946 | 3 |
| 1 | 0 | (b) | 7.09 | 3.30 | 2.15 | 52.92 | 25.01 | 0.946 | 3 |

wall 29 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
