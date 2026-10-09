# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_pattern_d (2026-10-01 07:12) — SMOKE, not a result

recipe: lr 0.0003, epochs 2, loss registered, aux weight 0.1, internal term pattern, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; hybrid head + SQM α + rung B pair features; pattern d

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 3.02 | 3.09 | 0.98 | 18.22 | 24.00 | 0.821 | 3 |
| 5 | 0 | (b) | 3.96 | 3.99 | 0.99 | 17.02 | 23.08 | 0.818 | 3 |

wall 30 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
