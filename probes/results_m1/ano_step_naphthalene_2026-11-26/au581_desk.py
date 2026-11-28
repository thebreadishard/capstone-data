"""Desk look at naphthalene's Au 581: every out-of-plane mode's harmonic frequency at five levels beside the measured list,
and the overlap of each ano-pVQZ mode vector with the B3LYP one (is the pairing by order inside a species the same mode?)."""
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
import ano_step_read_naphthalene as N  # noqa: E402
import cc_composite_full_check as CCF  # noqa: E402
import fundamentals_vs_experiment as F  # noqa: E402

held = N.load_held(N.Inputs())
run = PLAN / "probes" / "results_m1" / "ano_step_naphthalene_2026-11-26" / "rows"
M_ano, _, _ = CCF.rows_in_frame(str(run / "rows_mp2_anopvqz.npz"), None, held.sym, held.x0)
corpus = N.Inputs().corpus


def named(H: np.ndarray) -> N.Named:
    """Modes of a Hessian named as the read names a composite's (the composite formula with the MP2 parts cancelling)."""
    return N.harmonic(N.Held(held.sym, held.x0, held.masses, H, held.mp2_dz, held.mp2_tz, {}, {}), held.mp2_dz)


levels = {
    "B3LYP": named(np.load(corpus / "hessian_b3lyp_analytic.npz")["H_projected"]),
    "wB97X": named(np.load(corpus / "hessian_wb97x_analytic.npz")["H_projected"]),
    "MP2/DZ": named(held.mp2_dz),
    "MP2/TZ": named(held.mp2_tz),
    "MP2/ano-QZ": named(M_ano),
    "CC/DZ": named(held.cc_dz),
    "comp TZ": N.harmonic(held, held.mp2_tz),
    "comp ano": N.harmonic(held, M_ano),
}
keys = sorted((k for k in levels["comp ano"].freq if k[0] in N.OUT_OF_PLANE), key=lambda k: k[1])
print("species meas  " + "  ".join(f"{name:>10s}" for name in levels) + "   overlap2(ano,B3LYP)")
ano, b3 = levels["comp ano"], levels["B3LYP"]
for k in keys:
    ov = F.subspace_overlap(ano.V, ano.idx[k], b3.V, b3.idx[k])
    print(f"{k[0]:4s} {k[1]:6.0f}  " + "  ".join(f"{levels[name].freq[k] - k[1]:+10.1f}" for name in levels) + f"   {ov:.2f}")
