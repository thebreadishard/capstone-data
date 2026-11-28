# Step 0: the fitting sets on naphthalene's out-of-plane rows

Rows replaced (cc-pV5Z fitting sets): [2, 8, 11, 32, 38] of the rows along z [2, 8, 11, 32, 38]; the plane's normal has cosine 0.988 along that axis. Atoms of the replaced orbits: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]. psi4: rows_mp2_anopvqz.npz 1.11, rows_mp2_anopvqz_fit5z_oop.npz 1.11.

Change of each replaced row against the same row with cc-pVQZ fitting sets, E_h/bohr²:

| row | largest change of an element | rms | diagonal |
|---|---|---|---|
| 2 | 1.7e-04 | 6.1e-05 | -2.8e-05 |
| 8 | 1.4e-04 | 4.8e-05 | -9.9e-06 |
| 11 | 2.2e-04 | 8.0e-05 | -9.5e-06 |
| 32 | 1.1e-04 | 2.5e-05 | +6.6e-06 |
| 38 | 1.6e-04 | 3.3e-05 | +8.5e-06 |

Symmetry spread of the build: 3.2e-05 with the rows as they are, 4.0e-04 with the rows replaced (a.u.).

| species | measured | harmonic, cc-pVQZ fitting | with the rows replaced | move | overlap² | share on the replaced orbits |
|---|---|---|---|---|---|---|
| B1g | 386 | 390.64 | 390.70 | +0.06 | 1.00 | 1.00 |
| B2g | 461 | 474.97 | 474.99 | +0.02 | 1.00 | 1.00 |
| B3u | 476 | 481.90 | 481.87 | -0.03 | 1.00 | 1.00 |
| Au | 581 | 629.58 | 629.52 | -0.06 | 1.00 | 1.00 |
| B1g | 717 | 737.47 | 737.48 | +0.01 | 1.00 | 1.00 |
| B2g | 770 | 790.01 | 789.94 | -0.07 | 1.00 | 1.00 |
| B3u | 782 | 804.72 | 804.76 | +0.04 | 1.00 | 1.00 |
| Au | 841 | 853.02 | 853.06 | +0.04 | 1.00 | 1.00 |
| B2g | 876 | 901.50 | 901.54 | +0.03 | 1.00 | 1.00 |
| B1g | 943 | 966.37 | 966.44 | +0.07 | 1.00 | 1.00 |
| B3u | 958 | 983.39 | 983.48 | +0.09 | 1.00 | 1.00 |
| Au | 970 | 998.45 | 998.55 | +0.10 | 1.00 | 1.00 |
| B2g | 980 | 1003.04 | 1003.14 | +0.10 | 1.00 | 1.00 |

**Outcome: HOLDS** — the largest move of a judged mode is +0.10 cm⁻¹ (Au 970; line 1.0); the frame axis has cosine 0.988 along the plane's normal, so about 2 % of the out-of-plane block comes from rows that are not replaced.
