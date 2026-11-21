# Coverable out-of-plane screen on GFN2-xTB: stopped at its positive control (TASKS 210, 20 November 2026)

No candidate force field was computed. The check that had to come first, whether GFN2-xTB shows the effect on the one molecule
known to have it, failed, so no xtb field could select anything and the night's runs were not launched (the coordinator's
decision, 20 Nov, after hand-back 1). Paths are relative to `plans/05_delta-probed-ir-pipeline`.

## The question

TASKS 210 needs training molecules with a coverable strained out-of-plane mode: a mode below 2,000 cm⁻¹ with strain
|ν − ω| / ω of at least 0.08 that is strained by its own quartic constant, so that a block of the mode and its strongest partner
leaves at most 0.10 × ω outside (`probes/anharmonic_coverage_screen.py`; `src/dpir/vpt2_domain.py`, `STRAIN_MAX`). The row's plan
was to pre-screen compact PAHs on GFN2-xTB quartic force fields before paying for a DFT label.

## The control

Coronene is the only molecule known to have such modes. Its two force fields, read by the same screen on 13 November
(`probes/results_m1/coverage_screen_2026-11-13/targets/coverage_screen.json`):

| coronene | B3LYP/6-31G* (G) | GFN2-xTB (X) |
|---|---|---|
| mode 36 | 807.1 cm⁻¹, strain 0.222, φ_iiii/8 +88.9, coverable | — |
| mode 24 | 642.9 cm⁻¹, strain 0.103, φ_iiii/8 +16.2, coverable | — |
| largest strain below 2,000 cm⁻¹ | 0.222 (mode 36) | 0.021 (mode 3, 143.2 cm⁻¹) |
| largest φ_iiii/8, 300–2,000 cm⁻¹ | +88.9 (mode 36) | +13.1 (mode 37, 813.7 cm⁻¹, shift −12.4) |

Tetracene, which has no such mode, reads a larger xtb quartic constant than coronene: +24.5 (mode 30, 860.3 cm⁻¹) on X, +18.6 on
G. So at xtb neither the strain nor the size of the quartic constant separates the molecule with the effect from one without.

The read registered for the candidates, run on the stored X fields of coronene and tetracene in the candidates' layout
(`controls/sets.json`, the screen unchanged, `--strain-min 0.08`): **186 modes in 2 force fields, 0 reach a strain of 0.08**
(`controls/read/coverage_screen.md`). B3LYP's constant is not in doubt: φ_iiii of mode 36 is 711 cm⁻¹ from the force field and
697 from energies along the mode, mode 24 130 and 130 (obstacle ledger, 13 Nov 15:3x).

## A correction to TASKS 210

The row says GFN2-xTB found the same two molecules broken as B3LYP did. That holds for B_78f8233b4c and B_410ac0fb2f, both
substituted, whose strain is a near-cancellation against an X–H stretch and is not coverable (both sides of each are in
`coverage_screen_2026-11-13/coverage_screen.md`). It does not hold for the coverable kind: the ledger of 16 Nov 13:5x records
that the xtb mark catches 2 of 6 G marks, and coronene's two modes are among the four it misses. For ordinary out-of-plane modes
the levels agree (pyrene's largest φ_iiii/8 +22.8 on G and +23.4 on X, `coverage_screen_2026-11-13/coverage_screen.json`).

## Consequence

An xtb null clears nothing, because coronene itself reads null. A positive would still select, but no molecule is known to give
one. GFN2-xTB therefore cannot serve as this pre-screen, and further xtb fields would only slow the training search.

## The route that would do the job (not run)

The strain is the mode's own quartic constant, which `probes/mode_quartic_scan.py` measures from B3LYP single-point energies
along a chosen mode, with no force field. Its check on coronene is the one above (697 and 130 against the field's 711 and 130 cm⁻¹,
after removing the stencil's step error). The corpus already holds B3LYP modes for four compact PAHs without a quartic field:
benzo[ghi]perylene (D_210c3076e6, 34 atoms), peropyrene (T_2f846bd4a9, 40), ovalene (T_c874e3c6cf, 46) and
hexa-peri-hexabenzocoronene (T_76dfc434db, 60) (`modules/05_support_predictor/corpus/manifest.csv`).

Cost order, from coronene's scan on the laptop (run spec `probes/runspecs/mode_quartic_coronene.json`, 8 threads): 18 SCFs, wall
times 236 to 624 s, median 353 s (`probes/results_m1/mode_quartic_coronene_2026-11-13/pyscf.log`, the 18 'CPU time for SCF'
lines); the spec of the step run records 1 h 54 min for those 18. Two modes need 9 energies at one step and 8 more for the step
extrapolation, so about 2 h per molecule of coronene's size, and more for the larger ones (SCF cost grows steeply with size;
not measured for them). Which out-of-plane modes to scan in each molecule is the open choice; coronene's two were found from its
full field.

The price of a full B3LYP quartic field, for comparison: route A forecast coronene's 205 Hessians at about 9,000 s each on
8 threads, 129 h on the four-lane CCX53 (ledger, 2 Nov 16:3x), at €0.855 an hour (`probes/price_large_labels.py`, line 16)
about €110. That is a forecast, not a measured total. Paid compute stopped on 15 November (decision 63); spending is the author's
decision.

## What is kept

- Branch `t210-screen` (commit 3a931221, worktree `../wt_t210`, not merged): `probes/coverable_oop_candidates.py` (checks eight
  candidates' SMILES by formula, ring count and rim-hydrogen pattern and writes start records; 7 tests pass;
  needs an independent review before the trunk) and the registration
  `GoalGathering/notes/PreRegistration_2026-11-20_Coverable_OOP_Screen.md`, unrun. Both are kept for the day a B3LYP scan is
  chosen.
- In this folder: start records and sets files for benzo_ghi_perylene, anthanthrene and perylene; `benzo_ghi_perylene/field/`
  holds `ids.tsv` and `selection.json` from the dry run only; `controls/` holds the control read.
- `probes/runspecs/oop_screen_benzo_ghi_perylene.json`: validated, never launched.
