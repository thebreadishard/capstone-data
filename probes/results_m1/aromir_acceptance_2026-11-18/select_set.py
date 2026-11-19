"""TASKS 269 criterion 2: the fixed set of molecules, chosen by rule before any run (registration of 18 Nov 2026).

    python select_set.py <plan folder> <out.json>

- benzene;
- hold-out (a)'s eight molecules as v1.4's evaluation reads them (aromir_v14_release_2026-11-18/holdouts.json);
- five of hold-out (b): the three smallest fluorene children and the two smallest fluoranthene children by atom count, ties by id;
- five molecules the corpus does not hold: the first five of CANDIDATES, in order, that aromir admits and whose canonical SMILES
  is in no row of corpus/manifest.csv.
Read-only; runs aromir's admission only (no quantum chemistry).
"""
from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

from aromir import admission
from aromir.errors import RefusedError
from rdkit import Chem

FLUORENE = Chem.MolFromSmarts("c1ccc2c(c1)Cc1ccccc1-2")
FLUORANTHENE = Chem.MolFromSmiles("c1ccc2c(c1)-c1cccc3cccc-2c13")
CANDIDATES = (  # one each: S, F, Cl, a nitrile, an aza-fused ring, then spares, written down before the check
    "CSc1ccc(C)cc1", "Fc1ccc2ccccc2c1F", "Clc1ccc(Cl)c2ccccc12", "N#Cc1ccc2ccccc2n1", "c1ccc2nc3ccccc3cc2c1",
    "COc1ccc(F)cc1Cl", "Cc1ccc(C#N)cc1F", "Oc1ccc2sccc2c1",
    # added after the first pass found five of the eight in the corpus: more fused and heteroatom rings, in this order
    "N#Cc1ccc(Cl)s1", "Cc1nc2cc(F)ccc2s1", "Clc1ccc2ncccc2c1Cl", "COc1cc2ccccc2cc1C#N", "Cc1ccc2oc(C)nc2c1",
)


def canonical(smiles: str) -> str:
    return Chem.MolToSmiles(Chem.MolFromSmiles(smiles))


def main() -> None:
    plan, out = Path(sys.argv[1]), Path(sys.argv[2])
    module = plan / "modules" / "05_support_predictor"
    rows = list(csv.DictReader((module / "corpus" / "manifest.csv").open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    known = {canonical(r["smiles"]) for r in rows if r["smiles"] and Chem.MolFromSmiles(r["smiles"]) is not None}
    holdouts = json.loads((plan / "probes/results_m1/aromir_v14_release_2026-11-18/holdouts.json").read_text(encoding="utf-8"))
    chosen = [{"group": "benzene", "smiles": "c1ccccc1", "id": next(r["id"] for r in rows if r["smiles"] == "c1ccccc1"
                                                                     and r["id"].startswith("A_"))}]
    chosen += [{"group": "a", "id": i, "smiles": by_id[i]["smiles"]} for i in holdouts["ids"]["a"]]
    b = [(int(by_id[i]["n_atoms"]), i) for i in holdouts["ids"]["b"]]
    for ring, n in ((FLUORENE, 3), (FLUORANTHENE, 2)):
        ours = sorted((atoms, i) for atoms, i in b if Chem.MolFromSmiles(by_id[i]["smiles"]).HasSubstructMatch(ring)
                      and not (ring is FLUORENE and Chem.MolFromSmiles(by_id[i]["smiles"]).HasSubstructMatch(FLUORANTHENE)))
        chosen += [{"group": "b", "id": i, "smiles": by_id[i]["smiles"], "n_atoms": atoms} for atoms, i in ours[:n]]
    new = []
    for smiles in CANDIDATES:
        if len(new) == 5:
            break
        try:
            admission.admit(admission.parse_smiles(smiles))
        except RefusedError as refused:
            print(f"refused {smiles}: {refused}", flush=True)
            continue
        if canonical(smiles) in known:
            print(f"in the corpus: {smiles}", flush=True)
            continue
        new.append({"group": "new", "smiles": smiles})
    if len(new) < 5:
        raise SystemExit(f"only {len(new)} new molecules among the candidates")
    chosen += new
    for row in chosen:
        print(row, flush=True)
    tmp = out.with_name(out.name + ".tmp")
    tmp.write_text(json.dumps({"molecules": chosen}, indent=1) + "\n", encoding="utf-8")
    os.replace(tmp, out)
    print(f"wrote {out}: {len(chosen)} molecules", flush=True)


if __name__ == "__main__":
    main()
