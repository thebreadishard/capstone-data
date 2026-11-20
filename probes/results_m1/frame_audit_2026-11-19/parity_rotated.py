"""Frame audit (19 Nov 2026): does aromir's parity classification (mirror through the lab z = 0 plane) hold for a turned molecule
with a linear group? It decides the parity-odd factor's pairs, the fix of the mirror defect. Read-only; stored geometry only.

Usage: python parity_rotated.py <aromir src> <corpus molecules>
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, sys.argv[1])
from aromir.molecule import Geometry  # noqa: E402
from aromir.network import primitives as P  # noqa: E402

CORPUS = Path(sys.argv[2])
SETTINGS = P.PrimitiveSettings()
rng = np.random.default_rng(5)
for mid in ("A_3100da3761", "A_014f8519af", "A_8448043181"):
    g = json.loads((CORPUS / mid / "geometry.json").read_text(encoding="utf-8"))
    sym = tuple(s.capitalize() for s in g["symbols"])
    x = np.asarray(g["coords_bohr"], float)
    results = []
    for trial in range(6):
        if trial:
            q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
            R = q * np.sign(np.linalg.det(q))
        else:
            R = np.eye(3)
        built = P.build(Geometry(sym, x @ R.T), SETTINGS)
        try:
            odd, _ = P.parities(built)
            lin = [P.kind(p) == P.LINEAR_ANGLE for p in built.internals]
            results.append(f"ok (odd linear rows {int(odd[lin].sum())}/{sum(lin)}, odd total {int(odd.sum())})")
        except ValueError as err:
            results.append(f"REFUSED: {err}")
    print(mid, "| " + " | ".join(results))
