# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_mean (2026-09-28 10:08) — SMOKE, not a result

recipe: lr 0.001, epochs 2, loss registered, aux weight 0.1, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; mean aggregation

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 3.67 | 3.09 | 1.19 | 40.96 | 24.00 | 0.999 | 2 |
| 5 | 0 | (b) | 4.98 | 3.99 | 1.25 | 43.01 | 23.08 | 0.978 | 2 |

wall 43 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
