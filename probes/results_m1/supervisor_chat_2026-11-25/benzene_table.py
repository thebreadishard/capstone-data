"""For the composite page: benzene's twenty distinct harmonic frequencies in our full CCSD(T)/cc-pVTZ Hessian, in our composite
and in B3LYP/6-31G*, all at the B3LYP/6-31G* geometry, beside CCSD(T)/ano-pV5Z and CCSD(T)/ano-pVTZ of Semidalas & Martin, Mol.
Phys. 2023 (doi 10.1080/00268976.2023.2263593), Table 5. Every mode is labelled from its own vector: in or out of the plane, even
or odd under inversion, and its character under the six-fold rotation (±1: non-degenerate, ±0.5: one of a degenerate pair), which
fixes the D6h species up to the 1/2 subscript; within a species the modes are matched to the reference by frequency order.
Prints a Markdown table."""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
sys.path.insert(0, str(PLAN / "src"))
import e8_cc_locality as L  # noqa: E402
from dpir.symmetry import point_group_ops  # noqa: E402

REF = {  # Wilson mode: (symmetry, CCSD(T)/ano-pV5Z, CCSD(T)/ano-pVTZ, out of plane)
    "ω1": ("a1g", 1006.6, 1003.3, False), "ω2": ("a1g", 3204.3, 3209.9, False), "ω3": ("a2g", 1380.5, 1374.9, False),
    "ω4": ("b2g", 712.4, 708.4, True), "ω5": ("b2g", 1012.4, 1006.8, True), "ω6": ("e2g", 611.5, 610.3, False),
    "ω7": ("e2g", 3179.6, 3184.6, False), "ω8": ("e2g", 1639.3, 1637.0, False), "ω9": ("e2g", 1191.8, 1192.3, False),
    "ω10": ("e1g", 863.4, 863.6, True), "ω11": ("a2u", 683.6, 685.9, True), "ω12": ("b1u", 1024.6, 1019.4, False),
    "ω13": ("b1u", 3169.9, 3174.4, False), "ω14": ("b2u", 1328.6, 1328.3, False), "ω15": ("b2u", 1158.4, 1160.5, False),
    "ω16": ("e2u", 406.3, 405.8, True), "ω17": ("e2u", 987.0, 983.0, True), "ω18": ("e1u", 1057.2, 1054.8, False),
    "ω19": ("e1u", 1511.3, 1506.6, False), "ω20": ("e1u", 3195.1, 3200.7, False)}
M05 = PLAN / "modules" / "05_support_predictor"
mol = M05 / "corpus" / "molecules" / "A_8448043181"
g = json.loads((mol / "geometry.json").read_text(encoding="utf-8"))
sym = [s.capitalize() for s in g["symbols"]]
x, masses = np.asarray(g["coords_bohr"], float), np.asarray(g["masses_amu"], float)
normal = np.linalg.svd(x - x.mean(axis=0))[2][-1]
ops = point_group_ops(sym, x)
INV = next(o for o in ops if abs(np.trace(o[0]) + 3) < 1e-3)
C6 = next(o for o in ops if np.linalg.det(o[0]) > 0 and abs(np.trace(o[0]) - 2) < 1e-3)


def character(v: np.ndarray, op) -> float:
    R, perm = op
    moved = np.zeros_like(v)
    moved[np.array(perm)] = v @ R.T
    return float(np.sum(v * moved))


def key_of(v: np.ndarray) -> tuple[bool, bool, int]:
    """(out of plane, even under inversion, twice the C6 character rounded): the species up to the 1/2 subscript."""
    return bool(np.sum((v @ normal) ** 2) > 0.5), character(v, INV) > 0, round(2 * character(v, C6))


def by_species(path: Path) -> dict[tuple, list[float]]:
    with np.load(path, allow_pickle=True) as z:
        _, freq, V = L.normal_modes(np.asarray(z["H_projected"], float), masses)
    out: dict[tuple, list[float]] = defaultdict(list)
    for k in np.argsort(freq):
        out[key_of(V[:, k].reshape(-1, 3))].append(float(freq[k]))
    return {k: (v if abs(k[2]) == 2 else [float(np.mean(v[i:i + 2])) for i in range(0, len(v), 2)]) for k, v in out.items()}


# species key of each reference symmetry: (out of plane, gerade, 2 × χ(C6)); a/b: χ = ±1, e1: +0.5, e2: −0.5
KEY = {"a1g": (False, True, 2), "a2g": (False, True, 2), "b1u": (False, False, -2), "b2u": (False, False, -2), "e2g": (False, True, -1),
       "e1u": (False, False, 1), "b2g": (True, True, -2), "a2u": (True, False, 2), "e1g": (True, True, 1), "e2u": (True, False, -1)}
ref_by_key: dict[tuple, list[tuple[float, str]]] = defaultdict(list)
for name, (s, r5, _r3, _oop) in REF.items():
    ref_by_key[KEY[s]].append((r5, name))
R1 = PLAN / "probes" / "results_m1"
LEVELS = {"CC/TZ": R1 / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz", "composite": M05 / "out" / "composite_full_benzene_2026-10-07.npz",
          "B3LYP": mol / "hessian_b3lyp_analytic.npz"}
values: dict[str, dict[str, float]] = {}
for level, path in LEVELS.items():
    mine = by_species(path)
    vals = {}
    for key, refs in ref_by_key.items():
        if len(mine.get(key, [])) != len(refs):
            raise SystemExit(f"{level}: species {key} has {len(mine.get(key, []))} modes, the reference {len(refs)}")
        for f, (_, name) in zip(sorted(mine[key]), sorted(refs)):
            vals[name] = f
    values[level] = vals
order = sorted(REF, key=lambda k: int(k[1:]))
print("| mode | symmetrie | CCSD(T)/ano-pV5Z (gepubliceerd) | ano-pVTZ − 5Z | onze CCSD(T)/cc-pVTZ − 5Z | onze composiet − 5Z | B3LYP/6-31G* − 5Z | uit het vlak |")
print("|---|---|---|---|---|---|---|---|")
for k in order:
    s, r5, r3, oop = REF[k]
    print(f"| {k} | {s} | {r5:.1f} | {r3 - r5:+.1f} | {values['CC/TZ'][k] - r5:+.1f} | {values['composite'][k] - r5:+.1f} | "
          f"{values['B3LYP'][k] - r5:+.1f} | {'ja' if oop else ''} |")
for level in LEVELS:
    d = np.array([values[level][k] - REF[k][1] for k in order])
    oop = np.array([REF[k][3] for k in order])
    ch = np.array([REF[k][1] > 3000 for k in order])
    rest = ~oop & ~ch
    print(f"{level}: rms tegen ano-pV5Z — alle 20: {np.sqrt(np.mean(d ** 2)):.1f}; CH-strek (4): {np.sqrt(np.mean(d[ch] ** 2)):.1f}; "
          f"uit het vlak (6): {np.sqrt(np.mean(d[oop] ** 2)):.1f}; overig in het vlak (10): {np.sqrt(np.mean(d[rest] ** 2)):.1f}")
