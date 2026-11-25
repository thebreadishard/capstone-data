"""Read-only (TASKS 297, fact 6): the network's error on the cations of the selection set, per cation, over the three seeds of the
v1.4 search's winner c07 and of the control c00 — beside what the symmetry check found for that cation (distorted geometry,
imaginary mode in the label)."""
import csv
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
OUT = PLAN / "modules" / "05_support_predictor" / "out" / "v14"
CORPUS = PLAN / "modules" / "05_support_predictor" / "corpus"
sym = {o["id"]: o for o in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))}
names = {r["id"]: r["name"] for r in csv.DictReader((CORPUS / "manifest.csv").open(encoding="utf-8"))}
RUNS = {"c07": ["s1a_c07_seleval_seed0", "s1b_c07_seleval_seed1", "s2_c07_seleval_seed2"],
        "c00": ["s1a_c00_control_seleval_seed0", "s1b_c00_control_seleval_seed1", "s2_c00_control_seleval_seed2"]}
first = True
for arm, runs in RUNS.items():
    per: dict[str, list[dict]] = {}
    for run in runs:
        rec = json.loads((OUT / f"E7_rungC_v14{run}.json").read_text(encoding="utf-8"))
        for mol_id, entry in rec["selall"]["per_molecule"].items():
            per.setdefault(mol_id, []).append(entry)
    if first:
        any_entry = next(iter(per.values()))[0]
        print("per-molecule fields:", {k: (str(v)[:40]) for k, v in any_entry.items()})
        first = False
    key = "corrected_freq_rms"
    cat = {i: float(np.mean([e[key] for e in v])) for i, v in per.items() if i.startswith("P3c_")}
    neu = {i: float(np.mean([e[key] for e in v])) for i, v in per.items() if not i.startswith("P3c_")}

    def rms(d: dict[str, float]) -> float:
        return float(np.sqrt(np.mean(np.square(list(d.values())))))

    print(f"\n{arm}: cations {len(cat)} molecules, rms over molecules of the seed-mean {rms(cat):.2f}; neutrals {len(neu)}, {rms(neu):.2f}; "
          f"median cation {np.median(list(cat.values())):.2f}, median neutral {np.median(list(neu.values())):.2f}")
    for i, v in sorted(cat.items(), key=lambda kv: -kv[1]):
        res = json.loads((CORPUS / "molecules" / i / "result.json").read_text(encoding="utf-8"))
        s = sym.get(i, {})
        flags = []
        if s and s["order_cation_0.02"] < s["order_parent_0.02"]:
            flags.append(f"geometry {s['order_parent_0.02']}->{s['order_cation_0.02']}")
        if res["n_imaginary_b3lyp"] or res["n_imaginary_wb97x"]:
            flags.append(f"imaginary b3lyp/wb97x {res['n_imaginary_b3lyp']}/{res['n_imaginary_wb97x']}")
        print(f"  {i} {names[i][:26]:26s} {v:6.2f}  {'; '.join(flags)}")
    without = {i: v for i, v in cat.items() if i != max(cat, key=cat.get)}
    print(f"  without the worst cation: {rms(without):.2f}")
