"""Check S2 reference Hessians before their force fields finish: imaginary modes and the lowest frequencies (read-only).

    PYTHONPATH=/root/dpir_s2/src python check_ref_hessian.py /root/s2/<id>/G/refhess [...]
"""
import sys

import numpy as np
from dpir import qff

for d in sys.argv[1:]:
    recs = qff.load_results(d)
    if not recs:
        print(f"{d}: no record yet")
        continue
    ref = recs[qff.reference_index(recs)]
    try:
        h = qff.harmonic(ref.H, ref.symbols, ref.geom)
        print(f"{d}: minimum; lowest omega {np.round(np.sort(h.omega_cm)[:3], 1).tolist()} cm-1")
    except ValueError as e:
        print(f"{d}: REFUSED — {e}")
