"""Before a pilot launch (TASKS 320): does psi4 on this machine build ano-pVQZ from the file in PSIPATH for this molecule, with
cc-pVQZ's number of functions, and the fitting sets the rows name? No SCF is run.
    PSIPATH=<basis/psi> python basis_count_check.py <geometry.json> <expected functions>"""
import json
import sys

import psi4

psi4.core.be_quiet()
with open(sys.argv[1], encoding="utf-8") as handle:
    geometry = json.load(handle)
atoms = [f"{s.capitalize()} {x:.10f} {y:.10f} {z:.10f}" for s, (x, y, z) in zip(geometry["symbols"], geometry["coords_bohr"], strict=True)]
mol = psi4.geometry("\n".join(["0 1", *atoms, "units bohr", "symmetry c1", "no_reorient", "no_com"]))
psi4.set_options({"puream": True})
ano = psi4.core.BasisSet.build(mol, "BASIS", "ano-pvqz").nbf()
qz = psi4.core.BasisSet.build(mol, "BASIS", "cc-pvqz").nbf()
jk = psi4.core.BasisSet.build(mol, "DF_BASIS_SCF", "cc-pvqz-jkfit").nbf()
ri = psi4.core.BasisSet.build(mol, "DF_BASIS_MP2", "cc-pvqz-ri").nbf()
print(f"psi4 {psi4.__version__}: ano-pvqz {ano}, cc-pvqz {qz}, cc-pvqz-jkfit {jk}, cc-pvqz-ri {ri} functions on {''.join(geometry['symbols'])}")
if ano != qz or ano != int(sys.argv[2]):
    raise SystemExit(f"ano-pvqz builds {ano} functions; cc-pvqz {qz}, expected {sys.argv[2]}")
print("=== BASIS COUNT CHECK PASS")
