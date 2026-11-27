"""HCN in the ano-pVDZ file through pyscf (TASKS 328): RHF and frozen-core CCSD(T) energies, to compare with psi4's on the same
file's psi4 form; the basis given as the file's path (as a runner's --basis would) and element by element. Runs in WSL.

    python hcn_ano_pyscf.py <basis file, NWChem format>
"""
import sys

from pyscf import cc, gto, scf

ATOMS = "H 0 0 -2.0; C 0 0 0; N 0 0 2.2"   # bohr

by_element = gto.M(atom=ATOMS, unit="Bohr", basis={s: gto.basis.load(sys.argv[1], s) for s in "HCN"}, verbose=0)
mol = gto.M(atom=ATOMS, unit="Bohr", basis=sys.argv[1], verbose=0)
print(f"functions: by path {mol.nao}, element by element {by_element.nao}")
mf = scf.RHF(mol)
mf.conv_tol = 1e-12
mf.kernel()
mycc = cc.CCSD(mf, frozen=2)
mycc.conv_tol = 1e-11
mycc.conv_tol_normt = 1e-9
mycc.kernel()
e_t = mycc.ccsd_t()
print(f"pyscf nao {mol.nao} scf {mf.e_tot:.10f} ccsd {mycc.e_tot:.10f} ccsd(t) {mycc.e_tot + e_t:.10f}")
