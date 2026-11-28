# Step 0: the fitting sets on naphthalene's out-of-plane rows

Rows replaced (cc-pV5Z fitting sets): [11, 38] of the rows along z [2, 8, 11, 32, 38]; the plane's normal has cosine 0.988 along that axis. Atoms of the replaced orbits: [3, 8, 12, 13, 16, 17]. psi4: rows_mp2_anopvqz.npz 1.11, rows_mp2_anopvqz_fit5z_oop.npz 1.11.

Change of each replaced row against the same row with cc-pVQZ fitting sets, E_h/bohr²:

| row | largest change of an element | rms | diagonal |
|---|---|---|---|
| 11 | 2.2e-04 | 8.0e-05 | -9.5e-06 |
| 38 | 1.6e-04 | 3.3e-05 | +8.5e-06 |

Symmetry spread of the build: 3.2e-05 with the rows as they are, 4.0e-04 with the rows replaced (a.u.).

| species | measured | harmonic, cc-pVQZ fitting | with the rows replaced | move | overlap² | share on the replaced orbits |
|---|---|---|---|---|---|---|
| B1g | 386 | 390.64 | 390.67 | +0.03 | 1.00 | 0.20 |
| B2g | 461 | 474.97 | 475.00 | +0.03 | 1.00 | 0.23 |
| B3u | 476 | 481.90 | 481.84 | -0.06 | 1.00 | 0.71 |
| Au | 581 | 629.58 | 629.59 | +0.01 | 1.00 | 0.06 |
| B1g | 717 | 737.47 | 737.48 | +0.01 | 1.00 | 0.37 |
| B2g | 770 | 790.01 | 789.97 | -0.04 | 1.00 | 0.77 |
| B3u | 782 | 804.72 | 804.75 | +0.03 | 1.00 | 0.27 |
| Au | 841 | 853.02 | 853.05 | +0.03 | 1.00 | 0.61 |
| B2g | 876 | 901.50 | 901.52 | +0.02 | 1.00 | 0.53 |
| B1g | 943 | 966.37 | 966.41 | +0.04 | 1.00 | 0.41 |
| B3u | 958 | 983.39 | 983.45 | +0.05 | 1.00 | 0.49 |
| Au | 970 | 998.45 | 998.48 | +0.03 | 1.00 | 0.21 |
| B2g | 980 | 1003.04 | 1003.07 | +0.03 | 1.00 | 0.24 |

**Outcome: HOLDS** — the largest move of a judged mode is -0.06 cm⁻¹ (B3u 476; line 1.0); 2 of the 5 rows along the axis are replaced: elements coupling a replaced orbit to one that is not carry half the change, so the read is partial for every mode — a MOVES shows that the fitting sets matter, a HOLDS is not a verdict before the other rows are replaced; the frame axis has cosine 0.988 along the plane's normal, so about 2 % of the out-of-plane block comes from rows that are not replaced.
