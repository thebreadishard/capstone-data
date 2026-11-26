"""The first-order geometry term applied to our benzene reference Hessians (TASKS 301, 310): our full CCSD(T)/cc-pVTZ Hessian and
our composite, both at the B3LYP geometry, corrected to the higher level's own minimum and compared again with CCSD(T)/ano-pV5Z
(Semidalas & Martin 2023, Table 5).

Δω_i = ½ Σ_k φ_iik Δq_k (decision 48): φ the B3LYP/6-31G* cubic constants in reduced normal coordinates (the stored quartic force
field of benzene, level G), Δq the Newton step from the B3LYP geometry to the higher level's minimum, from the stored CCSD(T)/
cc-pVTZ gradient and the Hessian of the level being corrected. The functions are probes/geometry_term_check.py's (`reduced`,
`modes_at_target`, `paired`) and s1_anharmonic_level.newton_step — the route validated on 18 molecules on 1 Nov 2026.

The force field lives at its own B3LYP minimum (pyscf, grid 75/302), the CC Hessians at the corpus geometry (psi4): the CC
Hessian and gradient are carried into the force field's frame by a rigid map of the atoms (found here, checked on the B3LYP
Hessians of the two). Checks printed: the map's largest atom distance; the two B3LYP Hessians' frequencies; the uncorrected
differences, which must repeat benzene_table.txt.

    python benzene_geometry_term.py <out.json>
"""
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
sys.path.insert(0, str(PLAN / "src"))
import geometry_term_check as GT  # noqa: E402
from dpir.qff import harmonic  # noqa: E402
from dpir.symmetry import point_group_ops  # noqa: E402
from s1_anharmonic_level import newton_step  # noqa: E402

M05 = PLAN / "modules" / "05_support_predictor"
R1 = PLAN / "probes" / "results_m1"
G_DIR = R1 / "routea_2026-11-02" / "gate" / "benzene" / "G"
REF = {"ω1": ("a1g", 1006.6), "ω2": ("a1g", 3204.3), "ω3": ("a2g", 1380.5), "ω4": ("b2g", 712.4), "ω5": ("b2g", 1012.4),
       "ω6": ("e2g", 611.5), "ω7": ("e2g", 3179.6), "ω8": ("e2g", 1639.3), "ω9": ("e2g", 1191.8), "ω10": ("e1g", 863.4),
       "ω11": ("a2u", 683.6), "ω12": ("b1u", 1024.6), "ω13": ("b1u", 3169.9), "ω14": ("b2u", 1328.6), "ω15": ("b2u", 1158.4),
       "ω16": ("e2u", 406.3), "ω17": ("e2u", 987.0), "ω18": ("e1u", 1057.2), "ω19": ("e1u", 1511.3), "ω20": ("e1u", 3195.1)}
KEY = {"a1g": (False, True, 2), "a2g": (False, True, 2), "b1u": (False, False, -2), "b2u": (False, False, -2), "e2g": (False, True, -1),
       "e1u": (False, False, 1), "b2g": (True, True, -2), "a2u": (True, False, 2), "e1g": (True, True, 1), "e2u": (True, False, -1)}
OOP = {"b2g", "a2u", "e1g", "e2u"}


def rigid_map(sym_a: list[str], xa: np.ndarray, sym_b: list[str], xb: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """An orthogonal R and a permutation p with R (xa_i − centre) ≈ xb_p[i] − centre for same elements: Kabsch on the carbon ring
    for every start and direction of the ring, the hydrogens placed by nearest position; the best is returned with its largest
    atom distance (bohr)."""
    a, b = xa - xa.mean(0), xb - xb.mean(0)
    ca = [i for i, s in enumerate(sym_a) if s == "C"]
    cb = [i for i, s in enumerate(sym_b) if s == "C"]

    def ring(x: np.ndarray, idx: list[int]) -> list[int]:
        n = np.linalg.svd(x)[2][-1]
        u = x[idx[0]] / np.linalg.norm(x[idx[0]])
        v = np.cross(n, u)
        return sorted(idx, key=lambda i: np.arctan2(x[i] @ v, x[i] @ u))

    ra, rb = ring(a, ca), ring(b, cb)
    best = None
    for shift, step in itertools.product(range(6), (1, -1)):
        target = [rb[(shift + step * k) % 6] for k in range(6)]
        U, _, Vt = np.linalg.svd(a[ra].T @ b[target])
        R = (U @ Vt).T                                   # orthogonal, proper or improper: either carries a Hessian correctly
        moved = a @ R.T
        perm = np.empty(len(sym_a), int)
        for i, s in enumerate(sym_a):
            cand = [j for j, t in enumerate(sym_b) if t == s]
            perm[i] = cand[int(np.argmin([np.linalg.norm(moved[i] - b[j]) for j in cand]))]
        if len(set(perm.tolist())) != len(perm):
            continue
        worst = float(np.linalg.norm(moved - b[perm], axis=1).max())
        if best is None or worst < best[2]:
            best = (R, perm, worst)
    if best is None:
        raise SystemExit("no rigid map between the two geometries")
    return best


def carried(H: np.ndarray, R: np.ndarray, perm: np.ndarray) -> np.ndarray:
    n = len(perm)
    blocks = np.einsum("ac,ikcd,bd->ikab", R, H.reshape(n, 3, n, 3).transpose(0, 2, 1, 3), R)
    out = np.zeros_like(blocks)
    out[np.ix_(perm, perm)] = blocks
    return out.transpose(0, 2, 1, 3).reshape(3 * n, 3 * n)


def species(q: np.ndarray, sym: list[str], x: np.ndarray, masses_sqrt_inv: np.ndarray) -> list[tuple]:
    """Per mode (mass-weighted columns of q): (out of plane, even under inversion, 2 × χ(C6) rounded)."""
    ops = point_group_ops(sym, x)
    normal = np.linalg.svd(x - x.mean(0))[2][-1]
    inv = next(o for o in ops if abs(np.trace(o[0]) + 3) < 1e-3)
    c6 = next(o for o in ops if np.linalg.det(o[0]) > 0 and abs(np.trace(o[0]) - 2) < 1e-3)

    def ch(v: np.ndarray, op) -> float:
        moved = np.zeros_like(v)
        moved[np.array(op[1])] = v @ op[0].T
        return float(np.sum(v * moved))

    out = []
    for k in range(q.shape[1]):
        v = q[:, k].reshape(-1, 3)          # equivalent atoms have equal masses: the characters of the mass-weighted vector are the mode's
        out.append((bool(np.sum((v @ normal) ** 2) > 0.5), ch(v, inv) > 0, round(2 * ch(v, c6))))
    return out


def named(freq: np.ndarray, keys: list[tuple]) -> dict[str, float]:
    """Wilson name → frequency: within a species by order, a degenerate pair averaged."""
    groups: dict[tuple, list[float]] = defaultdict(list)
    for f, k in zip(freq, keys):
        groups[k].append(float(f))
    out = {}
    for sp, key in KEY.items():
        vals = sorted(groups[key])
        if abs(key[2]) == 1:
            vals = [float(np.mean(vals[i:i + 2])) for i in range(0, len(vals), 2)]
        refs = sorted((r, name) for name, (s, r) in REF.items() if KEY[s] == key)
        if len(vals) != len(refs):
            raise SystemExit(f"species {sp}: {len(vals)} modes of ours, {len(refs)} in the reference")
        for f, (_, name) in zip(vals, refs):
            out[name] = f
    return out


sym, x_g, H_g = GT.read_reference(G_DIR)
with np.load(G_DIR / "qff_report.npz") as z:
    omega_ff, phi = z["omega_cm"], z["phi_ijk"]
corpus = json.loads((M05 / "corpus" / "molecules" / "A_8448043181" / "geometry.json").read_text(encoding="utf-8"))
sym_c, x_c = [s.capitalize() for s in corpus["symbols"]], np.asarray(corpus["coords_bohr"], float)
R, perm, worst = rigid_map(sym_c, x_c, [s.capitalize() for s in sym], np.asarray(x_g, float))
print(f"rigid map corpus geometry -> force-field geometry: largest atom distance {worst:.4f} bohr")

hg = harmonic(H_g, sym, x_g)
if np.abs(hg.omega_cm - omega_ff).max() > GT.OMEGA_CHECK_CM:
    raise SystemExit("the force field's reference Hessian does not give the force field's frequencies")
with np.load(M05 / "corpus" / "molecules" / "A_8448043181" / "hessian_b3lyp_analytic.npz") as z:
    Hb = carried(np.asarray(z["H_raw"], float), R, perm)
w_b, q_b = GT.modes_at_target(Hb, sym, x_g, "benzene")
order_b, ov_b = GT.paired(hg.q, q_b)
print(f"B3LYP corpus Hessian carried into the frame against the force field's own: largest |Δω| {np.abs(w_b[order_b] - hg.omega_cm).max():.2f} "
      f"cm-1, smallest mode overlap² {ov_b:.3f}")

with np.load(R1 / "e8_benzene_ccpvtz_oop_2026-10-03" / "hessian_ccsd_t.npz", allow_pickle=True) as z:
    H_tz, g_tz = carried(np.asarray(z["H_raw"], float), R, perm), np.zeros((len(sym), 3))
    g_tz[perm] = np.asarray(z["gradient"], float).reshape(-1, 3) @ R.T
with np.load(M05 / "out" / "composite_full_benzene_2026-10-07.npz", allow_pickle=True) as z:
    H_co = carried(np.asarray(z["H_raw"], float), R, perm)
cubic = np.einsum("iik->ik", phi)
keys_g = species(hg.q, sym, np.asarray(x_g, float), hg.Minvh)
result = {"map_worst_bohr": worst, "gradient_max": float(np.abs(g_tz).max()), "levels": {}}
table: dict[str, dict[str, float]] = {}
for name, H in (("CC/TZ", H_tz), ("composite", H_co)):
    dx = newton_step(np.asarray(x_g, float), g_tz, H)
    dq = GT.reduced(hg, dx)
    shift = 0.5 * cubic @ dq
    w, q = GT.modes_at_target(H, sym, x_g, "benzene")
    order, ov = GT.paired(hg.q, q)
    raw = w[order]
    table[name + " raw"], table[name + " corrected"] = named(raw, keys_g), named(raw + shift, keys_g)
    big = np.argsort(-np.abs(dq))[:3]
    d = np.linalg.norm(dx.reshape(-1, 3), axis=1)
    print(f"{name}: Newton step largest atom displacement {d.max():.4f} bohr ({d.max() * 0.529177:.4f} Å); largest Δq at B3LYP modes "
          + ", ".join(f"{hg.omega_cm[k]:.0f} cm-1: {dq[k]:+.3f}" for k in big) + f"; smallest mode overlap² {ov:.3f}")
    result["levels"][name] = {"raw": table[name + " raw"], "corrected": table[name + " corrected"],
                              "shift_by_b3lyp_mode": {f"{hg.omega_cm[k]:.1f}": float(shift[k]) for k in range(len(shift))}}
names = sorted(REF, key=lambda k: int(k[1:]))
print("\n| trilling | symmetrie | ano-pV5Z | CC/TZ ruw − 5Z | CC/TZ gecorrigeerd − 5Z | composiet ruw − 5Z | composiet gecorrigeerd − 5Z |")
print("|---|---|---|---|---|---|---|")
for n in names:
    s, r = REF[n]
    print(f"| {n} | {s} | {r:.1f} | " + " | ".join(f"{table[c][n] - r:+.1f}" for c in
                                                   ("CC/TZ raw", "CC/TZ corrected", "composite raw", "composite corrected")) + " |")
groups = {"alle 20": names, "CH-strek (4)": [n for n in names if REF[n][1] > 3000], "uit het vlak (6)": [n for n in names if REF[n][0] in OOP],
          "overig in het vlak (10)": [n for n in names if REF[n][1] < 3000 and REF[n][0] not in OOP]}
print()
for col in ("CC/TZ raw", "CC/TZ corrected", "composite raw", "composite corrected"):
    line = "; ".join(f"{g} {np.sqrt(np.mean([(table[col][n] - REF[n][1]) ** 2 for n in ns])):.1f}" for g, ns in groups.items())
    print(f"{col}: rms tegen ano-pV5Z — {line}")
    result.setdefault("rms", {})[col] = {g: float(np.sqrt(np.mean([(table[col][n] - REF[n][1]) ** 2 for n in ns]))) for g, ns in groups.items()}
Path(sys.argv[1]).write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
