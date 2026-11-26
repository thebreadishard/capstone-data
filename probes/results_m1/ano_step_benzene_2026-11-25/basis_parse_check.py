"""Before the launch of ano_step_benzene: does psi4 find and parse every basis and fitting set the lane names, for benzene? No SCF is run;
only the basis objects are built. Run in WSL with PSIPATH set to the folder with ano-pvqz.gbs:
    PSIPATH=<basis/psi> python basis_parse_check.py <corpus geometry.json>
Prints the number of functions per set; exits 1 when a set cannot be built or ano-pVQZ has not cc-pVQZ's count (510 on benzene)."""
import json
import sys

import psi4

psi4.core.be_quiet()
with open(sys.argv[1], encoding="utf-8") as handle:
    geometry = json.load(handle)
atoms = [f"{s.capitalize()} {x:.10f} {y:.10f} {z:.10f}" for s, (x, y, z) in zip(geometry["symbols"], geometry["coords_bohr"], strict=True)]
mol = psi4.geometry("\n".join(["0 1", *atoms, "units bohr", "symmetry c1", "no_reorient", "no_com"]))
psi4.set_options({"puream": True})
ORBITAL = ("cc-pvdz", "cc-pvtz", "cc-pvqz", "roos-ano-tz", "ano-pvqz", "cc-pwcvtz")
FITTING = (("DF_BASIS_SCF", "cc-pvtz-jkfit"), ("DF_BASIS_SCF", "cc-pvqz-jkfit"), ("DF_BASIS_SCF", "cc-pv5z-jkfit"),
           ("DF_BASIS_MP2", "cc-pvqz-ri"), ("DF_BASIS_MP2", "cc-pv5z-ri"), ("DF_BASIS_MP2", "cc-pwcvtz-ri"))
counts = {}
for name in ORBITAL:
    counts[name] = psi4.core.BasisSet.build(mol, "BASIS", name).nbf()
    print(f"orbital {name}: {counts[name]} functions", flush=True)
for key, name in FITTING:
    print(f"fitting {name} ({key}): {psi4.core.BasisSet.build(mol, key, name).nbf()} functions", flush=True)
if counts["ano-pvqz"] != counts["cc-pvqz"]:
    raise SystemExit(f"ano-pvqz has {counts['ano-pvqz']} functions on benzene, cc-pvqz {counts['cc-pvqz']}: not a quadruple-zeta file")
print("=== BASIS PARSE CHECK PASS")
