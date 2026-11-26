"""Read-only: carbonyl groups among the 1,082 neutral training molecules and among the planned and carried reference molecules."""
import csv
import json
from pathlib import Path

import torch
from rdkit import Chem

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
M05 = PLAN / "modules" / "05_support_predictor"
rows = {r["id"]: r for r in csv.DictReader((M05 / "corpus" / "manifest.csv").open(encoding="utf-8"))}
ckpt = torch.load(M05 / "out" / "v14" / "E7_rungC_v14s3clean_c00_control_release_model_n1132_seed0.pt", map_location="cpu", weights_only=False)
train = [i for i in ckpt["train_ids"] if rows[i]["layer"] != "P3c"]
plan = [i for v in json.loads((M05 / "out" / "anchor_plan" / "count_n167.json").read_text(encoding="utf-8"))["chosen"].values() for i in v]
carried = [e["mol_id"] for e in json.loads((M05 / "out" / "ANCHORS_STATUS.json").read_text(encoding="utf-8"))["anchors"] if e["status"] == "carried"]
PATTERNS = {"any C=O": "[CX3]=[OX1]", "aldehyde CHO": "[CX3H1](=O)[#6]", "carboxylic acid": "[CX3](=O)[OX2H1]", "amide": "[CX3](=O)[NX3]",
            "ketone C(=O) between two carbons": "[#6][CX3](=O)[#6]", "C=O carbon inside a ring (quinone-like)": "[CX3;R](=O)",
            "ester": "[CX3](=O)[OX2][#6]"}
for label, group in (("training neutrals", train), ("plan of 167", plan), ("carried references", carried)):
    mols = [Chem.MolFromSmiles(rows[i]["smiles"]) for i in group]
    print(f"{label} ({len(group)}): " + "; ".join(
        f"{name} {sum(m.HasSubstructMatch(Chem.MolFromSmarts(s)) for m in mols)}" for name, s in PATTERNS.items()))
