"""Read-only: what the 1,132 training entries of the handed-out network are — pure hydrocarbons, heteroatoms, substituents."""
import csv
import sys
from collections import Counter
from pathlib import Path

import torch
from rdkit import Chem

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
M05 = PLAN / "modules" / "05_support_predictor"
ckpt = torch.load(M05 / "out" / "v14" / "E7_rungC_v14s3clean_c00_control_release_model_n1132_seed0.pt", map_location="cpu", weights_only=False)
ids = list(ckpt["train_ids"])
rows = {r["id"]: r for r in csv.DictReader((M05 / "corpus" / "manifest.csv").open(encoding="utf-8"))}
kinds, sizes, elements = Counter(), [], Counter()
for i in ids:
    r = rows[i]
    if r["layer"] == "P3c":
        kinds["radical cation"] += 1
        continue
    mol = Chem.MolFromSmiles(r["smiles"])
    els = {a.GetSymbol() for a in mol.GetAtoms()}
    for e in els:
        elements[e] += 1
    ring_atoms = {a.GetIdx() for a in mol.GetAtoms() if a.IsInRing()}
    substituted = any(a.GetIdx() not in ring_atoms for a in mol.GetAtoms())
    hetero_ring = any(mol.GetAtomWithIdx(k).GetSymbol() != "C" for k in ring_atoms)
    rings = mol.GetRingInfo().NumRings()
    five = any(len(r_) == 5 for r_ in mol.GetRingInfo().AtomRings())
    if els == {"C"} and not substituted:
        kinds["neutral, pure hydrocarbon ring system (a PAH or benzene)" + (" with a five-ring" if five else "")] += 1
    elif not substituted:
        kinds["neutral, heteroatom in the ring, no substituent"] += 1
    else:
        kinds["neutral, substituted" + (" (heteroatom in the ring too)" if hetero_ring else "")] += 1
    sizes.append((mol.GetNumHeavyAtoms(), rings))
print(len(ids), "entries")
for k, v in kinds.most_common():
    print(f"  {v:5d}  {k}")
print("elements among the neutrals:", dict(elements))
print("rings per neutral:", sorted(Counter(r for _, r in sizes).items()))
