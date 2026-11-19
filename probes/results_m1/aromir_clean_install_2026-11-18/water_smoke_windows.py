"""Does pyscf's native Windows wheel compute? Water, B3LYP/6-31G*, energy and an analytic Hessian: seconds, the smoke before a run."""
import time

import numpy as np
import pyscf
from pyscf import dft, gto
from pyscf.hessian import thermo

start = time.time()
mol = gto.M(atom="O 0 0 0.1173; H 0 0.7572 -0.4692; H 0 -0.7572 -0.4692", basis="6-31g*", verbose=0)
mf = dft.RKS(mol, xc="b3lyp").run()
hessian = mf.Hessian().kernel()
modes = thermo.harmonic_analysis(mol, hessian)["freq_wavenumber"]
print(f"pyscf {pyscf.__version__}: energy {mf.e_tot:.8f} Eh, converged {mf.converged}, "
      f"wavenumbers {np.round(np.real(modes), 1).tolist()} cm-1, {time.time() - start:.1f} s", flush=True)
