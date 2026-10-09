# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_hybrid (2026-09-30 22:59) — SMOKE, not a result

recipe: lr 0.001, epochs 200, loss registered, aux weight 1.0, internal term pattern, output scale rms, inner validation 0.0, patience 20; pool layers A,A2; sum aggregation; hybrid head + SQM α

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 1.73 | 3.09 | 0.56 | 13.07 | 24.00 | 0.450 | 27 |
| 5 | 0 | (b) | 3.03 | 3.99 | 0.76 | 8.04 | 23.08 | 0.586 | 27 |

wall 53 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
