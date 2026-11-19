"""TASKS 268, the review's finding 4: folders whose ωB97X label is semi-numerical only, in and outside v1.4's release pool, by layer.

    python semi_numerical.py <module 05 folder>
"""
import collections
import json
import sys
from pathlib import Path

module = Path(sys.argv[1])
run = json.loads((module / "out/v14/E7_rungC_v14s3clean_c00_control_release.json").read_text(encoding="utf-8"))
pool = set(run["pool_ids"])
inside, outside = collections.Counter(), collections.Counter()
for folder in sorted((module / "corpus" / "molecules").iterdir()):
    if (folder / "hessian_wb97x.npz").is_file() and not (folder / "hessian_wb97x_analytic.npz").is_file():
        (inside if folder.name in pool else outside)[folder.name.split("_")[0]] += 1
print("semi-numerical only, in the pool:", dict(inside), sum(inside.values()))
print("semi-numerical only, outside the pool:", dict(outside), sum(outside.values()))
