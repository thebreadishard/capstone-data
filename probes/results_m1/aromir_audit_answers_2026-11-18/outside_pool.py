"""TASKS 268: why 59 corpus folders with a ωB97X analytic Hessian are in no v1.4 release seed's training data.

    python outside_pool.py <module 05 folder> <out.json>

The release run (out/v14/E7_rungC_v14s3clean_c00_control_release.json) read corpus/molecules with --pool-layers A,A2,B,P3,P3c and
--use-analytic; its loader drops a molecule with an imaginary mode (m05/rungC_train.py load_corpus). Per folder outside the pool:
its layer, and the lowest wavenumber of each analytic Hessian (aromir's own vibrational analysis, on the stored geometry).
Read-only, no quantum chemistry.
"""
from __future__ import annotations

import collections
import json
import os
import sys
from pathlib import Path

import numpy as np
from aromir import vibrations
from aromir.molecule import Geometry


def lowest(folder: Path, level: str) -> float:
    g = json.loads((folder / "geometry.json").read_text(encoding="utf-8"))
    symbols = tuple(s[0].upper() + s[1:].lower() for s in g["symbols"])
    geometry = Geometry(symbols, np.array(g["coords_bohr"], float))
    with np.load(folder / f"hessian_{level}_analytic.npz") as z:
        hessian = np.array(z["H_projected"], float)
    return float(vibrations.vibrational_modes(hessian, geometry).wavenumbers.min())


def ids(path: Path) -> set[str]:
    """A frozen hold-out file's ids, as m05/e6_learning_curve.py reads them: one per line, '#' comments and blanks ignored."""
    return {line.split()[0] for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")}


def main() -> None:
    module, out = Path(sys.argv[1]), Path(sys.argv[2])
    run = json.loads((module / "out/v14/E7_rungC_v14s3clean_c00_control_release.json").read_text(encoding="utf-8"))
    pool, layers = set(run["pool_ids"]), run["pool_layers"].split(",")
    corpus = module / "corpus" / "molecules"
    labelled = sorted(p.name for p in corpus.iterdir() if (p / "hessian_wb97x_analytic.npz").is_file())
    frozen = {key: ids(module / "corpus" / name) for key, name in (("c", "holdout_c.txt"), ("r4", "holdout_rung4_test.txt"))}
    rows, why = {}, collections.Counter()
    for molecule_id in labelled:
        if molecule_id in pool:
            continue
        layer = molecule_id.split("_")[0]
        row = {"layer": layer}
        if layer not in layers:
            row["reason"] = f"layer {layer} is not among the pool's layers {run['pool_layers']}"
        elif molecule_id in frozen["c"]:
            row["reason"] = "hold-out (c), never trained (decision 54; corpus/holdout_c.txt)"
        elif molecule_id in frozen["r4"]:
            row["reason"] = "rung 4's test family, never trained (corpus/holdout_rung4_test.txt)"
        else:
            row["lowest_b3lyp_cm"] = round(lowest(corpus / molecule_id, "b3lyp"), 2)
            row["lowest_wb97x_cm"] = round(lowest(corpus / molecule_id, "wb97x"), 2)
            imaginary = min(row["lowest_b3lyp_cm"], row["lowest_wb97x_cm"]) < 0
            row["reason"] = "an imaginary mode in an analytic Hessian" if imaginary else "unexplained"
        rows[molecule_id] = row
        why[row["reason"]] += 1
    record = {"labelled": len(labelled), "pool": len(pool), "outside": len(rows), "by_reason": dict(why), "molecules": rows}
    for reason, n in why.items():
        print(f"{n:3d}  {reason}", flush=True)
    tmp = out.with_name(out.name + ".tmp")
    tmp.write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
    os.replace(tmp, out)
    print(f"wrote {out}", flush=True)


if __name__ == "__main__":
    main()
