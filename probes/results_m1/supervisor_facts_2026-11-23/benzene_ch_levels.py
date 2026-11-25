"""Read-only: benzene's six C-H stretches at the stored levels, all at the same (B3LYP) geometry — why CC/DZ alone is 138 off."""
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
import e8_cc_locality as L  # noqa: E402

M05 = PLAN / "modules" / "05_support_predictor"
mol = M05 / "corpus" / "molecules" / "A_8448043181"
masses = np.asarray(json.loads((mol / "geometry.json").read_text(encoding="utf-8"))["masses_amu"], float)
R1 = PLAN / "probes" / "results_m1"
for name, path in (("CCSD(T)/cc-pVTZ", R1 / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz"),
                   ("CCSD(T)/cc-pVDZ", R1 / "e8_benzene_ccpvdz_dip_2026-10-03" / "hessian_ccsd_t.npz"),
                   ("composite", M05 / "out" / "composite_full_benzene_2026-10-07.npz"),
                   ("B3LYP/6-31G*", mol / "hessian_b3lyp_analytic.npz"), ("wB97X", mol / "hessian_wb97x_analytic.npz")):
    with np.load(path, allow_pickle=True) as z:
        _, f, _ = L.normal_modes(np.asarray(z["H_projected"], float), masses)
    print(f"{name:18s} " + " ".join(f"{x:7.1f}" for x in np.sort(f)[-6:]))
