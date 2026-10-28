"""Scratch diagnostic (28 Oct): does psi4's grid standard orientation jump between benzene's reference and its displaced points?
psi4 1.10 cubature.cc orients every atomic grid by the principal axes of the nuclear-charge second moment; benzene at q = 0 is a
symmetric top (in-plane axes from a 'best atom' rule), any displacement makes it asymmetric (in-plane axes from a near-degenerate
eigenvector pair). STO-3G, 99/590 unpruned, DEBUG 1 prints the symmetry type per grid build. A jump shows as E(+-0.001) - E(0) far
above omega q^2 / 2 (about 3e-9 E_h)."""
import os
import sys

PLAN = "/mnt/c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline"
sys.path[:0] = [PLAN + "/probes", PLAN + "/src"]
import psi4  # noqa: E402
from qff_energy_route import harmonic, load_results, reference_index  # noqa: E402

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
REF = PLAN + "/probes/results_m1/s1tz_gridcheck_2026-10-28/s1tz_gridcheck/benzene/coarse"
recs = load_results(REF)
ref = recs[reference_index(recs)]
harm = harmonic(ref.H, ref.symbols, ref.geom)
geom0 = ref.geom.reshape(-1, 3)
psi4.core.set_output_file(os.path.join(OUT, "psi4.log"), False)
psi4.set_num_threads(8)
psi4.set_memory("3 GB")
psi4.set_options({"basis": "sto-3g", "scf_type": "direct", "e_convergence": 1e-11, "d_convergence": 1e-8, "dft_radial_points": 99,
                  "dft_spherical_points": 590, "dft_pruning_scheme": "none", "debug": 1})


def energy(geom):
    atoms = [f"{s} {x:.12f} {y:.12f} {z:.12f}" for s, (x, y, z) in zip(ref.symbols, geom, strict=True)]
    e = psi4.energy("b3lyp", molecule=psi4.geometry("\n".join(["units bohr", "no_reorient", "no_com", "symmetry c1", *atoms])))
    psi4.core.clean()
    return float(e)


e0 = energy(geom0)
print(f"ref E = {e0:.12f}", flush=True)
for i in (11, 10):
    for q in (0.001, -0.001, 0.1, -0.1):
        e = energy(geom0 + q * harm.A[:, i].reshape(-1, 3))
        print(f"mode {i} q {q:+.3f}: E - E0 = {e - e0:+.3e} E_h", flush=True)
