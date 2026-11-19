"""Evaluation records of format 3 for aromir's v1.3 and v1.4 (TASKS 266): each family's band error counts its molecules.

    python upgrade_record.py placeholder <evaluation.json of format 2> <out.json>
    python upgrade_record.py compose <evaluation.json of format 2> <measured.json of format 2> <new measured.json> <counts.json> <out.json>

`placeholder`: the record as format 3 with every count set to its hold-out's size — only so that aromir's loader takes the
folder `aromir evaluate` reads the licence line from; it is never shipped.
`compose`: the record aromir ships. `aromir evaluate` (format 3) wrote <new measured.json>; it must equal the old measurement in
every number it already held, and its counts must equal count_bands.py's (the route without the network), or nothing is written.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from aromir import evaluation

COUNTED_BY = ("the molecules with a band of each family: the same `aromir evaluate` (format 3); counterpart, equal in every cell: "
              "probes/results_m1/aromir_266_counts_2026-11-18/count_bands.py of thebreadishard/udacity-capstone-plan (plan 05), "
              "the molecules with a low-level mode of the family")


def read(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path: str, record: dict) -> None:
    target = Path(path)
    tmp = target.with_name(target.name + ".tmp")
    tmp.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, target)
    print(f"wrote {target}", flush=True)


def placeholder(old_path: str, out: str) -> None:
    record = read(old_path)
    if record["record_version"] != 2:
        raise SystemExit(f"{old_path}: format {record['record_version']}, expected 2")
    for per_holdout in record["band_error_seed_mean_cm"].values():
        for name, error in per_holdout.items():
            error["n_molecules"] = record["holdouts"][name]["n_molecules"]
    write(out, record | {"record_version": 3})


def without_counts(measured: dict) -> dict:
    out = json.loads(json.dumps(measured))
    for holdout in out.values():
        for error in holdout["band_error_seed_mean"].values():
            error.pop("n_molecules")
    return out


def compose(old_path: str, old_measured_path: str, new_measured_path: str, counts_path: str, out: str) -> None:
    old, old_measured, new_measured, counts = read(old_path), read(old_measured_path), read(new_measured_path), read(counts_path)
    if without_counts(new_measured) != old_measured:
        raise SystemExit("STOP: the new measurement differs from the old one in a number both hold")
    differ = [(name, family, error["n_molecules"], counts[name][family])
              for name, holdout in new_measured.items() for family, error in holdout["band_error_seed_mean"].items()
              if error["n_molecules"] != counts[name][family]]
    if differ:
        raise SystemExit(f"STOP: evaluate's counts differ from count_bands.py's: {differ}")
    record = old | {"record_version": 3} | evaluation.record_tables(new_measured)
    record["sources"] = [*old["sources"], COUNTED_BY]
    for name, holdout in new_measured.items():
        print(f"({name}) " + ", ".join(f"{family} {error['n_molecules']} of {holdout['n_molecules']}"
                                       for family, error in holdout["band_error_seed_mean"].items()), flush=True)
    write(out, record)


if __name__ == "__main__":
    {"placeholder": placeholder, "compose": compose}[sys.argv[1]](*sys.argv[2:])
