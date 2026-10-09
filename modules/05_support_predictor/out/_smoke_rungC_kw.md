# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_kw (2026-10-01 15:44) — SMOKE, not a result

recipe: lr 0.0003, epochs 2, loss registered, aux weight 0.1, internal term both, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f; LS pattern target (λ_rel 0.001)

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 2.72 | 3.09 | 0.88 | 18.58 | 24.00 | 0.709 | 7 |
| 5 | 0 | (b) | 3.65 | 3.99 | 0.92 | 16.60 | 23.08 | 0.708 | 7 |

wall 72 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
