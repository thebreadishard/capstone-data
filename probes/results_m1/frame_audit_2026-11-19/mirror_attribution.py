"""Frame audit (19 Nov 2026): split v1.4's mirror-image band spread into its causes (read-only; stored Hessians).

Variants, each against the bands of the molecule as stored (largest |difference|, cm^-1, seed mean):
  full   - the mirror image as aromir builds it (what invariance.json records);
  ideal  - the stored inputs carried through the reflection: positions, Hessian and B reflected, every scalar input kept;
           0 if the encoder is O(3)-equivariant and nothing else differs;
  value  - ideal, with only the primitive value slots of the pair features taken from the mirror build
           (dihedral +pi <-> -pi jumps, sign of odd values);
  gauge  - the full mirror build with the value slots put back from the stored build: the B-row sign flips of odd
           primitives and the signed F_pq the head reads (TASKS 52's class).
Also 'rotation' for one random rotation (linear groups only should move).

Usage: python mirror_attribution.py <aromir src> <release folder> <corpus molecules>
"""
import dataclasses
import json
import sys
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, sys.argv[1])
from aromir import release, vibrations  # noqa: E402
from aromir.molecule import Geometry  # noqa: E402
from aromir.network import inputs, weights  # noqa: E402
from aromir.network import pattern as PT  # noqa: E402

LOADED = release.load(Path(sys.argv[2]))
CORPUS = Path(sys.argv[3])
SETTINGS = LOADED.recipes[0].inputs
MOLS = {"benzene": "A_8448043181", "benzonitrile": "A_3100da3761", "diphenylacetylene": "A_014f8519af",
        "biphenyl": "A_fdc27f1bd1", "2-methylnaphthalene": "A_69789470db", "phenol": "B_3db4fe6829",
        "2-F-benzotrifluoride": "B_00d49961e3", "nitrophenanthrene": "A2_19eaf39036"}
if len(sys.argv) > 4:                     # corpus ids given: read those instead
    MOLS = {mid: mid for mid in sys.argv[4:]}
S =np.diag([1.0, 1.0, -1.0])
W = PT.N_PRIMITIVE_FEATURES + (SETTINGS.primitives.dihedral_encoding == "cossin")
VALUE_COLS = [PT._VALUE_SLOT, W + PT._VALUE_SLOT]  # noqa: SLF001  probe reads the layout


def bands(geo, H, built):
    dh = np.mean([weights.correction(n, built) for n in LOADED.networks], axis=0)
    return np.asarray(vibrations.vibrational_modes(H + dh, geo).wavenumbers)


def moved(geo, H, M):
    blocks = np.kron(np.eye(geo.n_atoms), M)
    return Geometry(geo.symbols, geo.coords_bohr @ M.T), blocks @ H @ blocks.T


def main():
    print(f"release {sys.argv[2]}; inputs {SETTINGS}")
    rng = np.random.default_rng(3)
    for name, mid in MOLS.items():
        g = json.loads((CORPUS / mid / "geometry.json").read_text(encoding="utf-8"))
        geo = Geometry(tuple(s[0].upper() + s[1:].lower() for s in g["symbols"]), np.asarray(g["coords_bohr"], float))
        with np.load(CORPUS / mid / "hessian_b3lyp_analytic.npz") as z:
            H = np.array(z["H_projected"], float)
        ref_in = inputs.build(geo, H, SETTINGS)
        ref = bands(geo, H, ref_in)
        mg, mH = moved(geo, H, S)
        mir_in = inputs.build(mg, mH, SETTINGS)
        if not torch.equal(ref_in.pairs, mir_in.pairs):
            raise RuntimeError(f"{name}: pattern changed under the mirror")
        N = geo.n_atoms
        Bs = (ref_in.wilson_b.reshape(len(ref_in.wilson_b), N, 3) @ torch.tensor(S, dtype=torch.float32)).reshape(len(ref_in.wilson_b), -1)
        ideal = dataclasses.replace(ref_in, positions=mir_in.positions, hessian=mir_in.hessian, wilson_b=Bs)
        pf = ref_in.pair_features.clone()
        pf[:, VALUE_COLS] = mir_in.pair_features[:, VALUE_COLS]
        value = dataclasses.replace(ideal, pair_features=pf)
        pg = mir_in.pair_features.clone()
        pg[:, VALUE_COLS] = ref_in.pair_features[:, VALUE_COLS]
        gauge = dataclasses.replace(mir_in, pair_features=pg)
        q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        R = q * np.sign(np.linalg.det(q))
        rg, rH = moved(geo, H, R)
        out = {"full": bands(mg, mH, mir_in), "ideal": bands(mg, mH, ideal), "value": bands(mg, mH, value),
               "gauge": bands(mg, mH, gauge), "rotation": bands(rg, rH, inputs.build(rg, rH, SETTINGS))}
        print(f"{name:22s} " + "  ".join(f"{k} {np.abs(v - ref).max():6.3f}" for k, v in out.items()), flush=True)


if __name__ == "__main__":
    main()
