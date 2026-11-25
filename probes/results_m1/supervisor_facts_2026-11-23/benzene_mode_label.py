"""Read-only: the D6h label of benzene's CCSD(T)/cc-pVTZ mode at 709 cm-1, from its characters under the point group's operations
(dpir.symmetry.point_group_ops on the corpus geometry). For a non-degenerate mode v the character of (R, perm) is v · (op v), with
(op v)[perm[i]] = R v[i]. The out-of-plane candidates: a2u (i −1, C6 +1, σh −1) and b2g (i +1, C6 −1, σh −1). numpy only."""
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
sys.path.insert(0, str(PLAN / "src"))
import e8_cc_locality as L  # noqa: E402
from dpir.symmetry import point_group_ops  # noqa: E402

M05 = PLAN / "modules" / "05_support_predictor"
g = json.loads((M05 / "corpus" / "molecules" / "A_8448043181" / "geometry.json").read_text(encoding="utf-8"))
sym, x, masses = [s.capitalize() for s in g["symbols"]], np.asarray(g["coords_bohr"], float), np.asarray(g["masses_amu"], float)
with np.load(PLAN / "probes" / "results_m1" / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz") as z:
    H = np.asarray(z["H_projected"], float)
_, freq, V = L.normal_modes(H, masses)
ops = point_group_ops(sym, x)
centred = x - x.mean(axis=0)
normal = np.linalg.svd(centred)[2][-1]
print(f"{len(ops)} operations; modes within 1 cm-1 of each other count as degenerate")


def kind(R: np.ndarray) -> str:
    det, tr = np.linalg.det(R), np.trace(R)
    along = abs(float(normal @ R @ normal))
    if det > 0:
        if abs(tr - 3) < 1e-3:
            return "E"
        angle = round(float(np.degrees(np.arccos(np.clip((tr - 1) / 2, -1, 1)))))
        return f"C{round(360 / angle)}" + ("(z)" if along > 0.99 else "'")
    if abs(tr + 3) < 1e-3:
        return "i"
    if abs(tr - 1) < 1e-3:
        return "sigma_h" if along > 0.99 else "sigma_v/d"
    angle = round(float(np.degrees(np.arccos(np.clip((tr + 1) / 2, -1, 1)))))
    return f"S{round(360 / angle)}"


for k in np.argsort(np.abs(freq - 708.9))[:1].tolist() + [int(i) for i in np.where((freq > 600) & (freq < 720))[0]]:
    v = V[:, k].reshape(-1, 3)
    degenerate = int(np.sum(np.abs(freq - freq[k]) < 1.0))
    chars: dict[str, list[float]] = {}
    for R, perm in ops:
        moved = np.zeros_like(v)
        moved[np.array(perm)] = v @ R.T
        chars.setdefault(kind(R), []).append(float(np.sum(v * moved)))
    oop = float(np.sum((v @ normal) ** 2))
    print(f"mode {freq[k]:7.1f} cm-1, degeneracy {degenerate}, out-of-plane share {oop:.3f}: "
          + "; ".join(f"{name} {np.mean(c):+.2f} (n {len(c)}, spread {np.ptp(c):.2f})" for name, c in sorted(chars.items())))
