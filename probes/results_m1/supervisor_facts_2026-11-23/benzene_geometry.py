"""Read-only (TASKS 300): at which geometry was our CCSD(T)/cc-pVTZ Hessian of benzene computed? The stored CC gradient there, and
the bond lengths against the corpus (B3LYP) geometry."""
import json
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
BOHR = 0.529177210903
g = json.loads((PLAN / "modules/05_support_predictor/corpus/molecules/A_8448043181/geometry.json").read_text(encoding="utf-8"))
x_corpus = np.asarray(g["coords_bohr"], float)
for name in ("e8_benzene_ccpvtz_oop_2026-10-03", "e8_benzene_ccpvdz_dip_2026-10-03"):
    with np.load(PLAN / "probes" / "results_m1" / name / "hessian_ccsd_t.npz", allow_pickle=True) as z:
        x, grad = np.asarray(z["coords_bohr"], float), np.asarray(z["gradient"], float).reshape(-1, 3)
    d = np.linalg.norm(x[:, None] - x[None], axis=-1) * BOHR
    cc = sorted(d[i, j] for i in range(6) for j in range(i + 1, 6))[:6]
    ch = [min(d[i, j] for j in range(6)) for i in range(6, 12)]
    centre = x.mean(axis=0)
    radial = [float(grad[i] @ (x[i] - centre) / np.linalg.norm(x[i] - centre)) for i in range(12)]
    print(f"{name}: same coordinates as the corpus geometry: {np.allclose(x, x_corpus, atol=1e-6)}; r(CC) {np.mean(cc):.4f} A, "
          f"r(CH) {np.mean(ch):.4f} A; CC gradient max |g| {np.abs(grad).max():.2e} Eh/bohr, radial on C {np.mean(radial[:6]):+.2e}, "
          f"on H {np.mean(radial[6:]):+.2e}")
