"""The downloaded ano-pVQZ file with N, O and S (TASKS 320, step 1), in pyscf: per element the contracted functions per angular
momentum against pyscf's own cc-pVQZ, and the SCF and all-electron MP2 energies of the HSNO geometry of basis_check_psi4.py.
    python basis_check_pyscf.py <ano-pvqz.nwchem.txt>
The file is untrusted text: pyscf parses it as numbers (gto.basis.load, as in pyscf's examples/gto/04-input_basis.py)."""
import sys
from collections import Counter

import pyscf
from pyscf import gto, mp, scf

ATOMS = "S 0.00 0.00 0.00; H 2.53 0.00 0.00; N -0.76 3.40 0.00; O 1.13 4.54 0.00"
LETTERS = "spdfgh"


def shape(shells: list) -> str:
    """Contracted functions per angular momentum, like 5s4p3d2f1g."""
    count: Counter[int] = Counter()
    for shell in shells:
        count[shell[0]] += len(shell[1]) - 1
    return "".join(f"{count[l]}{LETTERS[l]}" for l in sorted(count))


path = sys.argv[1]
basis = {}
for element in ("H", "C", "N", "O", "S"):
    basis[element] = gto.basis.load(path, element)
    ours, theirs = shape(basis[element]), shape(gto.basis.load("cc-pvqz", element))
    print(f"{element}: ano-pvqz [{ours}], cc-pvqz [{theirs}]", flush=True)
    if ours != theirs:
        raise SystemExit(f"{element}: the file's contraction is not cc-pVQZ's")
mol = gto.M(atom=ATOMS, unit="Bohr", basis={e: basis[e] for e in "SHNO"}, cart=False, symmetry=False, verbose=0)
mf = scf.RHF(mol)
mf.conv_tol, mf.conv_tol_grad = 1e-12, 1e-8
e_scf = mf.kernel()
if not mf.converged:
    raise SystemExit("SCF not converged")
e_corr = mp.MP2(mf).kernel()[0]
print(f"functions on HSNO: {mol.nao}", flush=True)
print(f"pyscf {pyscf.__version__} SCF {e_scf:.10f} MP2 {e_scf + e_corr:.10f}", flush=True)
