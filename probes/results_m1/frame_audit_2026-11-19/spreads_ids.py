"""Frame audit (19 Nov 2026): aromir's measure_invariance spreads (rotation, mirror, listings; v1.3's design, seed 7) for corpus ids
outside the registered seven. Read-only; prints per molecule.

Usage: python spreads_ids.py <aromir clone> <release folder> <corpus molecules> <id> [<id> ...]
"""
import sys
import tempfile
from pathlib import Path

import numpy as np

AROMIR = Path(sys.argv[1])
sys.path.insert(0, str(AROMIR / "src"))
sys.path.insert(0, str(AROMIR / "scripts"))
import measure_invariance as MI  # noqa: E402
from aromir import release  # noqa: E402

loaded = release.load(Path(sys.argv[2]))
corpus = Path(sys.argv[3])
rng = np.random.default_rng(MI.SEED)
with tempfile.TemporaryDirectory() as scratch:
    for mid in sys.argv[4:]:
        found = MI.spreads(loaded, MI.stored_molecule(corpus / mid), rng, Path(scratch))
        print(f"{mid}: rotation {found.rotation:.3f}  mirror {found.mirror_image:.3f}  listings {found.xyz_atom_order:.3f}", flush=True)
