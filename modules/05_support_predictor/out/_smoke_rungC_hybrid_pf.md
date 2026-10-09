# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_hybrid_pf (2026-10-01 02:27) — SMOKE, not a result

recipe: lr 0.001, epochs 200, loss registered, aux weight 1.0, internal term pattern, output scale rms, inner validation 0.0, patience 20; pool layers A,A2; sum aggregation; hybrid head + SQM α + rung B pair features

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 1.72 | 3.09 | 0.56 | 7.29 | 24.00 | 0.284 | 21 |
| 5 | 0 | (b) | 2.69 | 3.99 | 0.67 | 7.99 | 23.08 | 0.509 | 21 |

wall 43 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
