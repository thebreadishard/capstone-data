"""The v1.4 audit's answers in aromir's release records (TASKS 269, criterion 5): words that were not true, and the hashes.

    python amend_records.py <aromir's releases folder>
    python amend_records.py bind <a release folder>      (the hashes again, after another record changed)

K2/K6: hold-out (b)'s description in v1.4 and v1.3 says which molecules it holds and what the networks trained on, as counted
on 18 Nov 2026 (scaffolds.py beside this file: v1.4's measurement networks trained on 5 molecules containing fluoranthene's ring
system and none containing fluorene's; v1.3's on neither; v1.4's (b) 21 fluorene and 19 fluoranthene children, v1.3's 20 and 19).
K3: v1.4's licence basis names the measurement networks. S3: v1.4's release.json binds its records by the hash of their content,
with aromir's own `release.record_sha256`, written last. Every edit asserts the text it replaces.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from aromir import release

V14_B_OLD = ("every substituted molecule of two ring scaffolds, set aside on 8 October 2026; no measurement network trained on a "
             "molecule of either scaffold")
V14_B_NEW = ("the 40 substituted molecules of two ring scaffolds, fluorene (21) and fluoranthene (19), set aside on 8 October 2026, "
             "that have analytic Hessians at both levels and a minimum at the low level: of the 41 on that list, 9-nitrofluorene has "
             "an imaginary low-level mode, and 30 more fluoranthene children (set b+) have semi-numerical Hessians only and are not "
             "read here. No measurement network trained on a molecule containing fluorene's ring system; five that contain "
             "fluoranthene's, benzo[k]fluoranthene and four of its derivatives, were trained on")
V13_B_OLD = ("every substituted molecule of two ring scaffolds, set aside on 8 October 2026; the network trained on no molecule of "
             "either scaffold")
V13_B_NEW = ("39 substituted molecules of two ring scaffolds, fluorene (20) and fluoranthene (19), set aside on 8 October 2026, "
             "those with analytic Hessians at both levels when v1.3 was read; 30 more fluoranthene children (set b+) have "
             "semi-numerical Hessians only and are not read here. The network trained on no molecule containing either ring system")
DESCRIBED_BY = ("hold-out (b)'s description: modules/05_support_predictor/corpus/holdout_b_frozen_2026-10-08.txt (41 "
                "molecules) and probes/results_m1/aromir_audit_answers_2026-11-18/scaffolds.log and murcko.log of "
                "thebreadishard/udacity-capstone-plan (plan 05); 9-nitrofluorene's imaginary mode and set b+: "
                "probes/results_m1/aromir_audit_v14_2026-11-18/AUDIT.md, K2")
BASIS_OLD ="the band error of the seeds' mean, the error of what the release delivers, "
BASIS_NEW = ("the band error of the measurement networks' seed mean, the error bar of what the release networks deliver, ")


def read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, record: dict) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, path)
    print(f"wrote {path}", flush=True)


def replaced(text: str, old: str, new: str, where: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"{where}: the text to replace is there {text.count(old)} times")
    return text.replace(old, new)


def main() -> None:
    releases = Path(sys.argv[1])
    v14 = read(releases / "v1.4" / "evaluation.json")
    v14["holdouts"]["b"]["description"] = replaced(v14["holdouts"]["b"]["description"], V14_B_OLD, V14_B_NEW, "v1.4 (b)")
    v14["licence_basis"] = replaced(v14["licence_basis"], BASIS_OLD, BASIS_NEW, "v1.4 basis")
    v14["sources"] = [*v14["sources"], DESCRIBED_BY]
    write(releases / "v1.4" / "evaluation.json", v14)
    v13 = read(releases / "v1.3" / "evaluation.json")
    v13["holdouts"]["b"]["description"] = replaced(v13["holdouts"]["b"]["description"], V13_B_OLD, V13_B_NEW, "v1.3 (b)")
    v13["sources"] = [*v13["sources"], DESCRIBED_BY]
    write(releases / "v1.3" / "evaluation.json", v13)
    bind(releases / "v1.4")


def bind(folder: Path) -> None:
    """release.json's hashes of the records beside it, in RECORDED_FILES' order."""
    record = read(folder / release.RELEASE_FILE)
    hashes = {name: release.record_sha256(folder / name) for name in release.RECORDED_FILES}
    ordered = {key: value for key, value in record.items() if key != "record_sha256"}
    at = list(ordered).index("seed_sha256") + 1
    items = list(ordered.items())
    write(folder / release.RELEASE_FILE, dict([*items[:at], ("record_sha256", hashes), *items[at:]]))


if __name__ == "__main__":
    if sys.argv[1:2] == ["bind"]:
        bind(Path(sys.argv[2]))
    else:
        main()
