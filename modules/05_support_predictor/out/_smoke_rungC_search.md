# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_search (2026-09-27 20:11) — SMOKE, not a result

recipe: lr 0.001, epochs 2, loss internal, aux weight 0.1, output scale class, inner validation 0.4, patience 1; pool layers A,A2

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 5.78 | 3.09 | 1.87 | 57.04 | 24.00 | 1.469 | 2 |
| 5 | 0 | (b) | 7.69 | 3.99 | 1.93 | 80.74 | 23.08 | 1.732 | 2 |

wall 15 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
