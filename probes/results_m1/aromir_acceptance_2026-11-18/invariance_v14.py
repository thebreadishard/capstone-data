"""TASKS 267 / TASKS 269 criterion 3: how far v1.4's answer moves under a rotation, a mirror image and another atom order.

    python invariance_v14.py <corpus molecules folder> <manifest.csv> <out folder> [--only <SMILES>]

The trials of v1.3's record, with aromir's own code and the bundled release (registration GoalGathering/notes/
PreRegistration_2026-11-18_aromir_Acceptance.md):
- the molecules of v1.3's invariance.json, on their stored B3LYP geometry and analytic Hessian: 12 shuffled xyz listings put into
  aromir's canonical order, 8 random rotations, the mirror image (seeded as v1.3's audit script, rng 7);
- the three molecules of v1.3's atom-order spread, five SMILES-writing orders each (heavy atoms in a random order, each hydrogen after
  its heavy atom; seeds 0-4), the correction applied to the reordered input directly.
Writes invariance.json (aromir's Invariance record) and atom_order_spread.json; prints one line per molecule. No quantum chemistry.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path

import numpy as np
from aromir import admission, release, vibrations
from aromir import geometry as geo
from aromir.constants import ANGSTROM_PER_BOHR
from aromir.molecule import Geometry

INVARIANCE_SMILES = ("c1ccccc1", "N#Cc1ccccc1", "c1ccc(-c2ccccc2)cc1", "Cc1ccc2ccccc2c1", "C#Cc1ccccc1", "C(#Cc1ccccc1)c1ccccc1",
                     "Oc1ccccc1")
ORDER_IDS = ("A_541c53d1a5", "A_fdc27f1bd1", "A_ea73419366")
N_SHUFFLES, N_ROTATIONS, N_ORDER_SEEDS = 12, 8, 5
LINEAR = "#"                       # a nitrile or an alkyne: the linear groups whose angle is read against a fixed axis


def load(folder: Path) -> tuple[Geometry, np.ndarray]:
    g = json.loads((folder / "geometry.json").read_text(encoding="utf-8"))
    geometry = Geometry(tuple(s[0].upper() + s[1:].lower() for s in g["symbols"]), np.array(g["coords_bohr"], float))
    with np.load(folder / "hessian_b3lyp_analytic.npz") as z:
        return geometry, np.array(z["H_projected"], float)


def permuted(g: Geometry, h: np.ndarray, order) -> tuple[Geometry, np.ndarray]:
    idx = (3 * np.array(order)[:, None] + np.arange(3)).ravel()
    return g.reordered(list(order)), h[np.ix_(idx, idx)]


def turned(g: Geometry, h: np.ndarray, r: np.ndarray) -> tuple[Geometry, np.ndarray]:
    big = np.kron(np.eye(g.n_atoms), r)
    return Geometry(g.symbols, g.coords_bohr @ r.T), big @ h @ big.T


def corrected(bundled: release.Release, g: Geometry, h: np.ndarray) -> np.ndarray:
    return np.sort(vibrations.vibrational_modes(h + bundled.corrections(g, h).mean, g).wavenumbers)


def rotation(rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    return q * np.sign(np.linalg.det(q))


def xyz_orders(g: Geometry, rng: np.random.Generator, scratch: Path) -> set[tuple[int, ...]]:
    """The distinct canonical orders aromir gives 12 listings of one geometry."""
    orders = set()
    for _ in range(N_SHUFFLES):
        shuffle = rng.permutation(g.n_atoms)
        lines = [str(g.n_atoms), "listing"]
        lines += [f"{g.symbols[k]} " + " ".join(f"{x:.10f}" for x in g.coords_bohr[k] * ANGSTROM_PER_BOHR) for k in shuffle]
        (scratch / "listing.xyz").write_text("\n".join(lines) + "\n", encoding="utf-8")
        canon = geo.canonical_order(admission.parse_xyz(scratch / "listing.xyz"))
        orders.add(tuple(int(shuffle[k]) for k in canon))
    return orders


def smiles_like_order(g: Geometry, rng: np.random.Generator) -> np.ndarray:
    heavy = np.array([i for i, s in enumerate(g.symbols) if s != "H"])
    order = rng.permutation(heavy)
    rank = {int(a): k for k, a in enumerate(order)}
    partner = {h: int(heavy[np.argmin(np.linalg.norm(g.coords_bohr[heavy] - g.coords_bohr[h], axis=1))])
               for h, s in enumerate(g.symbols) if s == "H"}
    return np.concatenate([order, np.array(sorted(partner, key=lambda h: (rank[partner[h]], h)), dtype=int)])


def spreads(bundled: release.Release, g: Geometry, h: np.ndarray, rng: np.random.Generator, scratch: Path) -> dict[str, float]:
    base = corrected(bundled, g, h)
    listed = [corrected(bundled, *permuted(g, h, o)) for o in xyz_orders(g, rng, scratch)]
    order = max(float(np.abs(v - listed[0]).max()) for v in listed)
    turn = max(float(np.abs(corrected(bundled, *turned(g, h, rotation(rng))) - base).max()) for _ in range(N_ROTATIONS))
    mirror = float(np.abs(corrected(bundled, *turned(g, h, np.diag([1.0, 1.0, -1.0]))) - base).max())
    return {"rotation": turn, "mirror_image": mirror, "xyz_atom_order": order}


def spread_record(per: dict[str, dict[str, float]], smiles_of: dict[str, str], name: str, trials: int) -> dict:
    groups = {True: [m for m in per if LINEAR in smiles_of[m]], False: [m for m in per if LINEAR not in smiles_of[m]]}
    out = {"n_trials": trials}
    for linear, key in ((True, "with_linear_group"), (False, "without_linear_group")):
        values = [per[m][name] for m in groups[linear]]
        out[f"{key}_cm"] = round(max(values), 2) if values else None
        out[f"n_{key}"] = len(values)
    return out


def write(path: Path, record: dict) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(record, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, path)
    print(f"wrote {path}", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("corpus", type=Path)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--only", default=None, help="one SMILES of the invariance set, and no atom-order part (the dry run)")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    bundled = release.load(release.bundled())
    by_smiles = {}
    for row in csv.DictReader(a.manifest.open(encoding="utf-8")):
        if (a.corpus / row["id"] / "hessian_b3lyp_analytic.npz").is_file():
            by_smiles.setdefault(row["smiles"], row["id"])
    rng = np.random.default_rng(7)
    per, smiles_of = {}, {}
    for smiles in INVARIANCE_SMILES if a.only is None else (a.only,):
        molecule_id = by_smiles[smiles]
        per[molecule_id] = spreads(bundled, *load(a.corpus / molecule_id), rng, a.out)
        smiles_of[molecule_id] = smiles
        print(f"{smiles:24s} {molecule_id}: " + ", ".join(f"{k} {v:.3f}" for k, v in per[molecule_id].items()) + " cm-1", flush=True)
    source = (f"probes/results_m1/aromir_acceptance_2026-11-18/invariance_v14.py of thebreadishard/udacity-capstone-plan (plan 05), "
              f"aromir's bundled v{bundled.network_version} at {release.bundled()}: " + ", ".join(smiles_of.values()))
    invariance = {"network_version": bundled.network_version,
                  "rotation": spread_record(per, smiles_of, "rotation", N_ROTATIONS),
                  "mirror_image": spread_record(per, smiles_of, "mirror_image", 1),
                  "xyz_atom_order": spread_record(per, smiles_of, "xyz_atom_order", N_SHUFFLES), "source": source,
                  "per_molecule_cm": per}
    write(a.out / "invariance_measured.json", invariance)
    if a.only is not None:
        return
    worst, n_orders = 0.0, N_ORDER_SEEDS
    for molecule_id in ORDER_IDS:
        g, h = load(a.corpus / molecule_id)
        base = corrected(bundled, g, h)
        moved = [float(np.abs(corrected(bundled, *permuted(g, h, smiles_like_order(g, np.random.default_rng(s)))) - base).max())
                 for s in range(n_orders)]
        worst = max(worst, *moved)
        print(f"{molecule_id}: SMILES-writing orders, largest band difference {max(moved):.3f} cm-1", flush=True)
    write(a.out / "atom_order_spread.json", {"max_cm": round(worst, 2), "n_molecules": len(ORDER_IDS), "n_orders": n_orders,
                                             "source": source.replace(": " + ", ".join(smiles_of.values()), ": " + ", ".join(ORDER_IDS))})


if __name__ == "__main__":
    main()
