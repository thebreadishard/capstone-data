"""Read-only (TASKS 297, fact 1): which benzene mode carries the composite's largest deviation from full CCSD(T)/cc-pVTZ.
Both stored Hessians are diagonalised (mass-weighted, projected: e8_cc_locality.normal_modes) and the composite's modes paired with
the CC/TZ ones by eigenvector overlap; the kind of vibration is the corpus rule on the CC/TZ modes. The 6 Oct record
(composite_test2_benzene) gave 4.58 rms over all modes, per kind 3.29 / 4.37 / 7.30 / 3.32, by corrected frequencies in B3LYP's mode
basis — the rms printed here says whether this direct route is the same number."""
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
import e8_cc_locality as L  # noqa: E402

M05 = PLAN / "modules" / "05_support_predictor"
mol = M05 / "corpus" / "molecules" / "A_8448043181"
g = json.loads((mol / "geometry.json").read_text(encoding="utf-8"))
sym, x, masses = [s.capitalize() for s in g["symbols"]], np.asarray(g["coords_bohr"], float), np.asarray(g["masses_amu"], float)


def projected(path: Path) -> np.ndarray:
    with np.load(path) as z:
        return np.asarray(z["H_projected"], float)


tz = projected(PLAN / "probes" / "results_m1" / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz")
comp = projected(M05 / "out" / "composite_full_benzene_2026-10-07.npz")
_, f_tz, V_tz = L.normal_modes(tz, masses)
_, f_c, V_c = L.normal_modes(comp, masses)
fam = L.families(f_tz, V_tz, sym, masses, x)
overlap = np.abs(V_tz.T @ V_c)
# degenerate pairs mix freely, so pair greedily by largest overlap and compare frequencies; within a pair the two are equal anyway
pairs, used = [], set()
for i in np.argsort(-overlap.max(axis=1)):
    j = next(j for j in np.argsort(-overlap[i]) if j not in used)
    used.add(j)
    pairs.append((i, j))
err = np.zeros(len(f_tz))
for i, j in pairs:
    err[i] = f_c[j] - f_tz[i]
print(f"{len(f_tz)} modes; rms {np.sqrt(np.mean(err ** 2)):.2f}; largest |deviation| {np.abs(err).max():.2f}; sorted-frequency rms "
      f"{np.sqrt(np.mean((np.sort(f_c) - np.sort(f_tz)) ** 2)):.2f}, max {np.abs(np.sort(f_c) - np.sort(f_tz)).max():.2f}")
for f in ("ring-ip", "CH-stretch", "CH-oop", "other"):
    sel = fam == f
    print(f"  {f:10s} n {int(sel.sum()):2d} rms {np.sqrt(np.mean(err[sel] ** 2)):.2f}")
print("mode (CC/TZ cm-1) | composite | deviation | kind — the eight largest")
for i in np.argsort(-np.abs(err))[:8]:
    print(f"  {f_tz[i]:8.1f} | {f_tz[i] + err[i]:8.1f} | {err[i]:+6.2f} | {fam[i]}")
