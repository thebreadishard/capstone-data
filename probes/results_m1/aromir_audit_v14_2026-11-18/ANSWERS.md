# Answers to the audit of aromir 6047467 (v1.4), 18 November 2026

Every finding of `AUDIT.md`, with the answer and where it is. Code on aromir branch `acceptance-269`: `adc82f9` (TASKS 266)
and `8d9d6e4` (this audit), then `b093163` (the independent review of both: its nine findings); full suite 473 passed and
3 xfailed at `b093163`. Record edits by `probes/results_m1/aromir_audit_answers_2026-11-18/amend_records.py` (log beside it).

| finding | answer | where |
|---|---|---|
| S1 pair loader | refused now: measurement record of another domain (elements, min/max atoms, soft-mode repair), another cation test, cations the release lacks, `n_entries` below distinct neutral SMILES + cation parents, checks other than the five of `RELEASE_CHECKS`, measurement checkpoints not named in `evaluation.sources`, checkpoint hashes that are not 16 hex digits (seed hashes 64). `fitted_share` and `release.json`'s other own fields stay free: **nothing binds `release.json` itself** (the review of 18 Nov, finding 2; an earlier version of this line said S3's hash did); the README and CHANGELOG say so | `release.py` `_scope_reasons`, `_entry_reasons`, `ReleaseNetworks._named_as_expected`; tests in `test_release_networks.py` |
| S2 tables | refused now: rms outside its interval (±0.01), a share the interval contradicts (a recorded 97.5th percentile below the line ⇒ ≥ 0.97 — below, not at, since a recorded 3.00 may be 3.004; 2.5th above ⇒ ≤ 0.03), `n_molecules > n_modes`, and tables or hold-out sizes that differ from `measured.json` where it exists | `BandError._an_interval`, `Evaluation._shares_fit_the_line`, `_measured_reasons`; tests in `test_release.py` |
| S3 binding | `release.json` binds `evaluation.json`, `training.json`, `measurement.json`, `measured.json` by the SHA-256 of their content as Python's JSON reader gives it (line endings, whitespace, key order and escapes do not change it; 1 and 1.0 differ); a changed or missing record is refused. A guard against an accidental change, not a signature. Limits: `release.json` itself is not bound; a folder without release networks (v1.3) has no such binding | `release.record_sha256`, `_record_hash_reasons`; tests |
| K1 hold-out (a) on 8 | decided by the parent session (18 Nov): the eight decide — the set of 30 October on which v1.3 and v1.4 are both clean and the promotion was decided; the ten are printed beside them and decide nothing. v1.4's (a) says so, with the ten read by `aromir evaluate` on the measurement networks: ring-ip 1.10 [0.82–1.34], CH-stretch 0.78 [0.47–1.15], CH-oop 1.75 [0.91–2.83], other 2.23 [1.34–3.02] (`aromir_audit_answers_2026-11-18/a10_measured.json`, run `aromir_audit_read_a10`, 9 s, 0.44 GB) | v1.4 `evaluation.json` (`amend_records_review.py`) |
| K2 (b) description, b+ | v1.4: "the 40 … that have analytic Hessians at both levels and a minimum at the low level: of the 41 on that list, 9-nitrofluorene has an imaginary low-level mode, and 30 more fluoranthene children (set b+) have semi-numerical Hessians only and are not read here"; v1.3: its 39 are the 41 less 9-nitrofluorene (imaginary mode) and 1-(trifluoromethyl)fluorene, which v1.3's training run neither trained on nor read (the review's finding 5) | `evaluation.json` of both; sources cite `holdout_b_frozen_2026-10-08.txt`, `scaffolds.log` |
| K3 whose error | certificate: "the error of the version's measurement networks … and the error bar of this certificate's positions" for release networks; v1.4's licence basis names the measurement networks; README and `release.py` docstring | `certificate._whose_error`, v1.4 `evaluation.json`; tests |
| K4 README cations | "aromir accepts neutral, closed-shell … (v1.4's also trained on the radical cations of 50 of them)" | `README.md` |
| K5 card's files | the card lists the records present and says `release.json` binds them | `card._files`; test |
| K6 scaffolds | v1.4's (b): "No measurement network trained on a molecule containing fluorene's ring system; five that contain fluoranthene's, benzo[k]fluoranthene and four of its derivatives, were trained on" (`scaffolds.log`, `murcko.log`: all five have benzo[k]fluoranthene's Murcko scaffold); v1.3 trained on neither (same log) | `evaluation.json` |
| T1 tests | S1/S2/S3 each have refusal tests. The v1.4 platform pin is still one molecule computed on Linux; CI's macOS jobs passed it on 6047467 (run 44267566555). **Stated as a limit**; more pins are TASKS 269's criterion 2 (aromir against the pipeline on 19 molecules) | — |
| first audit K2 (b+) | answered by K2 above | |
| first audit K6 (`dft.py`) | `dft.py` now says the training Hessians were psi4's at psi4's minima and that the effect has not been measured end to end; the end-to-end number is criterion 2 | `dft.py` |
| first audit S2, K3, K8, K9, T1, T2 (partly) | S2, T1, T2: above. K3 (licence per family whatever the molecule): by design, stated on card and certificate. K8: the sources name paths of the public repository thebreadishard/udacity-capstone-plan; `probes/results_m1` paths are in its public data mirror, not in git — a limit. K9: RDKit's lower bound untested, the README says so — a limit | |
| first audit P2 (threads of `evaluate`, `card`) | minor; left as it is | |

Not answered in aromir (a TASKS 269 line, for the next release): the capstone's release scripts under `probes/results_m1` are
records of v1.3's and v1.4's builds and are not run again as they stand — `aromir_v14_release_2026-11-18/make_folders.py` writes
`release.json` without `record_sha256`; `aromir_v14_release_2026-11-18/make_evaluation_record.py`,
`aromir_audit_fixes_2026-11-16/make_evaluation_record.py` and `aromir_266_counts_2026-11-18/upgrade_record.py` call
`evaluation.record_tables` (now `release.record_tables`) and the first two write format 2. The next release's writer starts from
`release.record_tables`, format 3 and `release.record_sha256`. The caveat's resampling counts a draw without a band of the family
as an rms of zero (the review's finding 6): negligible for 5 of 8 molecules (0.04 % of draws), not for 1 or 2 of 8; the wording
now says what is drawn, and resampling only the molecules with a band is a change of numbers of its own.
