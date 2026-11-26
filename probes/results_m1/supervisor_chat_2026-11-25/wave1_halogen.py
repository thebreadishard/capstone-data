"""Read-only: of wave 1's molecules not yet carried, which contain F or Cl (the supervisor, 25 Nov: out of scope), per server."""
import csv
import json
from pathlib import Path

from rdkit import Chem

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
M05 = PLAN / "modules" / "05_support_predictor"
rows = {r["id"]: r for r in csv.DictReader((M05 / "corpus" / "manifest.csv").open(encoding="utf-8"))}
carried = {e["mol_id"] for e in json.loads((M05 / "out" / "ANCHORS_STATUS.json").read_text(encoding="utf-8"))["anchors"] if e["status"] == "carried"}
total = hal = 0
for host in sorted((PLAN / "probes/results_m1/anchor_waves_2026-11-21").glob("anc*")):
    ids = [line.split("|")[0] for line in (host / "wave.txt").read_text().splitlines() if line]
    left = [i for i in ids if i not in carried]
    marks = []
    for i in left:
        els = {a.GetSymbol() for a in Chem.MolFromSmiles(rows[i]["smiles"]).GetAtoms()}
        h = bool(els & {"F", "Cl"})
        hal += h
        marks.append(f"{rows[i]['name']}{' [F/Cl]' if h else ''}")
    total += len(left)
    print(f"{host.name}: {len(left)} left of {len(ids)}: " + "; ".join(marks))
print(f"wave 1 not yet carried: {total}, of which with F or Cl: {hal}")
