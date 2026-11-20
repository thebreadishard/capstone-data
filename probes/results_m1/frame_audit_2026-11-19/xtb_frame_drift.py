"""Frame audit (19 Nov 2026): does the GFN2-xTB minimum keep the B3LYP reference's frame? (read-only; stored ref.json pairs)

The anharmonic step matches xtb modes to B3LYP modes by the overlap of Cartesian mass-weighted vectors, with no alignment.
For each stored X/refstub/ref.json, the G reference it was started from is looked up, and the rigid rotation that best maps G's
centred geometry onto X's (Kabsch, mass-weighted) is reported: its angle, and the rms displacement it removes.

Usage: python xtb_frame_drift.py <PLAN root>
"""
import json
import sys
from pathlib import Path

import numpy as np

MASS = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "S": 32.06, "CL": 35.45, "Cl": 35.45}


def geometry(path):
    mol = json.loads(path.read_text(encoding="utf-8"))["molecule"]
    return list(mol["symbols"]), np.array(mol["geometry"], float).reshape(-1, 3)


def reference_for(x_ref):
    mol_dir = x_ref.parents[2]          # .../<name>/X/refstub/ref.json -> .../<name>
    name = mol_dir.name
    for up in list(x_ref.parents)[2:7]:
        for cand in (up / "G" / "ref.json", up / name / "G" / "ref.json"):
            if cand.is_file():
                return cand
        hits = [p for p in up.glob(f"**/{name}/G/ref.json") if "refstub" not in p.parts]
        if hits:
            return hits[0]
    return None


def main():
    root = Path(sys.argv[1])
    rows = []
    for x_ref in sorted(root.glob("probes/results_m1/**/X/refstub/ref.json")):
        g_ref = reference_for(x_ref)
        if g_ref is None:
            continue
        sg, xg = geometry(g_ref)
        sx, xx = geometry(x_ref)
        if [s.upper() for s in sg] != [s.upper() for s in sx]:
            continue
        m = np.array([MASS.get(s, MASS.get(s.capitalize(), 12.0)) for s in sg])
        cg = xg - m @ xg / m.sum()
        cx = xx - m @ xx / m.sum()
        U, _, Vt = np.linalg.svd((cg * m[:, None]).T @ cx)
        d = np.sign(np.linalg.det(U @ Vt))
        R = U @ np.diag([1, 1, d]) @ Vt                  # cg @ R ~ cx
        angle = np.degrees(np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)))
        before = np.sqrt((m * ((cx - cg) ** 2).sum(1)).sum() / m.sum())
        after = np.sqrt((m * ((cx - cg @ R) ** 2).sum(1)).sum() / m.sum())
        rows.append((angle, before, after, str(x_ref.relative_to(root))))
    print(f"{len(rows)} xtb minima with their B3LYP reference; angle of the best rigid rotation G -> X (deg), "
          "mass-weighted rms displacement before / after removing it (bohr)")
    for angle, before, after, path in sorted(rows, reverse=True)[:12]:
        print(f"{angle:9.4f}  {before:.4f} / {after:.4f}  {path}")
    angles = np.array([r[0] for r in rows])
    if len(angles):
        print(f"median {np.median(angles):.4f} deg, max {angles.max():.4f} deg, > 1 deg: {(angles > 1).sum()}")


if __name__ == "__main__":
    main()
