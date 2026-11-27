# ANO test on benzene: the read — 2026-11-26 03:06

Rows from `probes\results_m1\ano_step_benzene_2026-11-25\rows`. Registration: `GoalGathering/notes/PreRegistration_2026-11-25_ANO_Step_Benzene.md`. Columns: corrected composite minus CCSD(T)/ano-pV5Z, cm⁻¹. The lines are compared on unrounded values.

| mode | species | ano-pV5Z | ANO4321′ (1997) | conventional | recipe 1 | recipe 2 | recipe 3 | recipe 5 | recipe 6 | recipe 7 |
|---|---|---|---|---|---|---|---|---|---|---|
| ω1 | a1g | 1006.6 |  | -2.8 | -2.7 | -8.2 | -8.2 | -9.6 | -10.3 | -14.1 |
| ω2 | a1g | 3204.3 |  | +10.0 | +10.0 | +3.0 | -0.4 | +4.6 | +0.8 | -5.1 |
| ω3 | a2g | 1380.5 |  | -15.8 | -15.8 | -13.4 | -13.7 | -11.5 | -12.9 | -9.2 |
| ω4 | b2g | 712.4 | 708.8 | -36.7 | -36.1 | -24.7 | -15.7 | -1.3 | -15.6 | -10.1 |
| ω5 | b2g | 1012.4 | 1008.8 | -49.9 | -49.8 | -40.7 | -26.3 | -9.5 | -32.7 | -25.9 |
| ω6 | e2g | 611.5 |  | -7.2 | -7.4 | -6.5 | -5.0 | -4.9 | -6.5 | -3.8 |
| ω7 | e2g | 3179.6 |  | +6.3 | +6.4 | +1.6 | -4.9 | +2.8 | +0.0 | -5.5 |
| ω8 | e2g | 1639.3 |  | -3.8 | -3.5 | -12.9 | -12.5 | -12.8 | -16.2 | -20.4 |
| ω9 | e2g | 1191.8 |  | -5.1 | -5.3 | -7.5 | -5.3 | -7.6 | -9.5 | -7.8 |
| ω10 | e1g | 863.4 | 865.1 | -15.1 | -15.0 | -13.9 | -10.3 | -8.6 | -14.4 | -7.5 |
| ω11 | a2u | 683.6 | 687.2 | -7.4 | -7.0 | -6.6 | -3.7 | -7.1 | -8.2 | +0.7 |
| ω12 | b1u | 1024.6 |  | -17.8 | -16.9 | -15.9 | -10.5 | -7.3 | -15.2 | -13.0 |
| ω13 | b1u | 3169.9 |  | +4.7 | +4.8 | +0.5 | -8.0 | +2.6 | -1.0 | -6.4 |
| ω14 | b2u | 1328.6 |  | +6.1 | +6.0 | -6.6 | -1.7 | -6.6 | -12.7 | -21.0 |
| ω15 | b2u | 1158.4 |  | -2.5 | -2.8 | -6.4 | -2.6 | -6.4 | -9.3 | -8.4 |
| ω16 | e2u | 406.3 | 405.8 | -9.5 | -9.6 | -5.3 | -6.7 | -1.1 | -2.2 | +4.6 |
| ω17 | e2u | 987.0 |  | -35.6 | -35.4 | -30.0 | -13.8 | -9.3 | -26.9 | -20.1 |
| ω18 | e1u | 1057.2 |  | -5.7 | -5.7 | -8.5 | -7.1 | -8.8 | -9.7 | -10.0 |
| ω19 | e1u | 1511.3 |  | -7.5 | -7.5 | -10.6 | -9.0 | -10.7 | -12.5 | -12.0 |
| ω20 | e1u | 3195.1 |  | +8.4 | +8.5 | +2.4 | -2.4 | +3.6 | +0.5 | -5.3 |

| rms against ano-pV5Z, corrected (as computed) | C-H stretch | out of plane | other in plane |
|---|---|---|---|
| conventional composite (7 Oct) | 7.64 (29.89) | 30.22 (23.95) | 8.92 (7.95) |
| 1. cc-pVTZ, DF-MP2 (control) | 7.69 (29.83) | 30.01 (23.80) | 8.78 (7.72) |
| 2. cc-pVQZ | 2.08 (35.50) | 23.91 (17.83) | 10.17 (6.89) |
| 3. roos-ano-tz as psi4 ships it (414 functions) | 4.84 (41.46) | 14.71 (12.27) | 8.46 (5.90) |
| 5. ano-pVQZ | 3.48 (33.92) | 7.12 (8.40) | 8.93 (5.08) |
| 6. MP2 basis-set limit from cc-pVTZ and cc-pVQZ | 0.67 (37.35) | 19.64 (13.04) | 11.82 (7.84) |
| 7. recipe 6 + MP2 core-valence (cc-pwCVTZ) | 5.59 (43.11) | 14.47 (13.28) | 13.03 (9.26) |

- Recipe 4 not in the run: ano-pVTZ — no file of the registered shape (amendment 2).
- Control: DF-MP2 minus conventional MP2 in the cc-pVTZ step, corrected rms per group: +0.05 / -0.21 / -0.14 cm⁻¹ (line 0.5).
- Newton step, largest atom displacement in bohr (read up to 0.05), and smallest overlap² of the pairing with the B3LYP modes: conventional 0.0062, 0.586; recipe 1 0.0062, 0.586; recipe 2 0.0062, 0.586; recipe 3 0.0063, 0.586; recipe 5 0.0062, 0.586; recipe 6 0.0062, 0.586; recipe 7 0.0063, 0.586.
- Fitting check, mp2_anopvqz: with cc-pV5Z fitting sets the first row's largest change of any element is 2.2e-05 E_h/bohr² (NOT under the line 1e-06; this is what is judged), the change of its largest element 9.6e-06.
- Fitting check, mp2_roosanotz: with cc-pV5Z fitting sets the first row's largest change of any element is 2.5e-05 E_h/bohr² (NOT under the line 1e-06; this is what is judged), the change of its largest element 1.9e-05.
- psi4 that made the rows: 1.10.2 (every file read).
- Symmetry spread of the rows (a.u.): mp2_anopvqz 2.9e-05, mp2_ccpvdz 2.8e-05, mp2_ccpvqz 3.0e-05, mp2_ccpvtz 3.0e-05, mp2_ccpwcvtz_ae 3.0e-05, mp2_ccpwcvtz_fc 3.0e-05, mp2_roosanotz 3.0e-05, scf_ccpvqz 2.4e-05, scf_ccpvtz 2.3e-05.
- Diagnostic [CCSD(T) − MP2], cc-pVDZ → cc-pVTZ (the conventional MP2 Hessians we hold, as computed): ω4 -14.0 → -15.6 (change -1.6); ω5 -21.3 → -14.2 (change +7.1); ω17 -16.5 → -8.3 (change +8.1); line 5.0 cm⁻¹, crossed.

**Outcome: USEFUL** — recipe(s) 5: out of plane at or under 10.0 cm⁻¹ and no other group more than 1.0 above the control's; the same test follows on a second molecule before anything is adopted; the fitting check of mp2_anopvqz (recipe 5) is over its line of 1e-06 E_h/bohr² (2.2e-05): that recipe's numbers stand under this; the fitting check of mp2_roosanotz (recipe 3) is over its line of 1e-06 E_h/bohr² (2.5e-05): that recipe's numbers stand under this; [CCSD(T) − MP2] changes by more than 5.0 cm⁻¹ between cc-pVDZ and cc-pVTZ on ω5, ω17: the artefact sits in the coupled-cluster part as well, and no MP2 step can remove it there.
