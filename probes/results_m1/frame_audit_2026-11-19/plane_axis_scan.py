"""Frame audit (19 Nov 2026): how well-defined is the 'molecular normal' (axis of the largest moment of inertia) over the corpus?

The family rule and the anharmonic step's out-of-plane share o read modes along that axis. Where the two largest moments nearly
coincide the axis is fixed only by small asymmetries. Reads geometry.json only. Masses: standard atomic weights.

Usage: python plane_axis_scan.py <corpus molecules>
"""
import json
import sys
from pathlib import Path

import numpy as np

MASS = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "S": 32.06, "CL": 35.45, "BR": 79.904, "B": 10.81, "P": 30.974,
        "SI": 28.085, "I": 126.9}


def main():
    rows = []
    for g_path in sorted(Path(sys.argv[1]).glob("*/geometry.json")):
        g = json.loads(g_path.read_text(encoding="utf-8"))
        m = np.array([MASS[s.upper()] for s in g["symbols"]])
        x = np.asarray(g["coords_bohr"], float)
        x = x - m @ x / m.sum()
        inertia = sum(mm * (np.dot(r, r) * np.eye(3) - np.outer(r, r)) for r, mm in zip(x, m, strict=True))
        ev, R = np.linalg.eigh(inertia)
        planar = float(np.abs(x @ R[:, 2]).max()) < 0.5
        gap = (ev[2] - ev[1]) / ev[2]
        rows.append((gap, planar, g_path.parent.name))
    gaps = np.array([r[0] for r in rows])
    planar = np.array([r[1] for r in rows])
    print(f"{len(rows)} geometries; planar {planar.sum()}, non-planar {(~planar).sum()}")
    for lim in (0.01, 0.05, 0.1):
        print(f"  relative gap of the two largest moments < {lim}: planar {(planar & (gaps < lim)).sum()}, non-planar {(~planar & (gaps < lim)).sum()}")
    print("smallest gaps:", ", ".join(f"{n} {g:.4f}{' planar' if p else ''}" for g, p, n in sorted(rows)[:8]))


if __name__ == "__main__":
    main()
