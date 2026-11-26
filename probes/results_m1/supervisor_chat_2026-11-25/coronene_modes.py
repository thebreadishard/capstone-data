"""Read-only: what coronene's two modes with the large VPT2 shift are (harmonic 807.1 and 642.9 cm-1 at B3LYP/6-31G*): degeneracy,
out-of-plane share, hydrogen share, characters under inversion and the six-fold rotation, from the reference Hessian of the QFF run."""
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
sys.path.insert(0, str(PLAN / "src"))
import e8_cc_locality as L  # noqa: E402
from dpir.symmetry import point_group_ops  # noqa: E402
from qc_common import project_tr  # noqa: E402

ref = json.loads((PLAN / "probes/results_m1/routea_server_2026-11-10/routea/coronene/G/ref.json").read_text(encoding="utf-8"))
print("molecule keys:", list(ref["molecule"]))
sym = [s.capitalize() for s in ref["molecule"]["symbols"]]
x = np.asarray(ref["molecule"]["geometry"], float).reshape(-1, 3)
masses = np.array([{"C": 12.0, "H": 1.00782503223}[s] for s in sym])
H = project_tr(np.asarray(ref["return_result"], float).reshape(3 * len(sym), -1), masses, x)[0]
_, freq, V = L.normal_modes(H, masses)
ops = point_group_ops(sym, x)
normal = np.linalg.svd(x - x.mean(axis=0))[2][-1]
inv = next(o for o in ops if abs(np.trace(o[0]) + 3) < 1e-3)
c6 = next(o for o in ops if np.linalg.det(o[0]) > 0 and abs(np.trace(o[0]) - 2) < 1e-3)
c2 = next(o for o in ops if np.linalg.det(o[0]) > 0 and abs(np.trace(o[0]) + 1) < 1e-3 and abs(normal @ o[0] @ normal - 1) < 1e-3)
is_h = np.array([s == "H" for s in sym])
print(f"{len(sym)} atoms, {len(ops)} operations")
for target in (807.1, 642.9):
    k = int(np.argmin(np.abs(freq - target)))
    v = V[:, k].reshape(-1, 3)

    def ch(op):
        R, perm = op
        moved = np.zeros_like(v)
        moved[np.array(perm)] = v @ R.T
        return float(np.sum(v * moved))

    amp = np.sum(v ** 2, axis=1)
    print(f"mode {freq[k]:.1f}: degeneracy {int(np.sum(np.abs(freq - freq[k]) < 1.0))}, out-of-plane share {np.sum((v @ normal) ** 2):.3f}, "
          f"hydrogen share (mass-weighted) {amp[is_h].sum():.2f}, characters i {ch(inv):+.2f}, C6 {ch(c6):+.2f}, C2(z) {ch(c2):+.2f}; "
          f"neighbours {np.round(np.sort(freq[np.argsort(np.abs(freq - freq[k]))[:4]]), 1)}")
    z = v @ normal
    hz = z[is_h]
    print(f"   H out-of-plane displacements, signs around the rim: {''.join('+' if t > 0 else '-' for t in hz[np.argsort(np.arctan2(*(x[is_h] - x.mean(0))[:, :2].T))])}"
          f"; largest carbon amplitude / largest hydrogen amplitude {np.abs(z[~is_h]).max() / np.abs(hz).max():.2f}")
