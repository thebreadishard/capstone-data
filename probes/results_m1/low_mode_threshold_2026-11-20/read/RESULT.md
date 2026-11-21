# The low-mode repair's change of a label mode, against frequency and force constant (TASKS 218)

42 points (re-measured label mode × functional) on 20 molecules; 4 flagged for a coverage or overlap below 0.9 and 11 for two steps more than 0.15 cm⁻¹ apart (15 points have a step check; 1 check point(s) set aside for their own overlap); flagged points are in points.csv and in no statistic. A molecule is 'biased' when a label mode of it lies below 20 cm⁻¹, which is why the repair selected it. 0 point(s) turned imaginary under the patch. 'Noise' is the frequency noise the finite difference makes of 1e-07 hartree/bohr of gradient noise on that mode (see `noise_sensitivity_cm`); the gradient noise itself is not measured here.

## b3lyp, unbiased sample: 13 unflagged points in 20–100 cm⁻¹

| label frequency (cm⁻¹) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| 20–30 | 2 | 3.69 | 4.63 | 2 | 1.00 | 0.00 | 0.23 |
| 30–40 | 3 | 1.08 | 2.28 | 3 | 1.00 | 0.00 | 0.15 |
| 40–50 | 4 | 0.95 | 1.53 | 3 | 0.75 | 0.22 | 0.10 |
| 50–60 | 4 | 0.78 | 1.58 | 2 | 0.50 | 0.25 | 0.15 |
| 60–80 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 80–100 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |

| force constant quartile (hartree/bohr²) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| Q1: 2.00e-04 to 3.40e-04 | 4 | 1.92 | 4.63 | 3 | 0.75 | 0.22 | 0.24 |
| Q2: 3.88e-04 to 4.26e-04 | 3 | 0.85 | 2.28 | 2 | 0.67 | 0.27 | 0.15 |
| Q3: 5.91e-04 to 9.07e-04 | 3 | 0.60 | 1.53 | 2 | 0.67 | 0.27 | 0.12 |
| Q4: 9.21e-04 to 1.64e-03 | 3 | 1.43 | 1.58 | 3 | 1.00 | 0.00 | 0.07 |

Spearman of abs Δ against the label frequency: -0.43 (n = 13); against log k: -0.04 (n = 13). Frequency against log k on the same points: +0.70; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none. Rms of the signed change: 1.86 cm⁻¹.

The rule's arithmetic on this group's points in 20–60 cm⁻¹ (the registered population; its outcome is in the section below): n = 13, 10 moved more than 0.5 cm⁻¹: fewer than the 16 points the rule needs, so it reads nothing from them. Outcome 3: undecided.

## wb97x, unbiased sample: 13 unflagged points in 20–100 cm⁻¹

| label frequency (cm⁻¹) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| 20–30 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 30–40 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 40–50 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 50–60 | 1 | 1.31 | 1.31 | 1 | 1.00 | 0.00 | 0.13 |
| 60–80 | 9 | 0.70 | 1.41 | 6 | 0.67 | 0.16 | 0.07 |
| 80–100 | 3 | 0.68 | 1.37 | 3 | 1.00 | 0.00 | 0.06 |

| force constant quartile (hartree/bohr²) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| Q1: 4.07e-04 to 1.42e-03 | 4 | 0.58 | 1.31 | 3 | 0.75 | 0.22 | 0.16 |
| Q2: 1.51e-03 to 1.99e-03 | 3 | 0.70 | 0.83 | 2 | 0.67 | 0.27 | 0.07 |
| Q3: 2.04e-03 to 2.47e-03 | 3 | 1.10 | 1.41 | 3 | 1.00 | 0.00 | 0.06 |
| Q4: 2.57e-03 to 3.44e-03 | 3 | 0.98 | 1.37 | 2 | 0.67 | 0.27 | 0.06 |

Spearman of abs Δ against the label frequency: -0.01 (n = 13); against log k: +0.23 (n = 13). Frequency against log k on the same points: +0.53; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none. Rms of the signed change: 0.89 cm⁻¹.

The rule's arithmetic on this group's points in 20–60 cm⁻¹ (description only): n = 1, 1 moved more than 0.5 cm⁻¹: fewer than the 16 points the rule needs, so it reads nothing from them. Outcome 3: undecided.

## The registered decision rule

Population: b3lyp, unbiased sample, label frequency 20–60 cm⁻¹, unflagged. 8 checked points differ by more than 0.15 cm⁻¹ between the two steps (B_0af11315e3 mode 0, B_0c6c144a7f mode 0, B_1428bc8164 mode 0, B_1726105aae mode 0, B_3dcbd985e3 mode 0, B_3dcbd985e3 mode 1, B_4ff67f9ea2 mode 0, B_55cca3aaf2 mode 0): the finite difference is not under control here. Outcome 3: undecided; the step check is extended to every sampled molecule before any statement.

Flagged points in the window: 8. Counted as moved: 18 of 21, outcome majority wrong; counted as unmoved: 10 of 21, outcome undecided. The registered fraction stays the one on unflagged points.

Moved per band of the molecule's lowest mode: 20–30: 2 of 2; 30–40: 3 of 3; 40–50: 3 of 4; 50–60: 2 of 4. Weighted by the bands' eligible molecules (41/41/54/146): 0.69 (descriptive; the rule reads the unweighted fraction).

What orders the moves (descriptive): Spearman of abs Δ against the label frequency: -0.43 (n = 13); against log k: -0.04 (n = 13). Frequency against log k on the same points: +0.70; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none.

| registered point | label (cm⁻¹) | patched | Δ | noise per 1e-07 hartree/bohr | other step − this | flags |
|---|---|---|---|---|---|---|
| A2_05e08111d2 mode 0 | 55.45 | 57.02 | +1.58 | 0.09 | not checked |  |
| A2_3ac24b6972 mode 0 | 20.21 | 24.84 | +4.63 | 0.23 | not checked |  |
| B_0af11315e3 mode 0 | 45.74 | 44.37 | -1.37 | 0.11 | +0.23 | step |
| B_0c6c144a7f mode 0 | 23.73 | 23.54 | -0.19 | 1.09 | +0.57 | step |
| B_0d1c7f83df mode 0 | 53.07 | 52.95 | -0.12 | 0.21 | not checked |  |
| B_1139ae8d01 mode 0 | 48.44 | 49.97 | +1.53 | 0.12 | not checked |  |
| B_1428bc8164 mode 0 | 50.50 | 50.65 | +0.15 | 0.07 | +0.29 | step |
| B_14cf57747b mode 0 | 53.20 | 54.63 | +1.43 | 0.06 | not checked |  |
| B_15207e9ed5 mode 0 | 35.22 | 36.06 | +0.85 | 0.14 | not checked |  |
| B_16769b963f mode 0 | 48.06 | 49.37 | +1.30 | 0.07 | not checked |  |
| B_1726105aae mode 0 | 34.30 | 34.70 | +0.40 | 0.14 | +0.42 | step |
| B_19c3319693 mode 0 | 33.08 | 30.80 | -2.28 | 0.15 | not checked |  |
| B_1b434d2cd0 mode 0 | 48.07 | 47.48 | -0.60 | 0.07 | not checked |  |
| B_2326ac497c mode 0 | 21.22 | 18.47 | -2.76 | 0.24 | not checked |  |
| B_3dcbd985e3 mode 0 | 23.71 | 23.79 | +0.08 | 0.24 | +0.44 | step |
| B_3dcbd985e3 mode 1 | 30.28 | 29.93 | -0.35 | 0.71 | +0.27 | step |
| B_477b567fed mode 0 | 40.66 | 40.62 | -0.04 | 0.15 | not checked |  |
| B_4f6ebdb30b mode 0 | 31.00 | 32.07 | +1.08 | 0.23 | not checked |  |
| B_4ff67f9ea2 mode 0 | 32.99 | 32.56 | -0.43 | 0.73 | +0.30 | step |
| B_55cca3aaf2 mode 0 | 23.83 | 22.27 | -1.56 | 1.04 | +0.49 | step |
| B_863cdaad7a mode 0 | 53.76 | 53.78 | +0.02 | 0.28 | not checked |  |

## Flagged points

- A2_3ac24b6972 wb97x mode 1: label 116.00 → 116.57 cm⁻¹, coverage 0.85, overlap after the patch 1.00, flags overlap
- B_0af11315e3 b3lyp mode 0: label 45.74 → 44.37 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_0c6c144a7f b3lyp mode 0: label 23.73 → 23.54 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_0c6c144a7f wb97x mode 0: label 67.12 → 60.18 cm⁻¹, coverage 0.99, overlap after the patch 1.00, flags step
- B_1139ae8d01 wb97x mode 2: label 121.69 → 122.21 cm⁻¹, coverage 0.64, overlap after the patch 1.00, flags overlap
- B_1428bc8164 b3lyp mode 0: label 50.50 → 50.65 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_1428bc8164 wb97x mode 2: label 119.99 → 119.99 cm⁻¹, coverage 0.68, overlap after the patch 1.00, flags overlap
- B_1726105aae b3lyp mode 0: label 34.30 → 34.70 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_3dcbd985e3 b3lyp mode 0: label 23.71 → 23.79 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_3dcbd985e3 b3lyp mode 1: label 30.28 → 29.93 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_477b567fed wb97x mode 0: label 70.73 → 72.95 cm⁻¹, coverage 0.50, overlap after the patch 1.00, flags overlap
- B_4ff67f9ea2 b3lyp mode 0: label 32.99 → 32.56 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_4ff67f9ea2 wb97x mode 0: label 57.64 → 58.51 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_55cca3aaf2 b3lyp mode 0: label 23.83 → 22.27 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
- B_55cca3aaf2 wb97x mode 0: label 54.42 → 56.34 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags step
