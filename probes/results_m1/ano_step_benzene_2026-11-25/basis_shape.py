"""Read-only: the shape of downloaded NWChem-format basis files (untrusted text: parsed as numbers only) — per element and angular
momentum the number of primitives and of contracted functions — against what an ano-pVnZ set must have (TZ: C [4s3p2d1f],
H [3s2p1d]; QZ: C [5s4p3d2f1g], H [4s3p2d1f])."""
import sys
from collections import defaultdict
from pathlib import Path

EXPECT = {"ano-pvtz": {"H": "3s2p1d", "C": "4s3p2d1f"}, "ano-pvqz": {"H": "4s3p2d1f", "C": "5s4p3d2f1g"}}
for path in map(Path, sys.argv[1:]):
    shape: dict[str, dict[str, list[int]]] = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    el = am = None
    rows = cols = 0
    refs = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        parts = line.split()
        if line.startswith("#") or not parts or parts[0] in ("BASIS", "END"):
            if line.startswith("#") and ("Neese" in line or "Valeev" in line or "J. Chem" in line):
                refs.append(line.strip()[:110])
            continue
        if parts[0].isalpha() and len(parts) == 2:
            if el is not None:
                shape[el][am][0] += rows
                shape[el][am][1] += cols
            el, am, rows, cols = parts[0], parts[1].lower(), 0, 0
            continue
        try:
            [float(p.replace("D", "E")) for p in parts]
        except ValueError:
            print(f"{path.name}: unexpected line {line[:60]!r}")
            continue
        rows += 1
        cols = len(parts) - 1
    if el is not None:
        shape[el][am][0] += rows
        shape[el][am][1] += cols
    name = path.name.split(".")[0]
    for element, by_am in shape.items():
        contracted = "".join(f"{by_am[a][1]}{a}" for a in "spdfgh" if a in by_am)
        prims = "".join(f"{by_am[a][0]}{a}" for a in "spdfgh" if a in by_am)
        ok = EXPECT.get(name, {}).get(element)
        print(f"{name} {element}: primitives ({prims}) -> contracted [{contracted}]  expected [{ok}]  {'OK' if contracted == ok else 'DIFFERENT'}")
    print("   references in the header:", refs[:3] or "none in the header")
