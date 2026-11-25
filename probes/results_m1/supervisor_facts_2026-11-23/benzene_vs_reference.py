"""Read-only (TASKS 300): our CCSD(T)/cc-pVTZ harmonic frequencies of benzene against the near-basis-set-limit CCSD(T)/ano-pV5Z
values of Semidalas & Martin, Mol. Phys. 2023 (doi 10.1080/00268976.2023.2263593), Table 5, typed in from the paper's text.
Our distinct frequencies are matched to the reference by out-of-plane share and order within it (the out-of-plane ones were
labelled by characters in benzene_oop_levels.py; in-plane ones are matched by sorted order, which the reference's spacing allows)."""
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
import e8_cc_locality as L  # noqa: E402

REF = {  # mode: (symmetry, CCSD(T)/ano-pV5Z, CCSD(T)/ano-pVTZ, out of plane)
    "w1": ("a1g", 1006.6, 1003.3, False), "w2": ("a1g", 3204.3, 3209.9, False), "w3": ("a2g", 1380.5, 1374.9, False),
    "w4": ("b2g", 712.4, 708.4, True), "w5": ("b2g", 1012.4, 1006.8, True), "w6": ("e2g", 611.5, 610.3, False),
    "w7": ("e2g", 3179.6, 3184.6, False), "w8": ("e2g", 1639.3, 1637.0, False), "w9": ("e2g", 1191.8, 1192.3, False),
    "w10": ("e1g", 863.4, 863.6, True), "w11": ("a2u", 683.6, 685.9, True), "w12": ("b1u", 1024.6, 1019.4, False),
    "w13": ("b1u", 3169.9, 3174.4, False), "w14": ("b2u", 1328.6, 1328.3, False), "w15": ("b2u", 1158.4, 1160.5, False),
    "w16": ("e2u", 406.3, 405.8, True), "w17": ("e2u", 987.0, 983.0, True), "w18": ("e1u", 1057.2, 1054.8, False),
    "w19": ("e1u", 1511.3, 1506.6, False), "w20": ("e1u", 3195.1, 3200.7, False)}
OURS_OOP = {"w16": 403.4, "w4": 673.9, "w11": 708.9, "w10": 873.6, "w17": 973.1, "w5": 981.4}   # labelled by characters

M05 = PLAN / "modules" / "05_support_predictor"
g = json.loads((M05 / "corpus" / "molecules" / "A_8448043181" / "geometry.json").read_text(encoding="utf-8"))
x, masses = np.asarray(g["coords_bohr"], float), np.asarray(g["masses_amu"], float)
with np.load(PLAN / "probes" / "results_m1" / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz") as z:
    H = np.asarray(z["H_projected"], float)
_, freq, V = L.normal_modes(H, masses)
normal = np.linalg.svd(x - x.mean(axis=0))[2][-1]
inplane = sorted({round(float(f), 1) for k, f in enumerate(freq) if np.sum((V[:, k].reshape(-1, 3) @ normal) ** 2) < 0.5})
distinct = [inplane[0]]
for f in inplane[1:]:
    if f - distinct[-1] > 1.0:
        distinct.append(f)
ref_in = sorted((v[1], k) for k, v in REF.items() if not v[3])
if len(distinct) != len(ref_in):
    raise SystemExit(f"{len(distinct)} distinct in-plane frequencies of ours against {len(ref_in)} in the reference")
ours = dict(OURS_OOP) | {k: f for f, (_, k) in zip(distinct, ref_in)}
rows = sorted(REF, key=lambda k: int(k[1:]))
print("mode sym   ours(cc-pVTZ)  ano-pV5Z  ours-5Z   ano-pVTZ-5Z")
for k in rows:
    s, r5, r3, oop = REF[k]
    print(f"{k:4s} {s:4s} {ours[k]:9.1f} {r5:10.1f} {ours[k] - r5:+8.1f} {r3 - r5:+10.1f}  {'out of plane' if oop else ''}")
d = np.array([ours[k] - REF[k][1] for k in rows])
oop = np.array([REF[k][3] for k in rows])
print(f"rms ours - ano-pV5Z: all {np.sqrt(np.mean(d ** 2)):.1f}; in-plane {np.sqrt(np.mean(d[~oop] ** 2)):.1f} (max {np.abs(d[~oop]).max():.1f}); "
      f"out-of-plane {np.sqrt(np.mean(d[oop] ** 2)):.1f}")
