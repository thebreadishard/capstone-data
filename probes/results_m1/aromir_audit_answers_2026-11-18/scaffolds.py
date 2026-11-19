"""Which trained molecules of v1.3 and v1.4's measurement networks contain fluorene or fluoranthene; the (b) hold-outs' scaffolds."""
import json
import sys
from pathlib import Path

from rdkit import Chem

FLUORENE = Chem.MolFromSmarts("c1ccc2c(c1)Cc1ccccc1-2")
FLUORANTHENE = Chem.MolFromSmiles("c1ccc2c(c1)-c1cccc3cccc-2c13")
rel = Path(sys.argv[1])
for name in ("v1.3/training.json", "v1.4/measurement.json"):
    record = json.loads((rel / name).read_text(encoding="utf-8"))
    for label, ring in (("fluorene", FLUORENE), ("fluoranthene", FLUORANTHENE)):
        hits = [s for s in record["trained_smiles"] if Chem.MolFromSmiles(s).HasSubstructMatch(ring)]
        print(name, label, len(hits), hits[:6])
    held = record["held_out_smiles"]["b"]
    kinds = {"fluorene": 0, "fluoranthene": 0, "neither": 0}
    for s in held:
        m = Chem.MolFromSmiles(s)
        kinds["fluoranthene" if m.HasSubstructMatch(FLUORANTHENE) else "fluorene" if m.HasSubstructMatch(FLUORENE) else "neither"] += 1
    print(name, "held out (b):", len(held), kinds)
v13 = set(json.loads((rel / "v1.3/training.json").read_text(encoding="utf-8"))["held_out_smiles"]["b"])
v14 = set(json.loads((rel / "v1.4/measurement.json").read_text(encoding="utf-8"))["held_out_smiles"]["b"])
print("in v1.4's (b) only:", sorted(v14 - v13), "in v1.3's only:", sorted(v13 - v14))
