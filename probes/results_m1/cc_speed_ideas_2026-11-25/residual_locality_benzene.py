"""One-off (25 Nov 2026, idea 3 of GoalGathering/notes/Ideas_2026-11-26_Faster_CC.md): how local is the part of the basis-set effect
that the MP2 step misses? On benzene, from Hessians we hold: R = [CCSD(T) − MP2]/cc-pVTZ − [CCSD(T) − MP2]/cc-pVDZ, so that composite + R
is the full CCSD(T)/cc-pVTZ Hessian. R is cut to atom pairs within d bonds and added back; the frequencies are compared with the full
ones (as computed, no geometry term). Benzene is small (the farthest pair is 5 bonds apart), so this is an indication, not a test.

    python residual_locality_benzene.py     (from the plan folder)
"""
import sys
from pathlib import Path

import numpy as np

PLAN = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PLAN / "probes"))
import ano_step_read as A  # noqa: E402

inputs = A.Inputs()
frame, sym, x0 = A.load_frame(inputs)
cc, mp2 = A.conventional_parts(inputs, sym, x0)
composite = cc["dz"] + mp2["tz"] - mp2["dz"]
R = cc["tz"] - composite
n = len(sym)
dist = np.linalg.norm(x0[:, None] - x0[None], axis=2)
bond = (dist > 0) & (dist < np.where(np.add.outer(np.array(sym) == "H", np.array(sym) == "H") > 0, 2.3, 3.0))
hops = np.where(np.eye(n, dtype=bool), 0, np.where(bond, 1, 99))
for k in range(n):                                   # Floyd–Warshall on twelve atoms
    hops = np.minimum(hops, hops[:, [k]] + hops[[k], :])
full = A.named(A.own_modes(frame, cc["tz"])[0], frame.keys)
oop = A.GROUPS["out of plane"]
print(f"largest |R| {np.abs(R).max():.2e}, rms {np.sqrt(np.mean(R ** 2)):.2e} E_h/bohr²; farthest pair {hops.max()} bonds")
print("| pairs kept (bonds) | share of |R|² | rms over 20 vs full CC/TZ | rms out of plane | " + " | ".join(oop) + " |")
print("|---|---|---|---|" + "---|" * len(oop))
for d in (-1, *range(int(hops.max()) + 1)):
    mask = np.kron(hops <= d, np.ones((3, 3), dtype=bool))
    w = A.named(A.own_modes(frame, composite + np.where(mask, R, 0.0))[0], frame.keys)
    diff = {m: w[m] - full[m] for m in A.MODES}
    print(f"| {'none (the composite)' if d < 0 else d} | {np.sum(R[mask] ** 2) / np.sum(R ** 2):.3f} | "
          f"{np.sqrt(np.mean([v ** 2 for v in diff.values()])):.2f} | {np.sqrt(np.mean([diff[m] ** 2 for m in oop])):.2f} | "
          + " | ".join(f"{diff[m]:+.1f}" for m in oop) + " |")
