# ANO test on naphthalene: the read

Rows from `probes\results_m1\ano_step_naphthalene_2026-11-26\rows`. Registration: `GoalGathering/notes/PreRegistration_2026-11-26_ANO_Step_Naphthalene.md`. Harmonic frequency of the composite minus the measured fundamental, cm⁻¹, as computed (no geometry term). The lines are compared on unrounded values.

| species | measured | control (cc-pVTZ step) | ano-pVQZ step | rise | overlap² | judged | flag |
|---|---|---|---|---|---|---|---|
| B3u | 176 | -9.11 | -2.94 | +6.17 | 1.00 | no |  |
| Au | 195 | -15.00 | -9.32 | +5.68 | 1.00 | no |  |
| B1g | 386 | -4.53 | +4.64 | +9.16 | 1.00 | yes |  |
| B2g | 461 | +1.41 | +13.97 | +12.55 | 1.00 | yes |  |
| B3u | 476 | -1.45 | +5.90 | +7.35 | 1.00 | yes |  |
| Au | 581 | +17.51 | +48.58 | +31.07 | 0.99 | yes |  |
| B1g | 717 | +16.93 | +20.47 | +3.54 | 1.00 | yes |  |
| B2g | 770 | -32.55 | +20.01 | +52.56 | 0.92 | yes |  |
| B3u | 782 | +15.72 | +22.72 | +7.00 | 1.00 | yes |  |
| Au | 841 | +2.45 | +12.02 | +9.57 | 1.00 | yes |  |
| B2g | 876 | -3.70 | +25.50 | +29.21 | 0.93 | yes |  |
| B1g | 943 | +0.16 | +23.37 | +23.21 | 1.00 | yes |  |
| B3u | 958 | -3.23 | +25.39 | +28.62 | 1.00 | yes |  |
| Au | 970 | -15.55 | +28.45 | +44.00 | 0.99 | yes |  |
| B2g | 980 | -17.06 | +23.04 | +40.10 | 0.96 | yes |  |

- In plane, C–H stretch (8 modes), ano-pVQZ minus control: mean -4.58, rms 4.64, largest -5.41 cm⁻¹ (not judged: against fundamentals a few cm⁻¹ in plane cannot be read).
- In plane, other in plane (25 modes), ano-pVQZ minus control: mean -3.10, rms 5.56, largest -12.22 cm⁻¹ (not judged: against fundamentals a few cm⁻¹ in plane cannot be read).
- Control pins (19 Nov, line 0.5): B2g 770 -33.0, B2g 980 -17.1, Au 970 -15.6.
- Fitting check: with cc-pV5Z fitting sets the first row's largest change of any element is 1.5e-04 E_h/bohr² (NOT under the line 1e-06).
- psi4 that made the rows: dfmp2_rows_naphthalene_ccpvdz.npz 1.10.2, dfmp2_rows_naphthalene_ccpvtz.npz 1.10.2, rows_mp2_anopvqz.npz 1.11.
- Symmetry spread of the rows (a.u.): dfmp2_rows_naphthalene_ccpvdz.npz 2.8e-05, dfmp2_rows_naphthalene_ccpvtz.npz 3.4e-05, rows_mp2_anopvqz.npz 3.2e-05.

**Outcome: TRANSFERS** — the B2g mode at 770 rises by +52.6 cm⁻¹ (overlap² of its two mode vectors 0.92); the lowest judged out-of-plane harmonic is +4.6 from its fundamental (B1g 386); rise at or over 20.0 and no judged mode more than 5.0 below its fundamental; read as computed at the B3LYP geometry, without the geometry term (on benzene that term moves a C–H wag by up to about 20 cm⁻¹ down), so a C–H wag's place above its fundamental is flattered here; the fitting check is over its line of 1e-06 E_h/bohr² (1.5e-04).
