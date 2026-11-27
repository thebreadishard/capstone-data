"""HCN in the ano-pVDZ file through psi4 (TASKS 328): RHF and frozen-core CCSD(T) energies, conventional integrals, to compare
with pyscf's on the same file's NWChem form. Runs in WSL, env vpt2, with PSIPATH on the folder that holds ano-pvdz.gbs.

    python hcn_ano_psi4.py
"""
import psi4

psi4.core.set_output_file("hcn_ano_psi4.out", False)
psi4.set_memory("2 GB")
mol = psi4.geometry("""
units bohr
symmetry c1
no_reorient
no_com
H 0 0 -2.0
C 0 0 0
N 0 0 2.2
""")
psi4.set_options({"basis": "ano-pvdz", "scf_type": "pk", "freeze_core": True, "e_convergence": 1e-12, "d_convergence": 1e-10,
                  "r_convergence": 1e-9, "puream": True})
e = psi4.energy("ccsd(t)")
print(f"psi4 nao {psi4.core.Wavefunction.build(mol, 'ano-pvdz').basisset().nbf()} scf {psi4.variable('SCF TOTAL ENERGY'):.10f} "
      f"ccsd {psi4.variable('CCSD TOTAL ENERGY'):.10f} ccsd(t) {e:.10f}")
