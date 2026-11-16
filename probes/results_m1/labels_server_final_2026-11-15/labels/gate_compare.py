"""The labels server's gate (registration 1): benzene's analytic B3LYP Hessian computed on the server against the laptop's file, max |ΔH| ≤ 1e-6 a.u."""
import sys

import numpy as np

a = np.load("gate/A_8448043181/hessian_b3lyp_analytic.npz")["H_raw"]
b = np.load("gate_benzene_laptop.npz")["H_raw"]
d = float(np.abs(a - b).max())
print(f"GATE benzene B3LYP: max |H_server - H_laptop| = {d:.2e} a.u. ->", "PASS" if d <= 1e-6 else "FAIL")
sys.exit(0 if d <= 1e-6 else 1)
