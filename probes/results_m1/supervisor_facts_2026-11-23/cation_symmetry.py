"""Read-only (TASKS 297, fact 5): do the pool's cation Hessians break symmetry? For every done P3c row of the manifest:
- the point group order of the cation's own minimum against its neutral parent's (tolerances 0.02 and 0.10 bohr): a cation whose
  geometry lost operations distorted (Jahn-Teller or a symmetry-broken wavefunction during the optimisation);
- for the operations the cation's geometry does have, how well each Hessian obeys H[P(i),P(k)] = R H[i,k] R^T, as the largest
  violation over the largest element — at a symmetric geometry only a symmetry-broken wavefunction (or noise) violates it;
the parent's Hessian gives the baseline for that number."""
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


def geometry(mol_id: str) -> tuple[list[str], np.ndarray]:
    g = json.loads((CORPUS / "molecules" / mol_id / "geometry.json").read_text(encoding="utf-8"))
    return g["symbols"], np.array(g["coords_bohr"], float)


def hessian(mol_id: str, name: str) -> np.ndarray | None:
    path = CORPUS / "molecules" / mol_id / name
    if not path.is_file():
        return None
    with np.load(path) as z:
        key = "hessian" if "hessian" in z.files else next(k for k in z.files if z[k].ndim == 2 and z[k].shape[0] == z[k].shape[1])
        return np.array(z[key], float)


def violation(H: np.ndarray, ops: list) -> float:
    """Largest |H[P(i),P(k)] − R H[i,k] Rᵀ| over the operations, relative to the largest |H| element."""
    n = H.shape[0] // 3
    blocks = H.reshape(n, 3, n, 3).transpose(0, 2, 1, 3)
    worst = 0.0
    for R, perm in ops:
        p = np.array(perm)
        moved = np.einsum("ab,ikbc,dc->ikad", R, blocks, R)
        worst = max(worst, float(np.abs(blocks[np.ix_(p, p)] - moved).max()))
    return worst / float(np.abs(H).max())


rows = [r for r in csv.DictReader((CORPUS / "manifest.csv").open(encoding="utf-8")) if r["layer"] == "P3c" and r["status"] == "done"]
print(f"{len(rows)} done cation rows; result.json keys of the first: "
      f"{sorted(json.loads((CORPUS / 'molecules' / rows[0]['id'] / 'result.json').read_text(encoding='utf-8')))[:25]}")
out = []
for r in rows:
    parent = re.search(r"parent (\w+)", r["note"])[1]
    sym_c, xyz_c = geometry(r["id"])
    sym_p, xyz_p = geometry(parent)
    rec = {"id": r["id"], "name": r["name"], "n_atoms": len(sym_c)}
    for tol in (0.02, 0.10):
        rec[f"order_parent_{tol}"] = len(point_group_ops(sym_p, xyz_p, tol))
        rec[f"order_cation_{tol}"] = len(point_group_ops(sym_c, xyz_c, tol))
    ops_c, ops_p = point_group_ops(sym_c, xyz_c, 0.02), point_group_ops(sym_p, xyz_p, 0.02)
    for label, name in (("b3lyp", "hessian_b3lyp.npz"), ("wb97x", "hessian_wb97x.npz")):
        Hc, Hp = hessian(r["id"], name), hessian(parent, name)
        rec[f"viol_cation_{label}"] = None if Hc is None or len(ops_c) < 2 else violation(Hc, ops_c)
        rec[f"viol_parent_{label}"] = None if Hp is None or len(ops_p) < 2 else violation(Hp, ops_p)
    out.append(rec)
Path(sys.argv[1]).write_text(json.dumps(out, indent=1), encoding="utf-8")

lost = [o for o in out if o["order_cation_0.02"] < o["order_parent_0.02"]]
lost_loose = [o for o in out if o["order_cation_0.1"] < o["order_parent_0.1"]]
sym_parent = [o for o in out if o["order_parent_0.02"] > 2]
print(f"parents with more than a mirror plane (order > 2): {len(sym_parent)} of {len(out)}")
print(f"cation geometry has fewer operations than its parent: {len(lost)} at 0.02 bohr, {len(lost_loose)} at 0.10 bohr")
for o in sorted(lost, key=lambda o: -o["order_parent_0.02"]):
    print(f"  {o['id']} {o['name'][:28]:28s} parent {o['order_parent_0.02']:2d} -> cation {o['order_cation_0.02']:2d} "
          f"(at 0.10: {o['order_parent_0.1']} -> {o['order_cation_0.1']})")
for label in ("b3lyp", "wb97x"):
    c = np.array([o[f"viol_cation_{label}"] for o in out if o[f"viol_cation_{label}"] is not None])
    p = np.array([o[f"viol_parent_{label}"] for o in out if o[f"viol_parent_{label}"] is not None])
    print(f"{label}: equivariance violation / max|H| — cations n={len(c)} median {np.median(c):.1e} max {c.max():.1e}; "
          f"parents n={len(p)} median {np.median(p):.1e} max {p.max():.1e}")
    for o in sorted((o for o in out if (o[f'viol_cation_{label}'] or 0) > 1e-2), key=lambda o: -o[f"viol_cation_{label}"])[:8]:
        print(f"  {o['id']} {o['name'][:28]:28s} {o[f'viol_cation_{label}']:.1e} (order {o['order_cation_0.02']})")
