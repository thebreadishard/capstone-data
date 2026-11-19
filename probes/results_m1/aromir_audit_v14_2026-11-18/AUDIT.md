# Audit of aromir at 6047467 with release v1.4

Read at a private clone `~/audit_v14_src`, checked out at `6047467` (branch main, "The re-review of b16c67c answered…").
Nothing in `~/aromir-src`, the package or the corpus was written. No quantum chemistry was run. The experiments are the
scripts beside this file (`a0`–`a8`, `run.sh`, `pytest_some.sh`, as `.txt`). They ran in WSL under
`probes/wsl_capped.sh 1024`, with `OMP_NUM_THREADS=2` and `PYTHONPATH=~/audit_v14_src/src`; `aromir.__file__` was
`/home/thebreadishard/audit_v14_src/src/aromir/__init__.py` (a0, a4). Environment: Python 3.12.14, numpy 2.5.4,
torch 2.14.0+cpu, rdkit 2026.09.2, scipy 1.18.1, geomeTRIC 1.1.1, pydantic 2.14.3, pyscf 2.15.0. Stored corpus Hessians
(`hessian_*_analytic.npz`, `H_projected`; semi-numerical `hessian_*.npz` where stated). The converted measurement
networks came read-only from `probes/results_m1/aromir_v14_release_2026-11-18/measurement/`. pytest on six single files
(`test_bundled_release`, `test_release_networks`, `test_card`, `test_refusals`, `test_certificate`, `test_evaluation`):
120 passed in 4.65 s.

**Severity counts (new findings): WRONG-NUMBER 0 · SILENT-ACCEPT 3 · CRASH 0 · CLAIM 6 · PACKAGING 0 · TEST-GAP 1.**
Not reported again, as the brief asks: thin-ground molecule counts, the missing invariance record and its
rotation/mirror/order spread, and the m08 sentence.

Every number about the shipped records was reproduced. `aromir`'s own code with the measurement networks gives
evaluation.json's (b) row exactly: 1.22 / 1.67 / 1.26 / 2.10, first-order 1.53/1.49/1.89 … (a3, a4). The card's counts
1132 / 1078 / 50 / 1028 match the training project's `pool_ids` (a7).

---

## SILENT-ACCEPT

### S1. The pair loader does not compare the two training records, or `release.json` with the evaluation (RAN)
- Where: `release.py:576-620` (`_pair_reasons`) and `release.py:324-364` (`ReleaseNetworks`). The checks cover the
  versions, that the release has no hold-outs, measurement ⊆ release trained SMILES, hold-outs ⊆ release SMILES, the
  seed hashes, and the count of release checkpoints. Nothing else is compared.
- What happens: each case below is one edit to a fresh copy of the bundled v1.4, and `release.load` **accepted** each
  one (a5):
  - `measurement.json` `soft_mode_repair: true` while `training.json` says false. The pipeline prepares the Hessian
    from the release record (`pipeline.py:715`, `certificate.py:382`), so the error bars would belong to differently
    prepared inputs, and nobody is told.
  - Measurement `max_atoms: 30`, or `elements: [C, H]`. The card still prints "Sizes: 8 to 40" and all seven elements,
    and the size gate (`pipeline.py:591`) licenses 31–40-atom molecules on errors from networks that never saw one.
  - A measurement cation parent the release lacks; a measurement `cation_test` different from the release's.
  - `measurement_checkpoints` naming a file that `evaluation.sources` does not name (the bundled names agree, but
    only `test_bundled_release.py:93` checks that, by hard-coded value).
  - `n_entries: 5`. The card then says "trained on the 5 labelled entries … (1078 distinct neutral molecules …)".
  - `checks: {"anything": true}`: no check name is required, so the five checks the README lists can all be absent.
  - Checkpoint hashes `"zz"`: no hex pattern is enforced. `fitted_share: 0.5` is also accepted; it changes the card's
    "≈ 0.3 % by none" sentence.
- Smallest fix: in `_pair_reasons`, refuse unless the two records have equal `elements`, `min_atoms`, `max_atoms`
  and `soft_mode_repair`; unless measurement cation parents ⊆ release cation parents and the cation tests are equal;
  unless every `measurement_checkpoints` name appears in `evaluation.sources`; unless `n_entries` ≥ neutral SMILES +
  cation parents; and unless `checks` holds a required set of names. Add `pattern=^[0-9a-f]{16}$` to the checkpoint
  hashes.

### S2. The error tables' own consistency is not validated, and `measured.json` is never read (RAN)
- Where: `release.py:94-119` (`BandError`), `release.py:52` (`MEASURED_FILE`, used only in a test).
- Accepted (a5):
  - (a)/other `interval_cm: [0.1, 0.2]` with `rms_cm 2.38`, so the rms lies outside its own resampling interval.
    The card prints `2.38 [0.10–0.20]`, and the family drops off "thin ground".
  - `interval_cm [3.5, 4.0]` with `share_of_resamples_within_line: 1.0`.
  - `n_modes: 1`.
  - An evaluation.json value changed to 0.10 while `measured.json` still says 2.38. The loader never compares them;
    only `test_bundled_release.py:121` does, and only for the bundled folder.
- Fix: require `low ≤ rms ≤ high` (the full-sample rms of a bootstrap lies inside its interval in practice; allow
  rounding of 0.01), `share` consistent with the line (`high ≤ line ⇒ share = 1`, `low > line ⇒ share = 0`), and,
  where `measured.json` exists, `record_tables(measured) == evaluation tables` in `load`.

### S3. Nothing binds the records to the weights (RAN, follows from S1/S2)
- `release.json` binds the tensor files (`seed_sha256`). No file binds `evaluation.json`, `training.json`,
  `measurement.json` or `measured.json`, so every edit in a5 still loaded with valid weights. The first audit's
  "manifest hash over all release files" (its S2) is not done. Before the upload this matters more: once the folder is
  copied elsewhere, the records are what a user trusts.
- Fix: a sha256 per record file in `release.json` (or a `MANIFEST.sha256`), verified in `load`.

---

## CLAIM

### K1. Hold-out (a) leaves out two molecules for a reason that no longer holds (RAN)
- Text: `evaluation.json` `holdouts.a.description`, printed on the card (`MODEL_CARD.md:35`) and on every certificate:
  "the other two have a twin in another layer of the training pool and are left out of the read (30 October 2026)".
- What the records say:
  - The measurement networks' run record `out/v14/E7_rungC_v14s3clean_c00_control.json` has
    `"holdout_twins": "drop-any-charge"`, and its `holdout_twins_dropped` includes `B_3100da3761` and `B_07cadc7923`.
    These are the B-layer twins of benzonitrile (`A_3100da3761`) and 2-naphthoic acid (`A_07cadc7923`), with the
    cation `P3c_07cadc7923`.
  - `measurement.json` `trained_smiles` holds neither `N#Cc1ccccc1` nor `O=C(O)c1ccc2ccccc2c1` (a1, a2).
  - The measurement networks' own record still evaluates a 10-molecule set "a" in which 0 of 10 are trained on (a2).
  - So at v1.4 both molecules are as held out as the other eight.
- With them, by aromir's code and the measurement networks (a3, `a10`), band error of the seeds' mean on 10
  molecules:

  | family | rms | 95 % interval | bands | printed for 8 molecules |
  |---|---|---|---|---|
  | ring-ip | 1.10 | 0.82–1.34 | 231 | 1.17 |
  | CH-stretch | 0.78 | 0.47–1.15 | 86 | 0.80 |
  | CH-oop | 1.75 | 0.91–2.83 | 61 | 1.88 |
  | other | 2.23 | 1.34–3.02 | 186 | 2.38 |

  CH-oop would no longer be "on thin ground", and 'other' would be barely on it. The printed numbers are the more
  conservative ones, but the stated reason is false.
- Fix: read (a) on all ten, or replace the reason with the true one (for example "kept at the eight of 30 October so
  that versions compare").

### K2. (b) "every substituted molecule of two ring scaffolds" omits 31 never-trained substituted molecules, and a third hold-out still goes unmentioned (RAN; first audit K2 not held)
- What happens:
  - The release checks record lists 41 molecules in `holdout_b_frozen_2026-10-08.txt`. One, `A2_2c22216564`
    (9-nitrofluorene), is dropped as "not in the release training data". aromir's evaluation refuses it because its
    low-level Hessian has one imaginary mode (a3).
  - The measurement record also evaluates `b+`: 30 fluoranthene children, of which 0 are in either network's
    training data and 0 are in any held-out list (a2). They have semi-numerical Hessians only.
  - `evaluation.json` mentions neither set.
- Measured on b+ with aromir (a3), band error of the seeds' mean. Measurement networks: ring-ip 1.56, CH-stretch 0.90,
  CH-oop 2.67 [2.39–2.94], other **3.24** [2.55–3.94], 28 % of resamples within the line. The shipped release
  networks, for which b+ is truly out of sample: 1.48, 0.81, 2.62, **3.03**.
- The labels are the reason this is no verdict. On the 40 molecules of (b), the same networks score other 2.10 against
  analytic labels and 4.35 against semi-numerical ones, and CH-oop 1.26 against 2.60 (a4). So b+'s 3.24 on noisy
  labels is not evidence that 'other' fails; if anything b+ scores better than (b) does on the same kind of label.
- The claim is still wrong as written, and b+ is the one set on which the shipped networks themselves have a
  held-out error.
- Fix: describe (b) as "the substituted molecules of the two scaffolds with analytic Hessians and a minimum at the low
  level (40 of 71)". Name b+ in `evaluation.json` and why it is not read, and analytic labels for b+ would give the
  release networks an out-of-sample number.

### K3. "The error of what the release delivers" and "what this certificate's positions are" name the wrong networks for v1.4 (RAN)
- Text: `evaluation.json` `licence_basis` ("the band error of the seeds' mean, the error of what the release
  delivers"), printed by `card.py:118` and `certificate.py:572`; and `certificate.py:568-570`: "The rms error of the
  corrected band positions … : what this certificate's positions are". Both appear in every v1.4 certificate (read in
  `a8`'s naphthalene certificate). Similar wording is in `README.md:111-113` and the docstring at `release.py:126-127`.
- For v1.4 the table is the measurement networks' error. The certificate's positions come from the release
  networks, which differ from the measurement networks by 0.95 cm⁻¹ rms and up to 9.70 cm⁻¹ per band on 60 random
  corpus molecules (3,987 bands; 1.4 % above 3 cm⁻¹; a6).
- The opening paragraph (`made_by`) says this correctly; the two sentences lower down contradict it.
- Fix: for a pair, word them as "the error of the measurement networks' seed mean, the error bar of what is printed",
  from `release.shipped`, not from the record's fixed text.

### K4. The README says the network is trained on neutral, closed-shell molecules; v1.4 also trained on 50 radical cations (READ)
- `README.md:30`: "The network is trained on neutral, closed-shell aromatic molecules …". `training.json` has 50
  `cation_parent_smiles` (45 for the measurement networks), and the card says so (`MODEL_CARD.md:55`). The README
  sentence is meant as the input domain but reads as the training set.
- Fix: "accepts neutral, closed-shell …; v1.4 was also trained on the radical cations of 50 molecules".

### K5. The card's file list omits three of the records it is written from (READ)
- `card.py:363-366`, `MODEL_CARD.md:90`: "`evaluation.json` and `training.json` hold the records this card is
  written from". The **Networks** line and the counts come from `release.json` and `measurement.json`, and
  `measured.json` is the evaluation's source.
- Fix: list the files actually present.

### K6. "No measurement network trained on a molecule of either scaffold" holds by exact scaffold only (RAN)
- (b) is 21 fluorene and 19 fluoranthene derivatives. Five `measurement.json` trained molecules contain the whole
  fluoranthene ring system as a substructure, for example benzo[k]fluoranthene `c1ccc2cc3c(cc2c1)-c1cccc2cccc-3c12`
  and its OMe, CF₃ and CHO derivatives, and `Sc1ccc2cccc3c2c1-c1cc2ccccc2cc1-3` (a1). No fluorene-containing molecule
  and no fluorene or fluoranthene cation is in the measurement data.
- The sentence is true for Murcko scaffolds but not for "molecules of either scaffold" in the sense a reader takes.
- Fix: say "no molecule whose ring system is fluorene or fluoranthene; five benzo-annulated fluoranthenes were trained
  on".

---

## TEST-GAP

### T1. The pair's consistency and v1.4's platform agreement rest on hard-coded values and one molecule
- None of the S1/S2 cases has a test. `test_release_networks.py:158` (`a_pair_that_does_not_fit_together`) covers
  only the reasons `_pair_reasons` already gives.
- The only v1.4 platform pin is 4-cyanobiphenyl computed on Linux (`test_bundled_release.py:20`, key
  `delta_h_linux`). The tolerance's justification (`:35-38`, Linux and Windows 7e-9, 2.4e-7 over 76 molecules) was
  measured for v1.3. Whether v1.4 agrees on macOS rests on a CI run I could not see.
- Fix: parametrise S1/S2 as refusal tests; add two or three v1.4 pins and record the macOS difference in the docstring.

---

## First audit's findings at 6047467
- W1 rotation, W2 xyz order, W3 mirror: not held, excluded by the brief (measured separately; v1.4 has no
  `invariance.json`). The card and certificate now say it is unmeasured (`MODEL_CARD.md:68-69`).
- W4 position outside its seed range: **held**. The range now includes the position (`certificate.py:160-163`); 0 of
  3,987 bands outside (a6).
- W5 scale factors: **held**. `spectrum.py:36` is (0.979, 0.969, 0.960), exactly Table 2's 6-31G* row of Bauschlicher
  et al. 2018. I read the paper (astrochem.org PDF): 4-31G is (0.956, 0.952, 0.960), and the edges are 1111.1 and
  2500 cm⁻¹, as coded.
- W6 isotopes: **held**. `[2H]c1ccccc1` and `[13cH]1ccccc1` are refused, exit 2 (a8).
- S1 imaginary corrected band: **held**. Exit 3 (`cli.py:143-150`), never licensed (`certificate.py:116-124`); a band
  imaginary for one seed is unlicensed (by reading; tests `test_refusals.py:144,156` pass).
- S2 record validators: **partly**. Errors ≥ 0 and finite, elements ⊆ ELEMENTS, min ≤ max, hold-out names and counts,
  and seed number against file name are refused. The interval/share/n_modes checks, `measured.json`, the pair fields
  and a records hash are missing (S1–S3 above).
- S3 stereo: **held**. `unassigned_stereo` is noted on the certificate (`certificate.py:321-325`); trained
  stereoisomers are not called unseen (`certificate.py:195-212`).
- S4 text after the SMILES: **held**. `"c1ccccc1 benzene"`, `"c1ccccc1é"`, a tab, a leading blank and `""` are all
  refused (a8).
- S5 `card --out` overwrite: **held** (a8).
- S6 sizes: **held**. 42-atom hexacene is refused by the size gate unless `--outside-training-sizes` is given (a8).
  `check` is still not size-gated, by design.
- C1 tracebacks: **held** for every case tried. Benzyne gives a one-line refusal (a8); a damaged `.npz`, a non-UTF-8
  record, and a missing, truncated or damaged weight file give one-line refusals (`release.py:685-699`); `main` has a
  last `except (OSError, ValueError, ArithmeticError)` (`cli.py:214`). Wrong-reason messages remain: a duplicated atom
  gives "no neutral bonding pattern", and a one-carbon xyz gives "no aromatic ring" (a8), which is correct.
- C2 lost DFT, no resume: **held** (REASONED). The low level is saved before the minimum check (`pipeline.py:380-392`),
  the network inputs are built on the start geometry before the DFT (`:603-618, :710`), and the same `--out` resumes
  (`:196-226`).
- C3 soft-mode refusals: **held** (REASONED). The minimum is decided on the repaired Hessian, with one step off a saddle
  point and a re-optimisation (`pipeline.py:438-472`).
- C4 blocking folder: **held**, as C2.
- K1 first-order error printed as the product's: **held**. The record format 2 has the band error of the seed mean,
  reproduced by me exactly on (b).
- K2 the unmentioned `b+`: **not held**. See K2 above.
- K3 licence whatever the molecule: **partly**. No licence outside the training sizes; the licence is otherwise still
  per family.
- K4 family names: **held**. X–H bands are unlicensed by the off-carbon rule (45 bands in 60 molecules, a6), and the
  rules are spelled out on the card and certificate.
- K5 the certificate omits what is not in the error: **held** (the "What the measured error does not cover" section).
- K6 psi4 geometries against the "exactly this level" claim: **not held**. `dft.py:3-5` is unchanged, and the card
  names no end-to-end comparison.
- K7 stale statements:
  - "by construction" is now limited to symmetry and translations (`README.md:171`): held.
  - "one canonical order" is now qualified: held.
  - "Two checks and a repair" (`README.md:129`) now holds, with the step off the saddle point: held.
  - The Lorentzian curve is stated as unused (`CHANGELOG.md:36-37`): held.
  - "baseline the correction will be compared with" is gone: held.
  - The README:6 chain claim now says no full-chain test exists: held.
  - CONTRIBUTING's timing is now "in seconds": held.
  - `pipeline.py:3` is true after C2: held.
  - CHANGELOG isotopes: held.
- K8 untraceable sources: **partly**. `measured.json` now ships. The sources still name paths in the private training
  repository, with no hashes of those files.
- K9 SMILES string equality: **partly**. rdkit's upper bound is `<2026.10`, and a test checks that every listed
  SMILES is in present canonical form. The lower bound `>=2023.9` is untested (README says so).
- P1 open-ended dependencies: **held**. Every dependency has an upper bound (`pyproject.toml:37-44`).
- P2 threads: **held** for `spectrum` (`pipeline.py:709`). `evaluate` and `card` leave torch's default, which is minor.
- P3 tooling drift: **held**. Weights are excluded from the large-file hook, ruff is pinned 0.17.5 in both places, and
  CI covers 3.11–3.13.
- P4 CUDA wheel: **held** (README Install).
- T1 tests to add:
  - 1/2 (rotation, shuffled xyz): not added, excluded.
  - 3 (release numbers from the package): partly. For v1.3 they are reproduced from stored Hessians
    (`test_v13_on_stored_hessians.py`); for v1.4 only measured.json against evaluation.json is checked, since the
    measurement networks are not shipped.
  - 4 (CLI failures as one line): held (`test_refusals.py`).
  - 5 (after a failure): held except the quantum full-chain test (the README says none exists).
- T2 tests that pass with the feature broken: **partly**. The saddle and refusal tests are now real. The platform pin is
  still one molecule (T1 above).

## Checked, nothing found
- `measurement.trained_smiles` ⊆ `training.trained_smiles` (1028 ⊆ 1078). All 48 hold-outs are in the release data
  and none in the measurement data. No measurement cation parent is a hold-out. The release-only neutral molecules
  are exactly benzonitrile and 2-naphthoic acid (a1).
- The card's counts against the training project's `pool_ids` (a7):
  - Release: 1132 ids = 1082 neutral (1078 distinct SMILES, 4 duplicate ids) + 50 cations.
  - Measurement: 1075 ids = 1030 neutral (1028 distinct) + 45 cations.
  - 0.15³ ≈ 0.3 % is the right arithmetic.
  - The checkpoint name "n1082" of the measurement networks is not their pool size, but the package never prints it.
- evaluation.json against its stated sources: (b) reproduced to every printed digit by aromir's `molecule_errors`
  with the converted measurement networks (a3, a4). The release-check record's measurement column (a8: 1.1689,
  0.8011, 1.8609, 2.3777) rounds to the (a) row.
- Acquaintance sentences (a6):
  - Benzene, benzonitrile, 2-naphthoic acid and naphthalene give "in the release networks' training data".
  - The cation clause fires for the two release cation parents whose neutral parent is not trained on
    (`Cc1cccc(F)n1`, 9-nitroanthracene).
  - A b+ molecule gives "has not seen it".
- The benzene check in `release.json` is backed by the record (`…_release_release_checks.json`: benzene fitted by
  seeds 0 and 2, its bands listed).
- `aromir evaluate` refuses the bundled release networks (exit 2). With the measurement folder, a damaged `.npz` is a
  one-line refusal (a8).
- The `Evaluation` mean-of-seeds and family/hold-out coverage validators; the version mismatch of measurement.json is
  refused (a5).
- `partners` is a one-to-one assignment (`spectrum.py:115-124`), so no reference band is counted twice in the
  evaluation.
- The release and measurement networks on b+ (out of sample for both): the shipped networks are no worse than the
  measurement networks in any family (a3). On this evidence, substituting the measurement networks' error bars for
  the release networks' is conservative.

Sources: [Bauschlicher et al. 2018, ApJS 234, 32 (astrochem.org PDF), Table 2](https://astrochem.org/docs/Bauschlicher_2018_ApJS_234_32.pdf).
