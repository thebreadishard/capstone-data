"""Read-only (TASKS 300): benzene's out-of-plane harmonic modes at every stored level, labelled by their characters under inversion
and the six-fold rotation (a2u: i −1, C6 +1; b2g: i +1, C6 −1; e1g: i +1, pair; e2u: i −1, pair). numpy only."""
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

M05 = PLAN / "modules" / "05_support_predictor"
mol = M05 / "corpus" / "molecules" / "A_8448043181"
g = json.loads((mol / "geometry.json").read_text(encoding="utf-8"))
sym, x, masses = [s.capitalize() for s in g["symbols"]], np.asarray(g["coords_bohr"], float), np.asarray(g["masses_amu"], float)
ops = point_group_ops(sym, x)
normal = np.linalg.svd(x - x.mean(axis=0))[2][-1]
inversion = next((R, p) for R, p in ops if abs(np.trace(R) + 3) < 1e-3)
c6 = next((R, p) for R, p in ops if np.linalg.det(R) > 0 and abs(np.trace(R) - 2) < 1e-3)


def character(v: np.ndarray, op) -> float:
    R, perm = op
    moved = np.zeros_like(v)
    moved[np.array(perm)] = v @ R.T
    return float(np.sum(v * moved))


def oop_modes(H: np.ndarray) -> list[str]:
    _, freq, V = L.normal_modes(H, masses)
    out = []
    for k in np.argsort(freq):
        v = V[:, k].reshape(-1, 3)
        if np.sum((v @ normal) ** 2) < 0.99:
            continue
        ci, c = character(v, inversion), character(v, c6)
        single = np.sum(np.abs(freq - freq[k]) < 1.0) == 1
        label = ("a2u" if ci < 0 else "b2g") if single and abs(abs(c) - 1) < 0.05 and (c > 0) == (ci < 0) else ("e2u" if ci < 0 else "e1g")
        out.append(f"{label} {freq[k]:6.1f}")
    return out


def load(path: Path, key: str = "H_projected") -> np.ndarray:
    with np.load(path, allow_pickle=True) as z:
        H = np.asarray(z[key], float)
    return H if key == "H_projected" else project_tr(H, masses, x)[0]


R1 = PLAN / "probes" / "results_m1"
comp = M05 / "out" / "composite_full_benzene_2026-10-07.npz"
with np.load(comp, allow_pickle=True) as z:
    print("composite npz:", {k: z[k].shape for k in z.files})
levels = {
    "CCSD(T)/cc-pVTZ": load(R1 / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz"),
    "CCSD(T)/cc-pVDZ": load(R1 / "e8_benzene_ccpvdz_dip_2026-10-03" / "hessian_ccsd_t.npz"),
    "composite": load(comp),
    "B3LYP/6-31G* (analytic)": load(mol / "hessian_b3lyp_analytic.npz"),
    "wB97X (analytic)": load(mol / "hessian_wb97x_analytic.npz"),
}
for key, name in (("mp2_dz", "MP2/cc-pVDZ"), ("mp2_tz", "MP2/cc-pVTZ")):
    with np.load(comp, allow_pickle=True) as z:
        if z[key].shape == (36, 36):
            levels[name] = project_tr(np.asarray(z[key], float), masses, x)[0]
for name, H in levels.items():
    print(f"{name:26s} " + " | ".join(oop_modes(H)))
with np.load(R1 / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz", allow_pickle=True) as z:
    print("CC/TZ record:", {k: (str(z[k])[:80] if z[k].ndim == 0 else z[k].shape) for k in ("basis", "step", "frozen", "status", "symmetry_reduced", "symmetry_spread")})
