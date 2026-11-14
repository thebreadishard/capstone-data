# CPHF check, D_ac28161d06 (b3lyp, grid (99, 590), pyscf 2.15.0)

Verdict: **NOT CPHF** (tolerance 2.0 cm-1)

| route | frequency along v (cm-1) |
|---|---|
| label (pyscf 2.14.0 analytic) | -9.46 |
| pyscf 2.15.0 analytic | -9.45 |
| option 3 control (frozen-grid gradients, steps 0.01/0.02 bohr) | +3.38 / +3.56 |

Lowest projected frequency: label -9.46, 2.15.0 -9.45 cm-1.
Per mode, 2.15.0 minus label: rms 0.003, max |Δ| 0.018 cm-1; below 100 cm-1 (3 modes) rms 0.0018079992989443762 cm-1.
Translation residual max|H t|: label 8.70e-05, analytic_215 8.69e-05.
