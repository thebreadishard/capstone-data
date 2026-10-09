# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_scale (2026-09-30 21:40) — SMOKE, not a result

recipe: lr 0.001, epochs 200, loss registered, aux weight 1.0, output scale rms, inner validation 0.0, patience 20; pool layers A,A2,B; sum aggregation

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 3.03 | 3.09 | 0.98 | 12.30 | 24.00 | 0.777 | 12 |
| 5 | 0 | (b) | 4.09 | 3.99 | 1.03 | 11.48 | 23.08 | 0.784 | 12 |

wall 34 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
