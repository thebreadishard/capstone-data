"""Count, per hold-out and family, the molecules with at least one low-level mode of the family (TASKS 266).

    python count_bands.py <folder of hold-out folders> <out.json>

The route without the network: `aromir evaluate` pairs each corrected band one to one with a low-level mode and gives it that
mode's family, so the molecules with a band of a family are those with a low-level mode of it. aromir's own reader and
classifier; read-only, no quantum chemistry.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from aromir import evaluation, families, vibrations


def counts(holdout: Path) -> dict[str, int]:
    """The molecules of one hold-out folder with a mode of each family."""
    present = {family: 0 for family in families.FAMILIES}
    files = sorted(holdout.glob("*.npz"))
    if not files:
        raise SystemExit(f"{holdout}: no molecule in it")
    for path in files:
        reference = evaluation.read(path)
        low = vibrations.vibrational_modes(reference.hessian, reference.geometry)
        for family in set(families.classify(reference.geometry, low)):
            present[family] += 1
    return present | {"n_molecules": len(files)}


def main() -> None:
    folder, out = Path(sys.argv[1]), Path(sys.argv[2])
    record = {holdout.name: counts(holdout) for holdout in sorted(p for p in folder.iterdir() if p.is_dir())}
    for name, row in record.items():
        print(f"({name}) {row}", flush=True)
    tmp = out.with_name(out.name + ".tmp")
    tmp.write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
    os.replace(tmp, out)
    print(f"wrote {out}", flush=True)


if __name__ == "__main__":
    main()
