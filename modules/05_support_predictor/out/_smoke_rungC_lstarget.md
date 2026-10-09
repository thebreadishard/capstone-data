# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_lstarget (2026-10-01 09:20) — SMOKE, not a result

recipe: lr 0.0003, epochs 2, loss registered, aux weight 0.1, internal term pattern, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; hybrid head + SQM α + rung B pair features; pattern d; LS pattern target

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 3.10 | 3.09 | 1.00 | 16.30 | 24.00 | 0.792 | 5 |
| 5 | 0 | (b) | 4.01 | 3.99 | 1.01 | 15.25 | 23.08 | 0.803 | 5 |

wall 66 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
