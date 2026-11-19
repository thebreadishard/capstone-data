"""TASKS 269 criterion 2's three comparisons, as registered (GoalGathering/notes/PreRegistration_2026-11-18_aromir_Acceptance.md).

    python compare_set.py <fixed_set.json> <aromir out folder> <m08 out folder> <corpus molecules folder> <out.json> [--only <name>]

1. same input, two codes: aromir's correction on the pipeline's geometry and B3LYP Hessian (its atom order) against the pipeline's
   stored ΔH, as corrected wavenumbers; passes within 0.01 cm⁻¹ on every band;
2. end to end, B3LYP: each tool's printed B3LYP positions by rank; passes with rms ≤ 1.0 cm⁻¹ and every band above 200 cm⁻¹
   within 2.0 cm⁻¹;
3. end to end, corrected: the same rule on the corrected positions.
Beside them, for a corpus molecule, aromir's corrected positions against the stored ωB97X reference by rank (rms). A molecule
whose folders are not there yet is listed as missing. Run with the interpreter of the aromir install under test.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np
from aromir import release, vibrations
from aromir.molecule import Geometry

SAME_INPUT_CM = 0.01
RMS_CM, BAND_CM, ABOVE_CM = 1.0, 2.0, 200.0


def geometry(folder: Path) -> Geometry:
    g = json.loads((folder / "geometry.json").read_text(encoding="utf-8"))
    return Geometry(tuple(s[0].upper() + s[1:].lower() for s in g["symbols"]), np.array(g["coords_bohr"], float))


def same_input(folder: Path, bundled: release.Release) -> dict:
    """Comparison 1 on the pipeline's folder."""
    g = geometry(folder)
    with np.load(folder / "hessian_b3lyp_analytic.npz") as z:
        hessian = np.array(z["H_projected"], float)
    with np.load(folder / "correction.npz") as z:
        theirs = np.array(z["dH"], float)
    ours = bundled.corrections(g, hessian).mean
    a = vibrations.vibrational_modes(hessian + ours, g).wavenumbers
    b = vibrations.vibrational_modes(hessian + theirs, g).wavenumbers
    worst = float(np.abs(a - b).max())
    return {"max_dH": float(np.abs(ours - theirs).max()), "max_band_cm": round(worst, 5), "passed": worst <= SAME_INPUT_CM}


def by_rank(ours: list[float], theirs: list[float]) -> dict:
    """Comparisons 2 and 3: positions paired by rank."""
    if len(ours) != len(theirs):
        return {"passed": False, "reason": f"{len(ours)} bands against {len(theirs)}"}
    x, y = np.sort(np.array(ours)), np.sort(np.array(theirs))
    d = x - y
    above = np.abs(d[y > ABOVE_CM])
    rms, worst = float(np.sqrt(np.mean(d**2))), float(above.max()) if above.size else 0.0
    return {"rms_cm": round(rms, 3), "max_above_200_cm": round(worst, 3), "max_any_cm": round(float(np.abs(d).max()), 3),
            "passed": rms <= RMS_CM and worst <= BAND_CM}


def against_reference(bands: list[float], folder: Path) -> dict | None:
    """aromir's corrected positions against the stored ωB97X Hessian of the corpus folder, by rank."""
    path = folder / "hessian_wb97x_analytic.npz"
    if not path.is_file():
        return None
    with np.load(path) as z:
        reference = vibrations.vibrational_modes(np.array(z["H_projected"], float), geometry(folder)).wavenumbers
    d = np.sort(np.array(bands)) - np.sort(reference)
    return {"rms_cm": round(float(np.sqrt(np.mean(d**2))), 3), "max_cm": round(float(np.abs(d).max()), 3)}


def bands(path: Path, corrected: str) -> tuple[list[float], list[float]]:
    record = json.loads(path.read_text(encoding="utf-8"))["bands"]
    return [b["b3lyp_cm"] for b in record], [b[corrected] for b in record]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    for name in ("set", "aromir", "m08", "corpus", "out"):
        ap.add_argument(name, type=Path)
    ap.add_argument("--only", default=None)
    a = ap.parse_args()
    bundled = release.load(release.bundled())
    rows, seen = {}, set()
    for k, molecule in enumerate(json.loads(a.set.read_text(encoding="utf-8"))["molecules"]):
        name = molecule.get("id") or f"new{k:02d}"
        if molecule["smiles"] in seen or a.only not in (None, name):
            continue
        seen.add(molecule["smiles"])
        ours, theirs = a.aromir / name / "certificate.json", a.m08 / name / name
        row: dict = {"smiles": molecule["smiles"], "group": molecule["group"]}
        if not (theirs / "certificate.json").is_file():
            row["missing"] = "the pipeline's folder"
        else:
            row["same_input"] = same_input(theirs, bundled)
        if not ours.is_file():
            row.setdefault("missing", "aromir's folder")
        elif "same_input" in row:
            (b3_ours, nn_ours), (b3_theirs, nn_theirs) = bands(ours, "wavenumber_cm"), bands(theirs / "certificate.json", "network_cm")
            row["b3lyp"], row["corrected"] = by_rank(b3_ours, b3_theirs), by_rank(nn_ours, nn_theirs)
            if molecule.get("id"):
                row["against_wb97x"] = against_reference(nn_ours, a.corpus / molecule["id"])
        rows[name] = row
        print(name, json.dumps(row)[:300], flush=True)
    done = [r for r in rows.values() if "missing" not in r]
    record = {"release": str(release.bundled()), "n_molecules": len(rows), "n_compared": len(done),
              "passed": {c: all(r[c]["passed"] for r in done) for c in ("same_input", "b3lyp", "corrected")} if done else None,
              "molecules": rows}
    tmp = a.out.with_name(a.out.name + ".tmp")
    tmp.write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
    os.replace(tmp, a.out)
    print(f"wrote {a.out}: {len(done)} of {len(rows)} compared, passed {record['passed']}", flush=True)


if __name__ == "__main__":
    main()
