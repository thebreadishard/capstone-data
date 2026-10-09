# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_tensor (2026-09-30 22:51) — SMOKE, not a result

recipe: lr 0.001, epochs 200, loss registered, aux weight 1.0, internal term pattern, output scale rms, inner validation 0.0, patience 20; pool layers A,A2; sum aggregation; rank-2 tensor input

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 3.12 | 3.09 | 1.01 | 21.61 | 24.00 | 0.921 | 20 |
| 5 | 0 | (b) | 4.04 | 3.99 | 1.01 | 20.36 | 23.08 | 0.914 | 20 |

wall 45 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
