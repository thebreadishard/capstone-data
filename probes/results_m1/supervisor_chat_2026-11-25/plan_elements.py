"""Read-only: which elements the 167 planned reference molecules contain, and the same for the 23 already carried and for the
122 staged for the next batch."""
import csv
import json
from collections import Counter
from pathlib import Path

from rdkit import Chem

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
M05 = PLAN / "modules" / "05_support_predictor"
smiles = {r["id"]: r["smiles"] for r in csv.DictReader((M05 / "corpus" / "manifest.csv").open(encoding="utf-8"))}
plan = json.loads((M05 / "out" / "anchor_plan" / "count_n167.json").read_text(encoding="utf-8"))
ids = [i for v in plan["chosen"].values() for i in v]
carried = [e["mol_id"] for e in json.loads((M05 / "out" / "ANCHORS_STATUS.json").read_text(encoding="utf-8"))["anchors"] if e["status"] == "carried"]
wave2 = [line.split("|")[0] for p in (PLAN / "probes/results_m1/anchor_waves_2026-11-23").glob("anc*/wave2.txt") for line in p.read_text().splitlines() if line]


def count(group: list[str]) -> str:
    els, halogen, chnos = Counter(), 0, 0
    for i in group:
        e = {a.GetSymbol() for a in Chem.AddHs(Chem.MolFromSmiles(smiles[i])).GetAtoms()}
        for x in e:
            els[x] += 1
        halogen += bool(e & {"F", "Cl"})
        chnos += e <= {"C", "H", "N", "O", "S"}
    return (f"{len(group)} molecules: only C/H/N/O/S {chnos}, with F or Cl {halogen}; per element "
            + ", ".join(f"{k} {v}" for k, v in sorted(els.items()) if k not in "CH"))


print("plan of 167:", count(ids))
print("carried now:", count(carried))
print("next batch :", count(wave2))
print("contexts of the plan:", {k: len(v) for k, v in plan["chosen"].items()})
