# Rung C (equivariant ΔH, C1 from scratch) — out/_smoke_rungC_kdiag (2026-10-02 04:14) — SMOKE, not a result

recipe: lr 0.0003, epochs 2, loss registered, aux weight 0.1, internal term both, output scale rms, inner validation 0.0, patience 0; pool layers A,A2; sum aggregation; hybrid head + SQM α + rung B pair features; pattern f

| n | seed | hold-out | ring couplings | zero | ratio | corrected ω | zero ω | ΔH residual ratio | s |
|---|---|---|---|---|---|---|---|---|---|
| 5 | 0 | (a) | 3.00 | 3.09 | 0.97 | 13.56 | 24.00 | 0.697 | 4 |
| 5 | 0 | (b) | 3.92 | 3.99 | 0.98 | 11.97 | 23.08 | 0.712 | 4 |

wall 42 s; read-out keys: ['block_median_rule_rms', 'block_rms', 'corrected_freq_rms', 'corrected_freq_rms_zero_rule', 'coupling_ratio', 'coupling_rms', 'coupling_zero_rms', 'dH_residual_ratio', 'diag_rms', 'duschinsky_overlap_median', 'duschinsky_overlap_p10']
