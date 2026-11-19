"""The independent review of aromir acceptance-269 answered in the release records (18 Nov 2026), after amend_records.py.

    python amend_records_review.py <aromir's releases folder>

K1 (the parent session's decision: the eight decide, the ten are shown and decide nothing): v1.4's hold-out (a) gives the true
reason it is read on eight, and the ten beside it, from a10_measured.json (read_a10.sh, `aromir evaluate`, the measurement
networks). Finding 5: v1.3's hold-out (b) names the two molecules of the list it does not hold, and why. Then release.json binds
v1.4's records again (amend_records.bind). Every edit asserts the text it replaces.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from amend_records import bind, read, replaced, write

HERE = Path(__file__).resolve().parent
V14_A_OLD = "; the other two have a twin in another layer of the training pool and are left out of the read (30 October 2026)"
V13_B_OLD = "those with analytic Hessians at both levels when v1.3 was read; "
V13_B_NEW = ("the 41 on that list less 9-nitrofluorene, which has an imaginary low-level mode, and 1-(trifluoromethyl)fluorene, "
             "which v1.3's training run (chain 35) neither trained on nor read: its record lists it only among the molecules given "
             "analytic labels; ")
SOURCE_V13 = ("hold-out (b)'s two absent molecules: modules/05_support_predictor/out/E7_rungC_chain35_analytic.json "
              "(A2_28eed45ad3 only under substituted_analytic) and probes/results_m1/aromir_audit_v14_2026-11-18/AUDIT.md, K2 "
              "(A2_2c22216564's imaginary mode), of thebreadishard/udacity-capstone-plan (plan 05)")
SOURCE_V14 = ("hold-out (a) on ten, which decides nothing: probes/results_m1/aromir_audit_answers_2026-11-18/a10_measured.json "
              "(read_a10.sh: `aromir evaluate` with the measurement networks on set 'a' of "
              "E7_rungC_v14s3clean_c00_control_eval_clean_seed0.json) of thebreadishard/udacity-capstone-plan (plan 05)")


def ten(measured: dict) -> str:
    errors = measured["a"]["band_error_seed_mean"]
    return ", ".join(f"{family} {e['rms_cm']:.2f} [{e['interval_cm'][0]:.2f}–{e['interval_cm'][1]:.2f}]"
                     for family, e in errors.items())


def main() -> None:
    releases = Path(sys.argv[1])
    measured = json.loads((HERE / "a10_measured.json").read_text(encoding="utf-8"))
    if measured["a"]["n_molecules"] != 10:
        raise SystemExit(f"a10_measured.json holds {measured['a']['n_molecules']} molecules, not ten")
    v14 = read(releases / "v1.4" / "evaluation.json")
    new_a = ("; the licence and the promotion are decided on these eight, the set of 30 October on which v1.3 and v1.4 are both "
             "clean. For v1.4 the other two, benzonitrile and 2-naphthoic acid, are clean as well: on all ten its measurement "
             f"networks read {ten(measured)} cm⁻¹, which decides nothing")
    v14["holdouts"]["a"]["description"] = replaced(v14["holdouts"]["a"]["description"], V14_A_OLD, new_a, "v1.4 (a)")
    v14["sources"] = [*v14["sources"], SOURCE_V14]
    write(releases / "v1.4" / "evaluation.json", v14)
    v13 = read(releases / "v1.3" / "evaluation.json")
    v13["holdouts"]["b"]["description"] = replaced(v13["holdouts"]["b"]["description"], V13_B_OLD, V13_B_NEW, "v1.3 (b)")
    v13["sources"] = [*v13["sources"], SOURCE_V13]
    write(releases / "v1.3" / "evaluation.json", v13)
    bind(releases / "v1.4")


if __name__ == "__main__":
    main()
