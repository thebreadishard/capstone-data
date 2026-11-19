---
license: cc-by-4.0
library_name: aromir
tags:
  - chemistry
  - infrared-spectroscopy
  - hessian
  - equivariant
model_name: aromir ΔH network v1.3
---

# aromir ΔH network v1.3

A correction to the Hessian of an aromatic molecule. The network reads a cheap B3LYP/6-31G* Hessian and returns ΔH, the difference to ωB97X/6-31G* (the DFT proxy: the network's ΔH is trained on ωB97X − B3LYP Hessians). The corrected Hessian gives harmonic infrared band positions closer to that level at the cost of the cheap one.

- **Seeds:** 3 (0, 1, 2); the applied correction is their mean, and their spread is reported per band.
- **Licensed families:** ring-ip, CH-stretch, CH-oop, other.
- **Not licensed:** none.
- **On thin ground:** 'other' is within the licence line on hold-out (a) at 2.78 cm⁻¹, on 8 molecules: resampling those molecules puts the error between 1.68 and 3.76 cm⁻¹, and 30% of the resamples lie above the line.
- **Use it through:** [aromir](https://github.com/thebreadishard/aromir), which builds the inputs, applies the correction and writes a certificate for every band.

## How well it is known

The rms error of the corrected band positions of the seeds' mean against ωB97X/6-31G*, in cm⁻¹, on molecules the network never trained on: the error of what aromir prints. In square brackets the 95 % interval when the hold-out's molecules are resampled. The licence is read on the band error of the seeds' mean, the error of what the release delivers, as recorded to two decimals; chosen on 16 November 2026, after it and the first-order error per seed had both been measured on both hold-outs.

| family | (a), 8 molecules | (b), 39 molecules | licensed |
|---|---|---|---|
| ring-ip | 1.43 [1.13–1.70], 199 bands | 1.91 [1.84–2.00], 1164 bands | yes |
| CH-stretch | 0.95 [0.39–1.48], 73 bands | 2.19 [1.80–2.53], 401 bands | yes |
| CH-oop | 1.64 [1.19–1.97], 46 bands | 1.88 [1.56–2.16], 84 bands | yes |
| other | 2.78 [1.68–3.76], 156 bands | 2.77 [2.56–2.97], 1225 bands | yes |

- (a): eight molecules set aside on 19 September 2026, before any network was trained, and never trained on in any form (two more molecules of that set, 2-naphthoic acid and benzonitrile, are left out of this read because the network had trained on them under another identifier)
- (b): every substituted molecule of two ring scaffolds, set aside on 8 October 2026; the network trained on no molecule of either scaffold

For comparison, the first-order error of each seed alone, the number a training run reports and the one earlier versions of this card printed as the error: its mean over the seeds, each seed's value in brackets. It is not the error of what aromir prints.

| family | (a) | (b) |
|---|---|---|
| ring-ip | 1.77 (1.95, 1.68, 1.70) | 2.12 (2.25, 2.02, 2.11) |
| CH-stretch | 1.19 (0.91, 1.74, 0.91) | 2.50 (1.91, 3.51, 2.08) |
| CH-oop | 2.17 (2.46, 2.05, 1.99) | 2.73 (2.46, 2.93, 2.80) |
| other | 3.62 (4.09, 3.27, 3.51) | 3.89 (3.65, 4.51, 3.51) |

A family is licensed when the band error of the seeds' mean, as recorded to two decimals, is within 3 cm⁻¹ on every hold-out. aromir's certificate marks each band with its family, that family's error and whether the band itself is licensed, which asks more: see the limits below.

Coupled cluster: not measured for this network version.

Sources: every error in this record: `aromir evaluate` on the two hold-outs as probes/results_m1/aromir_audit_fixes_2026-11-16/holdouts_for_aromir.py of thebreadishard/udacity-capstone-plan (plan 05) writes them; counterpart for the band errors: probes/results_m1/aromir_product_error_2026-11-16/product_error.json; the hold-outs' molecules, and the first-order errors the training runs recorded themselves (within 0.08 cm⁻¹): E7_rungC_chain35_analytic_eval_frozenb_seed0.json, E7_rungC_chain35_analytic_eval_frozenb_seed1.json, E7_rungC_chain35_analytic_eval_frozenb_seed2.json, E7_rungC_chain35_analytic_a8read_seed0.json, E7_rungC_chain35_analytic_a8read_seed1.json, E7_rungC_chain35_analytic_a8read_seed2.json.

## What it was trained on

- 749 molecules, neutral and closed-shell, each with an aromatic ring.
- Elements: C, Cl, F, H, N, O, S.
- Sizes: 8 to 30 atoms.
- Held out and never trained on: 39 in (b); 8 in (a), not counting 2 the network also trained on.
- The training Hessians were used as pyscf's analytic Hessians, without the soft-mode repair; aromir gives the network a molecule's Hessian prepared the same way. It measures the soft modes in either case, to decide whether the geometry is a minimum and for the positions it prints: the correction is added to the Hessian with its soft modes measured.

## Where it stops being known

- **The level is ωB97X/6-31G*.** The errors above are against that level, not against experiment.
- **Positions are harmonic.** No anharmonic shift is applied.
- **Neutral, closed-shell, aromatic molecules only**, of the elements C, Cl, F, H, N, O, S. aromir refuses anything else before computing.
- **Sizes outside 8 to 30 atoms are extrapolation.** `aromir spectrum` refuses them unless `--outside-training-sizes` is given; its certificate then licenses none of their bands.
- **Not licensed: no family.** Bands of an unlicensed family are printed with their measured error and marked.
- **The answer depends on how the molecule's atoms are numbered**: the internal coordinates are chosen by atom number, and a dihedral near ±180° enters by its raw value. aromir orders the atoms of every input by the bond graph first, so every SMILES of a molecule gets one order; atoms the graph cannot tell apart keep the order of an xyz file, so two listings of one geometry can still differ. Do not feed the network a molecule in another order. Measured: band positions move by up to 10.73 cm⁻¹ between atom orders (3 molecules, 5 orders each; order_spread_smiles.json).
- **A rigid rotation of the molecule** moved band positions by up to 5.34 cm⁻¹ on 3 molecule(s) with a linear group and 0.00 cm⁻¹ on 4 molecule(s) without a linear group (8 trial(s) per molecule). These are the largest seen, not bounds.
- **The molecule's mirror image** moved band positions by up to 5.22 cm⁻¹ on 3 molecule(s) with a linear group and 2.60 cm⁻¹ on 4 molecule(s) without a linear group (1 trial(s) per molecule). These are the largest seen, not bounds.
- **Another listing of the same atoms in an xyz file** moved band positions by up to 5.27 cm⁻¹ on 3 molecule(s) with a linear group and 3.07 cm⁻¹ on 4 molecule(s) without a linear group (12 trial(s) per molecule). These are the largest seen, not bounds.
  A linear angle (in a nitrile, an alkyne) is measured against a fixed axis in space, and a dihedral enters with its sign; the hold-out errors hold none of this. Source: probes/results_m1/aromir_audit_fixes_2026-11-16/rerun/e3_invariance.log of thebreadishard/udacity-capstone-plan (plan 05), aromir at 8a0afa7: benzonitrile, phenylacetylene and diphenylacetylene with a linear group; benzene, biphenyl, 2-methylnaphthalene and phenol without; stored B3LYP geometries and Hessians.
- **Band heights are the cheap level's.** The dipole derivatives are not corrected.
- **A family is a rule, not a kind of bond.** ring-ip: between 950 and 1750 cm⁻¹ and in the molecular plane: ring stretches and in-plane bends, and with them every other mode there, such as a C=O stretch or a CH₃ deformation; in a non-planar molecule every mode in that window. CH-stretch: above 2800 cm⁻¹ with most of its motion on hydrogens: the C–H stretches, and by the same rule an O–H or N–H stretch. CH-oop: between 600 and 1050 cm⁻¹, out of the molecular plane and on hydrogens; a non-planar molecule has none, and its C–H wags fall under other or ring-ip. other: every mode the three rules above do not take. aromir's certificate licenses a band only when its family is within the licence line, the molecule lies inside the training sizes, its low-level mode is real, the band is real for the seeds' mean and for every seed, and a CH-stretch or CH-oop band moves carbon-bound hydrogens. A ring-ip band is licensed as the rule takes it, C=O stretches included.

## What it is

An equivariant message-passing encoder (PaiNN type) over the atoms, and a head that predicts one number per pair of internal coordinates: an entry of ΔF. The Cartesian correction is ΔH = Bᵀ ΔF B with B the Wilson matrix, so it is symmetric and free of translations. It is free of rotations and turns with the molecule only where no linear angle is among the internal coordinates: see the limits above.

- Encoder: 3 blocks, 64 scalar and 64 vector channels, sum pooling.
- Head: hidden width 256, with the pair features, a learned share of the low level's own force constant.
- Pair pattern f; primitives by the geometric angle choice, dihedrals raw.
- 292,546 parameters per seed.

## Files

| file | seed | sha256 |
|---|---|---|
| seed-0.safetensors | 0 | `bc1bbd91fc80068ac4fa16b6aeb9fcaa34429ca2f09a5c0284c924bfb3907094` |
| seed-1.safetensors | 1 | `96a15a89b6ac129c527fa643de07f51c7bf075b8de05a7898b9b9382dba2958e` |
| seed-2.safetensors | 2 | `4a3fda6248785ee6dc198095342ebb19cc66bb47c40823834c9ba9f4ff6a91d8` |

Each `seed-<n>.json` beside its tensors holds the recipe and that sha256; `evaluation.json` and `training.json` hold the records this card is written from.

## Use

```console
$ pip install git+https://github.com/thebreadishard/aromir
$ aromir spectrum "c1ccc2ccccc2c1" --out results/naphthalene
```

aromir uses the release inside the package; `--release <folder>` names another, such as a copy of this one.

## Licence

Weights and records: CC BY 4.0. Code: MIT, at https://github.com/thebreadishard/aromir.

This card was written by `aromir card` from release v1.3's own files.
