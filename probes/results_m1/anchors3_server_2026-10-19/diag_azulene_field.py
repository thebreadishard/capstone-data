"""Which stage of _cc_with_lambda fails for azulene in a field of +1e-3 a.u. along x (14 Oct 2026, anchors3, 2 threads)."""
import json
import sys

import numpy as np
from pyscf import cc, gto, lib, scf

lib.num_threads(2)
g = json.load(open("/root/dpir/geoms/azulene/geometry.json"))
mol = gto.M(atom=[(s, x) for s, x in zip(g["symbols"], g["coords_bohr"])], unit="Bohr", basis="cc-pvdz", verbose=0)
F = np.array([1e-3, 0.0, 0.0])
shift = np.einsum("t,tij->ij", F, mol.intor("int1e_r", comp=3))
for label, sh in (("no field", None), ("field x+", shift)):
    mf = scf.RHF(mol)
    mf.conv_tol = 1e-12
    if sh is not None:
        h0 = scf.hf.get_hcore(mol)
        mf.get_hcore = lambda *a, h0=h0, sh=sh, **k: h0 + sh
    e = mf.kernel()
    print(label, "SCF converged", mf.converged, "cycles", getattr(mf, "cycles", "?"), "E", e, flush=True)
if "--ccsd" in sys.argv:
    mycc = cc.CCSD(mf, frozen=10)
    mycc.conv_tol, mycc.conv_tol_normt = 1e-10, 1e-8
    mycc.verbose = 4
    mycc.kernel()
    print("CCSD converged", mycc.converged, flush=True)
