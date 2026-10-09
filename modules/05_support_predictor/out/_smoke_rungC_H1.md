# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_H1 (2026-10-01 03:43) — SMOKE, not a result

recipe: lr 0.0003, epochs 2, loss registered, aux weight 0.1, internal term pattern, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; hybrid head + SQM α + rung B pair features

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 2.91 | 3.09 | 0.94 | 20.38 | 24.00 | 0.839 | 2 |
| 5 | 0 | (b) | 3.89 | 3.99 | 0.98 | 18.73 | 23.08 | 0.830 | 2 |

wall 24 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
