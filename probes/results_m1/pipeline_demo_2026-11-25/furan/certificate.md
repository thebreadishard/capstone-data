# Certificate — furan · pipeline 0.15 · 2026-11-25 08:39

<!-- delivery 1 -->

furan: the infrared spectrum of ΔH-network v1.4 (3 seeds) — B3LYP/6-31G* corrected toward ωB97X/6-31G*. The spectrum is made by the release networks of version 1.4, trained on the 1132 labelled entries of their training pool, hold-outs (a) and (b) included: each of the 3 networks is fitted on a random 85 % of the molecules and stopped on the other 15 %, a different 15 % per seed, so not every molecule is fitted by every network (with 3 networks about 0.15³ ≈ 0.3 % by none). Its error bars were measured on the measurement networks of the same version — the same recipe trained without the hold-out molecules — on molecules those networks never saw; the release networks themselves have seen the molecules of hold-outs (a) and (b), so they have no held-out error of their own. The error stated is the measurement networks' error of the corrected band positions of the seed-mean correction; the harmonic positions ω are licensed for ring-ip, CH-stretch, CH-oop, other (decision 65) where a band's own position moved by no more than the licence line in the 11 presentations tried (this molecule turned, mirrored or listed in another atom order), each band marked; at the coupled-cluster level not measured for this network version: the coupled-cluster reads (T3) were made on an earlier network (chain 34). Each band's own spread was measured for this molecule: the networks corrected it again in 11 other presentations (8 rotations, 2 mirror images, 1 swap of equivalent atoms), and a band's spread is the furthest its position lay from the printed one in any of them: its distance from the printed presentation, not the range between presentations. The largest is 0.11 cm⁻¹, under the mirror image, and no band moved by more than the licence line. The scaled B3LYP spectrum is shown as the baseline only. This molecule and the ΔH network: not in the catalogue: the network has not seen it.

**Positions.** Positions are harmonic (ω): the anharmonic step was not applied — the step exists and was not run: it is off unless the run names a time budget, and `--anharmonic-minutes 120` switches it on.

## Molecule

- c1ccoc1, C4H4O, 9 atoms (C, H, O); the network's training set spans 8–40 atoms: inside
- catalogue: not listed
- the ΔH network: not in the catalogue: the network has not seen it
- delivery 1 — only: harmonic, the anharmonic step is switched off: 2026-11-25 08:39:14, 384.6 s after the start

## Spectrum, band by band (ΔH-network v1.4, 3 seeds)

| best estimate (cm⁻¹) | printed | harmonic ω, network | Δ_anh | ± of Δ_anh, against its VPT2 label (measured, not licensed) | height (km/mol) | seeds' range of ω | B3LYP ω | baseline ω | family | ω licensed | own spread of ω (cm⁻¹), under | error of the corrected band positions of the seed-mean correction of ω on (a) / (b), cm⁻¹ | laboratory region | u_band (cm⁻¹) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 626.8 | harmonic ω | 626.8 | — | — | 0.0 | 623.7–628.9 | 614.1 | 601.2 | other | yes | 0.07, the mirror image, rotated | 2.38 / 2.1 | low / skeletal | 16.12 |
| 637.3 | harmonic ω | 637.3 | — | — | 19.74 | 636.1–638.1 | 623.4 | 610.3 | other | yes | 0.00, the mirror image, rotated | 2.38 / 2.1 | low / skeletal | 16.12 |
| 763.4 | harmonic ω | 763.4 | — | — | 0.01 | 760.1–767.9 | 722.9 | 707.7 | CH-oop | yes | 0.02, the mirror image, rotated | 1.86 / 1.26 | CH-oop (10.5-15 um; benzene nu11 at 673 included) | 9.61 |
| 776.5 | harmonic ω | 776.5 | — | — | 78.37 | 775.9–777.3 | 758.1 | 742.2 | CH-oop | yes | 0.00, the mirror image, rotated | 1.86 / 1.26 | CH-oop (10.5-15 um; benzene nu11 at 673 included) | 9.61 |
| 868.2 | harmonic ω | 868.2 | — | — | 0.01 | 867.5–869.2 | 831.2 | 813.7 | CH-oop | yes | 0.11, the mirror image | 1.86 / 1.26 | CH-oop (10.5-15 um; benzene nu11 at 673 included) | 9.61 |
| 891.5 | harmonic ω | 891.5 | — | — | 14.72 | 891.5–891.6 | 885.8 | 867.2 | other | yes | 0.00, a swap of equivalent atoms 1 | 2.38 / 2.1 | CH-oop (10.5-15 um; benzene nu11 at 673 included) | 9.61 |
| 894.2 | harmonic ω | 894.2 | — | — | 0.37 | 893.9–894.5 | 890.9 | 872.2 | other | yes | 0.00, a swap of equivalent atoms 1 | 2.38 / 2.1 | CH-oop (10.5-15 um; benzene nu11 at 673 included) | 9.61 |
| 906.2 | harmonic ω | 906.2 | — | — | 0.0 | 905.9–906.7 | 872.7 | 854.4 | CH-oop | yes | 0.05, the mirror image | 1.86 / 1.26 | CH-oop (10.5-15 um; benzene nu11 at 673 included) | 9.61 |
| 1034.0 | harmonic ω | 1034.0 | — | — | 37.53 | 1032.4–1035.4 | 1024.0 | 1002.5 | ring-ip | yes | 0.00, the mirror image | 1.17 / 1.22 | ring / CH-ip (9-10.5 um) | 15.87 |
| 1082.9 | harmonic ω | 1082.9 | — | — | 1.7 | 1082.7–1083.1 | 1073.2 | 1050.7 | ring-ip | yes | 0.00, a swap of equivalent atoms 1 | 1.17 / 1.22 | ring / CH-ip (9-10.5 um) | 15.87 |
| 1103.6 | harmonic ω | 1103.6 | — | — | 12.42 | 1102.0–1105.4 | 1099.4 | 1076.3 | ring-ip | yes | 0.00, the mirror image, rotated | 1.17 / 1.22 | CH-ip-bend (8.6 um) | 8.64 |
| 1182.1 | harmonic ω | 1182.1 | — | — | 0.45 | 1181.8–1182.4 | 1175.4 | 1139.0 | ring-ip | yes | 0.00, the mirror image | 1.17 / 1.22 | CH-ip-bend (8.6 um) | 8.64 |
| 1233.0 | harmonic ω | 1233.0 | — | — | 17.27 | 1232.3–1233.7 | 1222.0 | 1184.1 | ring-ip | yes | 0.00, a swap of equivalent atoms 1 | 1.17 / 1.22 | CH-ip-bend (8.6 um) | 8.64 |
| 1302.1 | harmonic ω | 1302.1 | — | — | 0.46 | 1301.5–1303.3 | 1299.2 | 1258.9 | ring-ip | yes | 0.00, a swap of equivalent atoms 1 | 1.17 / 1.22 | CC-stretch/CH-ip (7.7 um) | 15.87 |
| 1454.8 | harmonic ω | 1454.8 | — | — | 2.4 | 1453.9–1456.0 | 1432.9 | 1388.5 | ring-ip | yes | 0.00, the mirror image, rotated | 1.17 / 1.22 | CC-stretch/CH-ip (7.7 um) | 15.87 |
| 1552.0 | harmonic ω | 1552.0 | — | — | 20.31 | 1550.9–1553.7 | 1529.8 | 1482.4 | ring-ip | yes | 0.00, the mirror image | 1.17 / 1.22 | CC-stretch (6.2 um) | 16.09 |
| 1637.1 | harmonic ω | 1637.1 | — | — | 0.49 | 1635.0–1638.5 | 1614.8 | 1564.7 | ring-ip | yes | 0.00, a swap of equivalent atoms 1 | 1.17 / 1.22 | CC-stretch (6.2 um) | 16.09 |
| 3301.8 | harmonic ω | 3301.8 | — | — | 3.02 | 3301.4–3302.3 | 3263.5 | 3133.0 | CH-stretch | yes | 0.00, rotation 2 | 0.8 / 1.67 | above 3200 | 16.05 |
| 3313.2 | harmonic ω | 3313.2 | — | — | 2.0 | 3312.5–3313.9 | 3274.4 | 3143.4 | CH-stretch | yes | 0.00, rotation 2 | 0.8 / 1.67 | above 3200 | 16.05 |
| 3339.2 | harmonic ω | 3339.2 | — | — | 2.99 | 3338.8–3339.6 | 3299.8 | 3167.8 | CH-stretch | yes | 0.00, a swap of equivalent atoms 1 | 0.8 / 1.67 | above 3200 | 16.05 |
| 3344.6 | harmonic ω | 3344.6 | — | — | 0.02 | 3344.5–3344.9 | 3305.4 | 3173.2 | CH-stretch | yes | 0.00, a swap of equivalent atoms 1 | 0.8 / 1.67 | above 3200 | 16.05 |

*Licence caveat: CH-oop on hold-out (a) rests on 5 of the hold-out's 8 molecules (the others have no such band): the 95 % interval of a bootstrap over molecules is 0.93–3.2 cm⁻¹ and crosses the line (96 % of the resamples lie under it); other on hold-out (a) rests on 8 molecules: the 95 % interval of a bootstrap over molecules is 1.45–3.19 cm⁻¹ and crosses the line (93 % of the resamples lie under it).*

*Laboratory region and u_band:* modules/03_lab_scoreboard/build_lab_tables.py FAMILY_RULE (12 Sep 2026), read at the printed position.

## How well the network is known (its product-error record and its evaluation records)

Against ωB97X/6-31G* (the DFT proxy: the network's ΔH is trained on ωB97X − B3LYP Hessians); two quantities, each under its name.

The licence reads the error of the corrected band positions of the seed-mean correction (rms over the family's bands of the corrected band position's error against the higher level (cm⁻¹): the seeds' mean ΔH added to the B3LYP Hessian and diagonalised, each corrected band paired to its higher-level band by mode overlap and counted in the family of its B3LYP partner — what the pipeline prints; with the 95 % interval of a bootstrap over whole molecules).

| family | (a), 8 molecules | (b), 40 molecules | line |
|---|---|---|---|
| ring-ip | 1.17 (95 % interval over molecules 0.9–1.41; 199 bands) | 1.22 (95 % interval over molecules 1.09–1.34; 1194 bands) | 3 |
| CH-stretch | 0.8 (95 % interval over molecules 0.44–1.2; 73 bands) | 1.67 (95 % interval over molecules 1.37–1.95; 410 bands) | 3 |
| CH-oop | 1.86 (95 % interval over molecules 0.93–3.2; 46 bands) | 1.26 (95 % interval over molecules 0.98–1.59; 84 bands) | 3 |
| other | 2.38 (95 % interval over molecules 1.45–3.19; 156 bands) | 2.1 (95 % interval over molecules 1.88–2.34; 1258 bands) | 3 |

Beside it the evaluation records' read-outs — the first-order diagonal error of each seed's correction, averaged over the seeds (each seed's value in brackets), which the licence read until 16 Nov 2026 — and the coupling ratio; targets: 3 cm⁻¹ per family — decision 53's line for ring-ip, CH-oop and 'other', every family's under decision 65 (the licence) — and the coupling ratio ≤ 0.25 of chain 35's T1 line (probes/chain35_read.py).

| read-out | (a), 8 molecules | (b), 40 molecules | target |
|---|---|---|---|
| ring-ip | 1.55 (1.77, 1.52, 1.37) | 1.64 (1.53, 1.49, 1.89) | 3.0 |
| CH-stretch | 1.15 (1.34, 1.19, 0.92) | 2.02 (2.32, 2.2, 1.55) | 3.0 |
| CH-oop | 2.22 (2.22, 2.1, 2.35) | 1.72 (1.8, 1.96, 1.41) | 3.0 |
| other | 2.91 (2.79, 3.1, 2.84) | 3.68 (3.2, 4.15, 3.7) | 3.0 |
| coupling_ratio | 0.147 (0.15, 0.147, 0.143) | 0.17 (0.168, 0.164, 0.177) | 0.25 |

| spectral shape | (a), 8 with an APT | (b), 31 with an APT |
|---|---|---|
| overlap, uncorrected → corrected | 0.277 → 0.977 | 0.366 → 0.975 |
| height error, uncorrected → corrected | 0.227 → 0.109 | 0.511 → 0.216 |

*Read-outs:* rms over the family's B3LYP modes of the first-order diagonal error of a seed's ΔH against the higher level, per seed, and the seeds' mean (cm⁻¹); families by module 05's rule (m05/learning_curve_layerA.molecule_features).
*Hold-outs:* hold-out (a) on its eight molecules never trained on in any version (the set fixed on 30 Oct 2026): eight layer-A molecules held out on 19 Sep 2026; this version's training left out the twins of the hold-out molecules, so the other two, 2-naphthoic acid and benzonitrile, are clean too, and the eight are kept for comparability with v1.3; hold-out (b): every substituted molecule of two scaffold cores, frozen on 8 Oct 2026 — scaffolds the measurement networks never saw. *Coupled cluster:* not measured for this network version: the coupled-cluster reads (T3) were made on an earlier network (chain 34).
*Sources:* E7_rungC_v14s3clean_c00_control_eval_clean_seed0.json; E7_rungC_v14s3clean_c00_control_eval_clean_seed1.json; E7_rungC_v14s3clean_c00_control_eval_clean_seed2.json; E7_rungC_v14s3clean_c00_control_a8read_seed0.json; E7_rungC_v14s3clean_c00_control_a8read_seed1.json; E7_rungC_v14s3clean_c00_control_a8read_seed2.json; E7_rungC_v14s3clean_c00_control_product_error.json.

*Licence:* licensed at the DFT proxy: ring-ip (1.17 / 1.22), CH-stretch (0.8 / 1.67), CH-oop (1.86 / 1.26), other (2.38 / 2.1); not licensed: none — error of the corrected band positions of the seed-mean correction on hold-outs (a) / (b) in cm⁻¹ against 3 (decision 65 as amended on 16 Nov 2026); CH-oop on hold-out (a) rests on 5 of the hold-out's 8 molecules (the others have no such band): the 95 % interval of a bootstrap over molecules is 0.93–3.2 cm⁻¹ and crosses the line (96 % of the resamples lie under it); other on hold-out (a) rests on 8 molecules: the 95 % interval of a bootstrap over molecules is 1.45–3.19 cm⁻¹ and crosses the line (93 % of the resamples lie under it); the first-order diagonal error of each seed's correction, averaged over the seeds, which the licence read until then: ring-ip (1.55 / 1.64), CH-stretch (1.15 / 2.02), CH-oop (2.22 / 1.72), other (2.91 / 3.68); no coupled-cluster licence (README.md, decision 65 as amended on 16 Nov 2026).

## Cost

- Asus18 (laptop): 382 s = 6 min, € 0.00 ex VAT (corpus ledger machine column 'Asus18'); steps optimise 22.7 s, low_level 356.2 s, correction_and_spectra 0.7 s, own_spread 2.5 s

## Provenance

- result C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline\probes\results_m1\pipeline_demo_2026-11-25\furan; run at commit c7e41f8a (uncommitted changes: yes); certificate at c7e41f8a
- deck 9e27bf8e934893f3; low level {"pyscf": "2.15.0", "pyscf_git": null, "numpy": "2.5.2", "python": "3.12.14", "sha256": {"analytic_hessians.py": "f9307fc95a2f", "apt.py": "abf342388bf1"}}; host Asus18
- models: E7_rungC_v14s3clean_c00_control_release_model_n1132_seed0.pt (carried, sha16 6f52c9d8570fbcf5); E7_rungC_v14s3clean_c00_control_release_model_n1132_seed1.pt (carried, sha16 1e820b8755078b90); E7_rungC_v14s3clean_c00_control_release_model_n1132_seed2.pt (carried, sha16 bc4de0b6458e44f2)
- own spread: 8 rotations, 2 mirror images, 1 swap of equivalent atoms, drawn with the seed 7 under RDKit 2026.03.6; each presentation is in certificate.json (own_spread: a rotation's matrix, a swap's or a listing's atom order)
- the models above are release networks, trained on the 1132 labelled entries of their training pool: each of the 3 networks is fitted on a random 85 % of the molecules and stopped on the other 15 %, a different 15 % per seed, so not every molecule is fitted by every network (with 3 networks about 0.15³ ≈ 0.3 % by none); the error bars are those of the measurement networks: E7_rungC_v14s3clean_c00_control_model_n1082_seed0.pt (sha16 89574ed1b69c4e10); E7_rungC_v14s3clean_c00_control_model_n1082_seed1.pt (sha16 03dbbf9f29b59186); E7_rungC_v14s3clean_c00_control_model_n1082_seed2.pt (sha16 8dd85f3f1ba5bbeb)
