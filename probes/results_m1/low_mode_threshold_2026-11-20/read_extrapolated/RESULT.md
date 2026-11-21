# The low-mode repair's change of a label mode, against frequency and force constant (TASKS 218)

**Extrapolated to step zero (amendment 3 of the registration).** 42 points (re-measured label mode × functional) on 20 molecules, each measured at a step and at 2 times it. Per direction the two steps' columns are combined as 1.3333·C(small) -0.3333·C(large), which cancels the part of the finite-difference error that grows as the square of the step, and the patched Hessian is rebuilt from those columns. 'Patched' and Δ below are the extrapolated values. 4 points are flagged for a coverage or overlap below 0.9 (at step zero or at either step) and 0 as 'step bias too large for the line', their two steps standing more than 1.0 cm⁻¹ apart; 4 are flagged 'directions differ': their molecule's two steps were measured along rotated directions of the same space, so they have no extrapolated value (their noise is the small step's). Flagged points are in points.csv and in no statistic. A molecule is 'biased' when a label mode of it lies below 20 cm⁻¹. 0 point(s) turned imaginary under the patch. 'Noise' is the frequency noise the extrapolated value carries per 1e-07 hartree/bohr of gradient noise: the small step's (`noise_sensitivity_cm`) times 1.344; the gradient noise itself is not measured here.

On a third step the q² test holds (`probes/results_m1/low_mode_threshold_2026-11-20/q2_test/q2_test.json`): R = B_1428bc8164 b3lyp 4.99, B_1428bc8164 wb97x 5.00, B_1726105aae b3lyp 4.99, B_1726105aae wb97x 5.00; the law is taken to hold when every R lies in 4–6.

## Every point: extrapolated, at the small step, and the step bias removed

| point | label (cm⁻¹) | extrapolated | Δ extrapolated | Δ at the small step | step bias removed | large − small step | noise per 1e-07 hartree/bohr | flags |
|---|---|---|---|---|---|---|---|---|
| A2_3ac24b6972 b3lyp mode 0 | 20.21 | 24.63 | +4.42 | +4.63 | 0.21 | +0.61 | 0.31 |  |
| B_2326ac497c b3lyp mode 0 | 21.22 | 18.25 | -2.98 | -2.76 | 0.22 | +0.64 | 0.32 |  |
| B_3dcbd985e3 b3lyp mode 0 | 23.71 | none | none | +0.08 | none | +0.44 | 0.24 | directions differ |
| B_0c6c144a7f b3lyp mode 0 | 23.73 | 23.34 | -0.38 | -0.19 | 0.19 | +0.57 | 1.46 |  |
| B_55cca3aaf2 b3lyp mode 0 | 23.83 | 22.10 | -1.73 | -1.56 | 0.17 | +0.49 | 1.39 |  |
| B_3dcbd985e3 b3lyp mode 1 | 30.28 | none | none | -0.35 | none | +0.27 | 0.71 | directions differ |
| B_4f6ebdb30b b3lyp mode 0 | 31.00 | 32.07 | +1.07 | +1.08 | 0.01 | +0.02 | 0.31 |  |
| B_4ff67f9ea2 b3lyp mode 0 | 32.99 | 32.46 | -0.53 | -0.43 | 0.10 | +0.30 | 0.98 |  |
| B_19c3319693 b3lyp mode 0 | 33.08 | 30.66 | -2.42 | -2.28 | 0.14 | +0.41 | 0.20 |  |
| B_1726105aae b3lyp mode 0 | 34.30 | 34.56 | +0.26 | +0.40 | 0.14 | +0.42 | 0.18 |  |
| B_15207e9ed5 b3lyp mode 0 | 35.22 | 35.98 | +0.77 | +0.85 | 0.08 | +0.23 | 0.19 |  |
| B_477b567fed b3lyp mode 0 | 40.66 | 40.56 | -0.10 | -0.04 | 0.06 | +0.17 | 0.20 |  |
| B_0af11315e3 b3lyp mode 0 | 45.74 | 44.29 | -1.45 | -1.37 | 0.08 | +0.23 | 0.15 |  |
| B_16769b963f b3lyp mode 0 | 48.06 | 49.33 | +1.27 | +1.30 | 0.04 | +0.11 | 0.10 |  |
| B_1b434d2cd0 b3lyp mode 0 | 48.07 | 47.44 | -0.63 | -0.60 | 0.03 | +0.10 | 0.10 |  |
| B_1139ae8d01 b3lyp mode 0 | 48.44 | 49.91 | +1.47 | +1.53 | 0.06 | +0.18 | 0.16 |  |
| B_1428bc8164 b3lyp mode 0 | 50.50 | 50.56 | +0.06 | +0.15 | 0.10 | +0.29 | 0.09 |  |
| B_0d1c7f83df b3lyp mode 0 | 53.07 | 52.93 | -0.14 | -0.12 | 0.02 | +0.07 | 0.28 |  |
| B_14cf57747b b3lyp mode 0 | 53.20 | 54.59 | +1.39 | +1.43 | 0.04 | +0.13 | 0.08 |  |
| B_863cdaad7a b3lyp mode 0 | 53.76 | 53.73 | -0.03 | +0.02 | 0.05 | +0.15 | 0.38 |  |
| A2_05e08111d2 b3lyp mode 0 | 55.45 | 57.01 | +1.56 | +1.58 | 0.01 | +0.04 | 0.12 |  |
| B_4f6ebdb30b wb97x mode 0 | 54.24 | 52.92 | -1.32 | -1.31 | 0.00 | +0.01 | 0.18 |  |
| B_55cca3aaf2 wb97x mode 0 | 54.42 | 56.25 | +1.83 | +1.92 | 0.08 | +0.25 | 0.68 |  |
| B_4ff67f9ea2 wb97x mode 0 | 57.64 | 58.43 | +0.79 | +0.87 | 0.08 | +0.24 | 0.66 |  |
| B_3dcbd985e3 wb97x mode 0 | 63.39 | none | none | -0.43 | none | +0.14 | 0.40 | directions differ |
| B_0c6c144a7f wb97x mode 0 | 67.12 | 60.09 | -7.03 | -6.95 | 0.09 | +0.26 | 0.58 |  |
| B_477b567fed wb97x mode 0 | 70.73 | 72.95 | +2.22 | +2.22 | 0.01 | +0.02 | 0.19 | overlap |
| B_1b434d2cd0 wb97x mode 0 | 71.34 | 70.93 | -0.40 | -0.37 | 0.03 | +0.10 | 0.07 |  |
| B_16769b963f wb97x mode 0 | 71.36 | 72.74 | +1.38 | +1.41 | 0.03 | +0.10 | 0.06 |  |
| A2_05e08111d2 wb97x mode 0 | 71.98 | 72.80 | +0.82 | +0.83 | 0.01 | +0.02 | 0.11 |  |
| B_14cf57747b wb97x mode 0 | 77.13 | 78.09 | +0.96 | +0.98 | 0.02 | +0.06 | 0.05 |  |
| B_863cdaad7a wb97x mode 0 | 77.48 | 78.00 | +0.52 | +0.55 | 0.03 | +0.09 | 0.25 |  |
| B_3dcbd985e3 wb97x mode 1 | 77.84 | none | none | -0.70 | none | +0.12 | 0.07 | directions differ |
| B_15207e9ed5 wb97x mode 0 | 78.76 | 79.82 | +1.05 | +1.10 | 0.05 | +0.14 | 0.09 |  |
| B_2326ac497c wb97x mode 0 | 79.00 | 78.97 | -0.03 | +0.01 | 0.04 | +0.13 | 0.09 |  |
| B_19c3319693 wb97x mode 0 | 80.33 | 79.59 | -0.74 | -0.68 | 0.05 | +0.16 | 0.08 |  |
| B_0d1c7f83df wb97x mode 0 | 82.13 | 81.51 | -0.62 | -0.61 | 0.01 | +0.03 | 0.16 |  |
| B_0af11315e3 wb97x mode 0 | 84.64 | 83.23 | -1.41 | -1.37 | 0.04 | +0.12 | 0.08 |  |
| B_1726105aae wb97x mode 0 | 111.71 | 111.32 | -0.39 | -0.35 | 0.04 | +0.13 | 0.06 |  |
| A2_3ac24b6972 wb97x mode 1 | 116.00 | 116.53 | +0.54 | +0.57 | 0.04 | +0.12 | 0.06 | overlap |
| B_1428bc8164 wb97x mode 2 | 119.99 | 119.95 | -0.05 | -0.01 | 0.04 | +0.11 | 0.05 | overlap |
| B_1139ae8d01 wb97x mode 2 | 121.69 | 122.19 | +0.49 | +0.52 | 0.03 | +0.08 | 0.05 | overlap |

## b3lyp, unbiased sample: 19 unflagged points in 20–100 cm⁻¹

| label frequency (cm⁻¹) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| 20–30 | 4 | 2.35 | 4.42 | 3 | 0.75 | 0.22 | 0.86 |
| 30–40 | 5 | 0.77 | 2.42 | 4 | 0.80 | 0.18 | 0.20 |
| 40–50 | 5 | 1.27 | 1.47 | 4 | 0.80 | 0.18 | 0.15 |
| 50–60 | 5 | 0.14 | 1.56 | 2 | 0.40 | 0.22 | 0.12 |
| 60–80 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 80–100 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |

| force constant quartile (hartree/bohr²) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| Q1: 5.35e-05 to 2.00e-04 | 5 | 1.07 | 2.98 | 4 | 0.80 | 0.18 | 0.98 |
| Q2: 2.18e-04 to 4.26e-04 | 5 | 0.77 | 4.42 | 3 | 0.60 | 0.22 | 0.20 |
| Q3: 5.53e-04 to 9.07e-04 | 5 | 0.63 | 1.47 | 3 | 0.60 | 0.22 | 0.16 |
| Q4: 9.21e-04 to 1.64e-03 | 4 | 1.33 | 1.56 | 3 | 0.75 | 0.22 | 0.09 |

Spearman of abs Δ against the label frequency: -0.39 (n = 19); against log k: -0.07 (n = 19). Frequency against log k on the same points: +0.78; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none. Rms of the signed change: 1.62 cm⁻¹.

The rule's arithmetic on this group's points in 20–60 cm⁻¹ (the registered population; its outcome is in the section below): n = 19, 13 moved more than 0.5 cm⁻¹: p = 0.68, 1 SE = 0.11. p ≥ 0.50 and p − 1 SE = 0.58 ≥ 0.40. Outcome 2, for this group's molecules: a majority of the labels of their modes in this window stand more than 0.5 cm⁻¹ from the patched value. That says label and patch disagree, not why: the missing grid-weight derivative is one cause, the labels' older CPHF another, and the finite difference corrects both.

## wb97x, unbiased sample: 14 unflagged points in 20–100 cm⁻¹

| label frequency (cm⁻¹) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| 20–30 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 30–40 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 40–50 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 50–60 | 3 | 1.32 | 1.83 | 3 | 1.00 | 0.00 | 0.66 |
| 60–80 | 8 | 0.89 | 7.03 | 6 | 0.75 | 0.15 | 0.09 |
| 80–100 | 3 | 0.74 | 1.41 | 3 | 1.00 | 0.00 | 0.08 |

| force constant quartile (hartree/bohr²) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| Q1: 2.73e-04 to 6.08e-04 | 4 | 1.58 | 7.03 | 4 | 1.00 | 0.00 | 0.62 |
| Q2: 7.18e-04 to 1.99e-03 | 4 | 0.57 | 0.82 | 3 | 0.75 | 0.22 | 0.13 |
| Q3: 2.04e-03 to 2.47e-03 | 3 | 1.05 | 1.38 | 3 | 1.00 | 0.00 | 0.08 |
| Q4: 2.57e-03 to 3.44e-03 | 3 | 0.96 | 1.41 | 2 | 0.67 | 0.27 | 0.08 |

Spearman of abs Δ against the label frequency: -0.35 (n = 14); against log k: -0.23 (n = 14). Frequency against log k on the same points: +0.71; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none. Rms of the signed change: 2.12 cm⁻¹.

The rule's arithmetic on this group's points in 20–60 cm⁻¹ (description only): n = 3, 3 moved more than 0.5 cm⁻¹: fewer than the 16 points the rule needs, so it reads nothing from them. Outcome 3: undecided.

## The registered decision rule

Population: b3lyp, unbiased sample, label frequency 20–60 cm⁻¹, unflagged. n = 19, 13 moved more than 0.5 cm⁻¹: p = 0.68, 1 SE = 0.11. p ≥ 0.50 and p − 1 SE = 0.58 ≥ 0.40. Outcome 2, for molecules whose lowest b3lyp mode lies in 20–60 cm⁻¹, with at most 25 atoms, each band weighted equally: a majority of the labels of their modes in this window stand more than 0.5 cm⁻¹ from the patched value. That says label and patch disagree, not why: the missing grid-weight derivative is one cause, the labels' older CPHF another, and the finite difference corrects both.

Flagged points in the window: 2. Counted as moved: 15 of 21, outcome majority wrong; counted as unmoved: 13 of 21, outcome majority wrong. The registered fraction stays the one on unflagged points.

Moved per band of the molecule's lowest mode: 20–30: 3 of 4; 30–40: 4 of 5; 40–50: 4 of 5; 50–60: 2 of 5. Weighted by the bands' eligible molecules (41/41/54/146): 0.59 (descriptive; the rule reads the unweighted fraction).

What orders the moves (descriptive): Spearman of abs Δ against the label frequency: -0.39 (n = 19); against log k: -0.07 (n = 19). Frequency against log k on the same points: +0.78; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none.

| registered point | label (cm⁻¹) | extrapolated | Δ extrapolated | Δ at the small step | step bias removed | large − small step | noise per 1e-07 hartree/bohr | flags |
|---|---|---|---|---|---|---|---|---|
| A2_05e08111d2 mode 0 | 55.45 | 57.01 | +1.56 | +1.58 | 0.01 | +0.04 | 0.12 |  |
| A2_3ac24b6972 mode 0 | 20.21 | 24.63 | +4.42 | +4.63 | 0.21 | +0.61 | 0.31 |  |
| B_0af11315e3 mode 0 | 45.74 | 44.29 | -1.45 | -1.37 | 0.08 | +0.23 | 0.15 |  |
| B_0c6c144a7f mode 0 | 23.73 | 23.34 | -0.38 | -0.19 | 0.19 | +0.57 | 1.46 |  |
| B_0d1c7f83df mode 0 | 53.07 | 52.93 | -0.14 | -0.12 | 0.02 | +0.07 | 0.28 |  |
| B_1139ae8d01 mode 0 | 48.44 | 49.91 | +1.47 | +1.53 | 0.06 | +0.18 | 0.16 |  |
| B_1428bc8164 mode 0 | 50.50 | 50.56 | +0.06 | +0.15 | 0.10 | +0.29 | 0.09 |  |
| B_14cf57747b mode 0 | 53.20 | 54.59 | +1.39 | +1.43 | 0.04 | +0.13 | 0.08 |  |
| B_15207e9ed5 mode 0 | 35.22 | 35.98 | +0.77 | +0.85 | 0.08 | +0.23 | 0.19 |  |
| B_16769b963f mode 0 | 48.06 | 49.33 | +1.27 | +1.30 | 0.04 | +0.11 | 0.10 |  |
| B_1726105aae mode 0 | 34.30 | 34.56 | +0.26 | +0.40 | 0.14 | +0.42 | 0.18 |  |
| B_19c3319693 mode 0 | 33.08 | 30.66 | -2.42 | -2.28 | 0.14 | +0.41 | 0.20 |  |
| B_1b434d2cd0 mode 0 | 48.07 | 47.44 | -0.63 | -0.60 | 0.03 | +0.10 | 0.10 |  |
| B_2326ac497c mode 0 | 21.22 | 18.25 | -2.98 | -2.76 | 0.22 | +0.64 | 0.32 |  |
| B_3dcbd985e3 mode 0 | 23.71 | none | none | +0.08 | none | +0.44 | 0.24 | directions differ |
| B_3dcbd985e3 mode 1 | 30.28 | none | none | -0.35 | none | +0.27 | 0.71 | directions differ |
| B_477b567fed mode 0 | 40.66 | 40.56 | -0.10 | -0.04 | 0.06 | +0.17 | 0.20 |  |
| B_4f6ebdb30b mode 0 | 31.00 | 32.07 | +1.07 | +1.08 | 0.01 | +0.02 | 0.31 |  |
| B_4ff67f9ea2 mode 0 | 32.99 | 32.46 | -0.53 | -0.43 | 0.10 | +0.30 | 0.98 |  |
| B_55cca3aaf2 mode 0 | 23.83 | 22.10 | -1.73 | -1.56 | 0.17 | +0.49 | 1.39 |  |
| B_863cdaad7a mode 0 | 53.76 | 53.73 | -0.03 | +0.02 | 0.05 | +0.15 | 0.38 |  |

## Flagged points

- A2_3ac24b6972 wb97x mode 1: label 116.00 → 116.53 cm⁻¹, coverage 0.85, overlap after the patch 1.00, flags overlap
- B_1139ae8d01 wb97x mode 2: label 121.69 → 122.19 cm⁻¹, coverage 0.64, overlap after the patch 1.00, flags overlap
- B_1428bc8164 wb97x mode 2: label 119.99 → 119.95 cm⁻¹, coverage 0.68, overlap after the patch 1.00, flags overlap
- B_3dcbd985e3 b3lyp mode 0: label 23.71 → 23.79 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags directions differ
- B_3dcbd985e3 b3lyp mode 1: label 30.28 → 29.93 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags directions differ
- B_3dcbd985e3 wb97x mode 0: label 63.39 → 62.96 cm⁻¹, coverage 1.00, overlap after the patch 0.99, flags directions differ
- B_3dcbd985e3 wb97x mode 1: label 77.84 → 77.14 cm⁻¹, coverage 0.95, overlap after the patch 1.00, flags directions differ
- B_477b567fed wb97x mode 0: label 70.73 → 72.95 cm⁻¹, coverage 0.50, overlap after the patch 1.00, flags overlap
