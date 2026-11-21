# The low-mode repair's change of a label mode, against frequency and force constant (TASKS 218)

**Exploratory read; it decides nothing.** A demonstration of the extrapolated read on the seven molecules that had both steps on 20 November, run before the step-0.02 data of the other 13 were read; it states no outcome.

**Extrapolated to step zero (amendment 3 of the registration).** 16 points (re-measured label mode × functional) on 7 molecules, each measured at a step and at 2 times it. Per direction the two steps' columns are combined as 1.3333·C(small) -0.3333·C(large), which cancels the part of the finite-difference error that grows as the square of the step, and the patched Hessian is rebuilt from those columns. 'Patched' and Δ below are the extrapolated values. 1 points are flagged for a coverage or overlap below 0.9 (at step zero or at either step) and 0 as 'step bias too large for the line', their two steps standing more than 1.0 cm⁻¹ apart; 4 are flagged 'directions differ': their molecule's two steps were measured along rotated directions of the same space, so they have no extrapolated value (their noise is the small step's). Flagged points are in points.csv and in no statistic. A molecule is 'biased' when a label mode of it lies below 20 cm⁻¹. 0 point(s) turned imaginary under the patch. 'Noise' is the frequency noise the extrapolated value carries per 1e-07 hartree/bohr of gradient noise: the small step's (`noise_sensitivity_cm`) times 1.344; the gradient noise itself is not measured here.

**No record of the q² test was given**, so this read states no outcome.

**13 molecule(s) have no second step of this measurement** and no point here: A2_05e08111d2 (no second step), A2_3ac24b6972 (no second step), B_0d1c7f83df (no second step), B_1139ae8d01 (no second step), B_14cf57747b (no second step), B_15207e9ed5 (no second step), B_16769b963f (no second step), B_19c3319693 (no second step), B_1b434d2cd0 (no second step), B_2326ac497c (no second step), B_477b567fed (no second step), B_4f6ebdb30b (no second step), B_863cdaad7a (no second step).

## Every point: extrapolated, at the small step, and the step bias removed

| point | label (cm⁻¹) | extrapolated | Δ extrapolated | Δ at the small step | step bias removed | large − small step | noise per 1e-07 hartree/bohr | flags |
|---|---|---|---|---|---|---|---|---|
| B_3dcbd985e3 b3lyp mode 0 | 23.71 | none | none | +0.08 | none | +0.44 | 0.24 | directions differ |
| B_0c6c144a7f b3lyp mode 0 | 23.73 | 23.34 | -0.38 | -0.19 | 0.19 | +0.57 | 1.46 |  |
| B_55cca3aaf2 b3lyp mode 0 | 23.83 | 22.10 | -1.73 | -1.56 | 0.17 | +0.49 | 1.39 |  |
| B_3dcbd985e3 b3lyp mode 1 | 30.28 | none | none | -0.35 | none | +0.27 | 0.71 | directions differ |
| B_4ff67f9ea2 b3lyp mode 0 | 32.99 | 32.46 | -0.53 | -0.43 | 0.10 | +0.30 | 0.98 |  |
| B_1726105aae b3lyp mode 0 | 34.30 | 34.56 | +0.26 | +0.40 | 0.14 | +0.42 | 0.18 |  |
| B_0af11315e3 b3lyp mode 0 | 45.74 | 44.29 | -1.45 | -1.37 | 0.08 | +0.23 | 0.15 |  |
| B_1428bc8164 b3lyp mode 0 | 50.50 | 50.56 | +0.06 | +0.15 | 0.10 | +0.29 | 0.09 |  |
| B_55cca3aaf2 wb97x mode 0 | 54.42 | 56.25 | +1.83 | +1.92 | 0.08 | +0.25 | 0.68 |  |
| B_4ff67f9ea2 wb97x mode 0 | 57.64 | 58.43 | +0.79 | +0.87 | 0.08 | +0.24 | 0.66 |  |
| B_3dcbd985e3 wb97x mode 0 | 63.39 | none | none | -0.43 | none | +0.14 | 0.40 | directions differ |
| B_0c6c144a7f wb97x mode 0 | 67.12 | 60.09 | -7.03 | -6.95 | 0.09 | +0.26 | 0.58 |  |
| B_3dcbd985e3 wb97x mode 1 | 77.84 | none | none | -0.70 | none | +0.12 | 0.07 | directions differ |
| B_0af11315e3 wb97x mode 0 | 84.64 | 83.23 | -1.41 | -1.37 | 0.04 | +0.12 | 0.08 |  |
| B_1726105aae wb97x mode 0 | 111.71 | 111.32 | -0.39 | -0.35 | 0.04 | +0.13 | 0.06 |  |
| B_1428bc8164 wb97x mode 2 | 119.99 | 119.95 | -0.05 | -0.01 | 0.04 | +0.11 | 0.05 | overlap |

## b3lyp, unbiased sample: 6 unflagged points in 20–100 cm⁻¹

| label frequency (cm⁻¹) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| 20–30 | 2 | 1.06 | 1.73 | 1 | 0.50 | 0.35 | 1.43 |
| 30–40 | 2 | 0.40 | 0.53 | 1 | 0.50 | 0.35 | 0.58 |
| 40–50 | 1 | 1.45 | 1.45 | 1 | 1.00 | 0.00 | 0.15 |
| 50–60 | 1 | 0.06 | 0.06 | 0 | 0.00 | 0.00 | 0.09 |
| 60–80 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 80–100 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |

| force constant quartile (hartree/bohr²) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| Q1: 5.35e-05 to 5.74e-05 | 2 | 1.06 | 1.73 | 1 | 0.50 | 0.35 | 1.43 |
| Q2: 1.13e-04 to 5.53e-04 | 2 | 0.40 | 0.53 | 1 | 0.50 | 0.35 | 0.58 |
| Q3: 7.63e-04 to 7.63e-04 | 1 | 1.45 | 1.45 | 1 | 1.00 | 0.00 | 0.15 |
| Q4: 1.33e-03 to 1.33e-03 | 1 | 0.06 | 0.06 | 0 | 0.00 | 0.00 | 0.09 |

Spearman of abs Δ against the label frequency: -0.43 (n = 6); against log k: -0.43 (n = 6). Frequency against log k on the same points: +1.00; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none. Rms of the signed change: 0.96 cm⁻¹.

The rule's arithmetic on this group's points in 20–60 cm⁻¹ (the registered population; its outcome is in the section below): n = 6, 3 moved more than 0.5 cm⁻¹: fewer than the 16 points the rule needs, so it reads nothing from them. Outcome 3: undecided.

## wb97x, unbiased sample: 4 unflagged points in 20–100 cm⁻¹

| label frequency (cm⁻¹) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| 20–30 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 30–40 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 40–50 | 0 | undefined | undefined | 0 | undefined | undefined | undefined |
| 50–60 | 2 | 1.31 | 1.83 | 2 | 1.00 | 0.00 | 0.67 |
| 60–80 | 1 | 7.03 | 7.03 | 1 | 1.00 | 0.00 | 0.58 |
| 80–100 | 1 | 1.41 | 1.41 | 1 | 1.00 | 0.00 | 0.08 |

| force constant quartile (hartree/bohr²) | n | median abs Δ (cm⁻¹) | max abs Δ | > 0.5 | fraction | 1 SE | median noise per 1e-07 |
|---|---|---|---|---|---|---|---|
| Q1: 2.73e-04 to 2.73e-04 | 1 | 1.83 | 1.83 | 1 | 1.00 | 0.00 | 0.68 |
| Q2: 2.99e-04 to 2.99e-04 | 1 | 0.79 | 0.79 | 1 | 1.00 | 0.00 | 0.66 |
| Q3: 3.84e-04 to 3.84e-04 | 1 | 7.03 | 7.03 | 1 | 1.00 | 0.00 | 0.58 |
| Q4: 2.61e-03 to 2.61e-03 | 1 | 1.41 | 1.41 | 1 | 1.00 | 0.00 | 0.08 |

Spearman of abs Δ against the label frequency: +0.00 (n = 4); against log k: +0.00 (n = 4). Frequency against log k on the same points: +1.00; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none. Rms of the signed change: 3.72 cm⁻¹.

The rule's arithmetic on this group's points in 20–60 cm⁻¹ (description only): n = 2, 2 moved more than 0.5 cm⁻¹: fewer than the 16 points the rule needs, so it reads nothing from them. Outcome 3: undecided.

## The registered decision rule

Population: b3lyp, unbiased sample, label frequency 20–60 cm⁻¹, unflagged. No outcome is stated: 13 molecule(s) have no second step of this measurement (A2_05e08111d2: no second step; A2_3ac24b6972: no second step; B_0d1c7f83df: no second step; B_1139ae8d01: no second step; B_14cf57747b: no second step; B_15207e9ed5: no second step; B_16769b963f: no second step; B_19c3319693: no second step; B_1b434d2cd0: no second step; B_2326ac497c: no second step; B_477b567fed: no second step; B_4f6ebdb30b: no second step; B_863cdaad7a: no second step). That is a missing measurement; the rule is read when every molecule has both steps.

Flagged points in the window: 2. Counted as moved: 5 of 8, outcome undecided; counted as unmoved: 3 of 8, outcome undecided. The registered fraction stays the one on unflagged points.

Moved per band of the molecule's lowest mode: 20–30: 1 of 2; 30–40: 1 of 2; 40–50: 1 of 1; 50–60: 0 of 1. Weighted by the bands' eligible molecules (41/41/54/146): 0.34 (descriptive; the rule reads the unweighted fraction).

What orders the moves (descriptive): Spearman of abs Δ against the label frequency: -0.43 (n = 6); against log k: -0.43 (n = 6). Frequency against log k on the same points: +1.00; as far as these two are one ordering the points cannot tell a frequency trigger from a force-constant trigger, and the read names none.

| registered point | label (cm⁻¹) | extrapolated | Δ extrapolated | Δ at the small step | step bias removed | large − small step | noise per 1e-07 hartree/bohr | flags |
|---|---|---|---|---|---|---|---|---|
| B_0af11315e3 mode 0 | 45.74 | 44.29 | -1.45 | -1.37 | 0.08 | +0.23 | 0.15 |  |
| B_0c6c144a7f mode 0 | 23.73 | 23.34 | -0.38 | -0.19 | 0.19 | +0.57 | 1.46 |  |
| B_1428bc8164 mode 0 | 50.50 | 50.56 | +0.06 | +0.15 | 0.10 | +0.29 | 0.09 |  |
| B_1726105aae mode 0 | 34.30 | 34.56 | +0.26 | +0.40 | 0.14 | +0.42 | 0.18 |  |
| B_3dcbd985e3 mode 0 | 23.71 | none | none | +0.08 | none | +0.44 | 0.24 | directions differ |
| B_3dcbd985e3 mode 1 | 30.28 | none | none | -0.35 | none | +0.27 | 0.71 | directions differ |
| B_4ff67f9ea2 mode 0 | 32.99 | 32.46 | -0.53 | -0.43 | 0.10 | +0.30 | 0.98 |  |
| B_55cca3aaf2 mode 0 | 23.83 | 22.10 | -1.73 | -1.56 | 0.17 | +0.49 | 1.39 |  |

## Flagged points

- B_1428bc8164 wb97x mode 2: label 119.99 → 119.95 cm⁻¹, coverage 0.68, overlap after the patch 1.00, flags overlap
- B_3dcbd985e3 b3lyp mode 0: label 23.71 → 23.79 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags directions differ
- B_3dcbd985e3 b3lyp mode 1: label 30.28 → 29.93 cm⁻¹, coverage 1.00, overlap after the patch 1.00, flags directions differ
- B_3dcbd985e3 wb97x mode 0: label 63.39 → 62.96 cm⁻¹, coverage 1.00, overlap after the patch 0.99, flags directions differ
- B_3dcbd985e3 wb97x mode 1: label 77.84 → 77.14 cm⁻¹, coverage 0.95, overlap after the patch 1.00, flags directions differ
