"""Read-only follow-up (TASKS 297, fact 5): imaginary modes of the 60 cations, and for the 11 with a less symmetric geometry than
the parent the tolerance at which the parent's order comes back (how far the distortion goes) and the lowest frequency."""
import csv
import json
import re
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "src"))
from dpir.symmetry import point_group_ops  # noqa: E402

CORPUS = PLAN / "modules" / "05_support_predictor" / "corpus"
rows = [r for r in csv.DictReader((CORPUS / "manifest.csv").open(encoding="utf-8")) if r["layer"] == "P3c" and r["status"] == "done"]
imag = {"b3lyp": 0, "wb97x": 0}
for r in rows:
    res = json.loads((CORPUS / "molecules" / r["id"] / "result.json").read_text(encoding="utf-8"))
    for k in imag:
        imag[k] += int(res[f"n_imaginary_{k}"] > 0)
    parent = re.search(r"parent (\w+)", r["note"])[1]
    g = json.loads((CORPUS / "molecules" / r["id"] / "geometry.json").read_text(encoding="utf-8"))
    gp = json.loads((CORPUS / "molecules" / parent / "geometry.json").read_text(encoding="utf-8"))
    xyz, xyz_p = np.array(g["coords_bohr"], float), np.array(gp["coords_bohr"], float)
    target = len(point_group_ops(gp["symbols"], xyz_p, 0.02))
    if len(point_group_ops(g["symbols"], xyz, 0.02)) >= target:
        continue
    back = next((t for t in (0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2) if len(point_group_ops(g["symbols"], xyz, t)) >= target), None)
    f = np.array(res["freq_b3lyp_cm"], float)
    print(f"{r['id']} {r['name'][:26]:26s} parent order {target:2d}; back at tol {back} bohr; lowest B3LYP {f.min():7.1f} cm-1; "
          f"imaginary b3lyp/wb97x {res['n_imaginary_b3lyp']}/{res['n_imaginary_wb97x']}")
print(f"cations with an imaginary mode: B3LYP {imag['b3lyp']} of {len(rows)}, wB97X {imag['wb97x']} of {len(rows)}")
