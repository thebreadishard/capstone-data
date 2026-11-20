"""Frame audit (19 Nov 2026): which network inputs of aromir change under rotation, mirror image and atom listing.

Read-only on aromir (imported from its clone) and on stored corpus geometries/Hessians; no quantum chemistry.
Per transform, primitives are matched by kind + atoms (mapped back to the stored order); reported per kind:
B rows that flip sign, B rows that turn (neither +1 nor -1), value changes, 2pi jumps of a value, and F entries
whose sign or size changes. Primitives present in one build only are counted (geomeTRIC's choice by atom number).

Usage: python input_invariance.py <aromir src> <corpus molecules> [canonical] [cos]
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, sys.argv[1])
from aromir.molecule import Geometry  # noqa: E402
from aromir.network import primitives as P  # noqa: E402
from aromir.vibrations import project_rigid_motions  # noqa: E402

CORPUS = Path(sys.argv[2])
SETTINGS = P.PrimitiveSettings(angle_choice="canonical" if "canonical" in sys.argv else "geometric",
                               dihedral_encoding="cos" if "cos" in sys.argv else "raw")
MOLS = {"benzene": "A_8448043181", "benzonitrile": "A_3100da3761", "diphenylacetylene": "A_014f8519af",
        "biphenyl (D2, chiral)": "A_fdc27f1bd1", "2-methylnaphthalene": "A_69789470db", "phenol": "B_3db4fe6829",
        "2-F-benzotrifluoride": "B_00d49961e3", "nitrophenanthrene": "A2_19eaf39036"}
KIND = P.PRIMITIVE_KINDS


def rotation(rng):
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    w, x, y, z = q
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def key(prim, atoms_orig):
    """A primitive's identity in the stored atom order, independent of how its atoms are listed."""
    k = P.kind(prim)
    if k == P.BOND:
        return (k, frozenset(atoms_orig))
    if k in (P.ANGLE, P.LINEAR_ANGLE):
        a, b, c = atoms_orig
        return (k, b, frozenset((a, c)), getattr(prim, "axis", None))
    if k == P.DIHEDRAL:
        return (k, min(tuple(atoms_orig), tuple(atoms_orig[::-1])))
    if k == P.OUT_OF_PLANE:
        return (k, atoms_orig[0], frozenset(atoms_orig[1:]))
    return (k, tuple(atoms_orig))


def build(symbols, x, H, perm):
    """Inputs of the geometry listed as x[perm]; keys are in stored indices (perm[i] = stored index of listed atom i)."""
    geo = Geometry(tuple(symbols[p] for p in perm), x[perm])
    idx = (3 * np.asarray(perm)[:, None] + np.arange(3)).ravel()
    Hl = project_rigid_motions(H[np.ix_(idx, idx)], geo)
    built = P.build(geo, SETTINGS)
    F = P.internal_force_constants(Hl, built.wilson_b)
    keys, rows, vals = [], [], []
    N = len(symbols)
    for k in range(len(built.internals)):
        listed = [int(built.order[a]) for a in built.atoms(k)]       # input-geometry indices
        keys.append(key(built.internals[k], [int(perm[a]) for a in listed]))
        row = np.zeros((N, 3))
        row[np.asarray(perm)] = built.wilson_b[k].reshape(N, 3)     # columns back to stored order
        rows.append(row)
        vals.append(built.value(k))
    return dict(keys=keys, B=np.array(rows), F=F, vals=np.array(vals),
                kinds=[P.kind(p) for p in built.internals], prims=built.internals)


def compare(ref, cur, M):
    """M: 3x3 map applied to the stored geometry (rows of B transform as B @ M.T)."""
    pos = {k: i for i, k in enumerate(cur["keys"])}
    if len(pos) != len(cur["keys"]):
        raise RuntimeError("duplicate keys")
    common = [(i, pos[k]) for i, k in enumerate(ref["keys"]) if k in pos]
    out = defaultdict(lambda: defaultdict(float))
    out["_"]["only_one_side"] = (len(ref["keys"]) - len(common)) + (len(cur["keys"]) - len(common))
    sign = {}
    for i, j in common:
        kn = KIND[ref["kinds"][i]]
        e = ref["B"][i] @ M.T
        c = cur["B"][j]
        cosv = float((e * c).sum() / (np.linalg.norm(e) * np.linalg.norm(c) + 1e-300))
        s = 1.0 if cosv > 1 - 1e-6 else (-1.0 if cosv < -1 + 1e-6 else 0.0)
        sign[i] = s
        o = out[kn]
        o["n"] += 1
        o["B_flip"] += s == -1.0
        o["B_turned"] += s == 0.0
        dv = cur["vals"][j] - ref["vals"][i]
        o["val_2pi_jump"] += abs(abs(dv) - 2 * np.pi) < 0.5
        dvs = min(abs(dv), abs(cur["vals"][j] + ref["vals"][i]))      # change beyond a pure sign flip
        o["val_change_beyond_sign_max"] = max(o["val_change_beyond_sign_max"], dvs if abs(abs(dv) - 2 * np.pi) >= 0.5 else 0.0)
        o["val_sign_flip"] += abs(dv) > 1e-6 and abs(cur["vals"][j] + ref["vals"][i]) < 1e-6
    # F entries: signed change, and the change left after the B-row sign convention is undone
    jmap = dict(common)
    for a_i, a_j in common:
        for b_i, b_j in common:
            if b_i < a_i:
                continue
            f0, f1 = ref["F"][a_i, b_i], cur["F"][a_j, b_j]
            if abs(f0) < 1e-5 and abs(f1) < 1e-5:
                continue
            pk = "F:" + "-".join(sorted((KIND[ref["kinds"][a_i]], KIND[ref["kinds"][b_i]])))
            o = out[pk]
            o["n"] += 1
            o["sign_flip"] += f0 * f1 < 0 and abs(f0 + f1) < 1e-6 + 1e-3 * abs(f0)
            o["max_abs_change"] = max(o["max_abs_change"], abs(f1 - f0))
            if sign[a_i] and sign[b_i]:
                o["max_after_sign_undone"] = max(o["max_after_sign_undone"], abs(f1 - sign[a_i] * sign[b_i] * f0))
    del jmap
    return out


def merge(acc, out):
    for k, d in out.items():
        for m, v in d.items():
            acc[k][m] = max(acc[k][m], v)


def main():
    rng = np.random.default_rng(11)
    print(f"settings: {SETTINGS}")
    S = np.diag([1.0, 1.0, -1.0])
    for name, mid in MOLS.items():
        g = json.loads((CORPUS / mid / "geometry.json").read_text(encoding="utf-8"))
        sym = [s.capitalize() for s in g["symbols"]]
        x = np.asarray(g["coords_bohr"], float)
        x = x - x.mean(0)
        with np.load(CORPUS / mid / "hessian_b3lyp_analytic.npz") as z:
            H = np.array(z["H_projected"], float)
        N = len(sym)
        ident = np.arange(N)
        ref = build(sym, x, H, ident)
        res = {}
        for label in ("rotation", "mirror", "listing"):
            acc = defaultdict(lambda: defaultdict(float))
            for _ in range(4 if label != "mirror" else 1):
                if label == "rotation":
                    M = rotation(rng)
                    perm = ident
                elif label == "mirror":
                    M = S
                    perm = ident
                else:
                    M = np.eye(3)
                    perm = rng.permutation(N)
                Rb = np.kron(np.eye(N), M)
                cur = build(sym, x @ M.T, Rb @ H @ Rb.T, perm)
                merge(acc, compare(ref, cur, M))
            res[label] = acc
        print(f"\n### {name} ({mid}, N={N}, K={len(ref['keys'])}, kinds " +
              ", ".join(f"{KIND[k]} {ref['kinds'].count(k)}" for k in sorted(set(ref['kinds']))) + ")")
        for label, acc in res.items():
            parts = [f"only-one-side {int(acc['_']['only_one_side'])}"]
            for kn in KIND:
                if kn in acc:
                    o = acc[kn]
                    bits = [f"{m}={v:.3g}" for m, v in o.items() if m != "n" and v]
                    if bits:
                        parts.append(f"{kn}[{' '.join(bits)}]")
            for kn, o in sorted(acc.items()):
                if kn.startswith("F:"):
                    bits = [f"{m}={v:.2g}" for m, v in o.items() if m != "n" and v > 1e-7]
                    if bits:
                        parts.append(f"{kn}[{' '.join(bits)}]")
            print(f"  {label:8s}: " + "; ".join(parts))


if __name__ == "__main__":
    main()
