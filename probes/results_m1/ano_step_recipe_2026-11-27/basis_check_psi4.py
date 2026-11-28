"""The downloaded ano-pVQZ file with N, O and S (TASKS 320, step 1), in psi4: function counts against cc-pVQZ and the conventional
SCF and MP2 energies of a four-atom molecule that holds H, N, O and S (HSNO, a fixed geometry in bohr, not optimised), for the
comparison with pyscf in basis_check_pyscf.py. Run in WSL with PSIPATH set to the folder with ano-pvqz.gbs:
    PSIPATH=<basis/psi> python basis_check_psi4.py
The same psi4 call with a user-supplied basis as tests/psithon2 (PSIPATH); energies as tests/scf1 and tests/mp2-1."""
import psi4

ATOMS = ("S 0.00 0.00 0.00", "H 2.53 0.00 0.00", "N -0.76 3.40 0.00", "O 1.13 4.54 0.00")

psi4.core.be_quiet()
psi4.set_memory("2 GB")
psi4.set_num_threads(4)
mol = psi4.geometry("\n".join(["0 1", *ATOMS, "units bohr", "symmetry c1", "no_reorient", "no_com"]))
psi4.set_options({"puream": True, "scf_type": "pk", "mp2_type": "conv", "freeze_core": False,
                  "e_convergence": 1e-11, "d_convergence": 1e-10})
counts = {name: psi4.core.BasisSet.build(mol, "BASIS", name).nbf() for name in ("cc-pvqz", "ano-pvqz")}
print(f"functions on HSNO: cc-pvqz {counts['cc-pvqz']}, ano-pvqz {counts['ano-pvqz']}", flush=True)
if counts["ano-pvqz"] != counts["cc-pvqz"]:
    raise SystemExit("ano-pvqz has not cc-pvqz's number of functions: not the quadruple-zeta file for these elements")
psi4.set_options({"basis": "ano-pvqz"})
e_mp2, wfn = psi4.energy("mp2", return_wfn=True)
print(f"psi4 {psi4.__version__} SCF {wfn.variable('SCF TOTAL ENERGY'):.10f} MP2 {e_mp2:.10f}", flush=True)
