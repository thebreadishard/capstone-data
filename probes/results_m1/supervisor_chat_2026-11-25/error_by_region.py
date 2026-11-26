"""TASKS 307 (decision 67): the product's error per spectral region. The measurement networks of the current version and the two
test sets of its product-error record are read as probes/product_error_read.py reads them — H_B3LYP + the seeds' mean ΔH
diagonalised, each band paired to its ωB97X band by mode overlap — and each band is counted in the region of its ωB97X partner's
harmonic frequency. Regions fixed in TASKS 307 before this read: below 500, 500–700, 700–1000, 1000–1700, 1700–2800, above 2800
cm⁻¹. No training, no quantum chemistry: stored analytic Hessians and three checkpoints. Against ωB97X, harmonic.

    python error_by_region.py <out.json>
"""
import json
import sys
from pathlib import Path

import numpy as np

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
import product_error_read as PR  # noqa: E402

M05 = PLAN / "modules" / "05_support_predictor"
RECORD = M05 / "out" / "v14" / "E7_rungC_v14s3clean_c00_control_product_error.json"
EDGES = (0.0, 500.0, 700.0, 1000.0, 1700.0, 2800.0, 1e9)
NAMES = ("below 500", "500-700", "700-1000", "1000-1700", "1700-2800", "above 2800")
FAMILIES = ("ring-ip", "CH-stretch", "CH-oop", "other")

record = json.loads(RECORD.read_text(encoding="utf-8"))
models = tuple(M05 / "out" / "v14" / name for name in record["models"])
missing = [str(m) for m in models if not m.is_file()]
if missing:
    raise SystemExit(f"checkpoints missing: {missing}")
out = {"record": RECORD.name, "models": record["models"], "against": "ωB97X/6-31G*, harmonic", "edges_cm": EDGES[:-1], "sets": {}}
pooled: dict[str, list] = {"freq": [], "err": [], "fam": []}
for set_name, block in record["holdouts"].items():
    ids = sorted(block["label_sha16"])
    freq, err, fam = [], [], []
    for mol_id in ids:
        folder = M05 / "corpus" / "molecules" / mol_id
        lo, hi = PR.label_hessians(folder)
        masses = np.asarray(json.loads((folder / "geometry.json").read_text(encoding="utf-8"))["masses_amu"], float)
        dH, _ = PR.P.correction(models, folder)
        family = np.array(PR.molecule_features(folder, lo=lo, hi=hi)["family"])
        _, w_low, V_low, _ = PR.normal_modes(lo, masses)
        _, w_ref, V_ref, _ = PR.normal_modes(hi, masses)
        _, w_net, V_net, _ = PR.normal_modes(lo + dH, masses)
        partner = PR.RINT.match_modes(V_net, V_ref)
        freq.append(w_ref[partner])
        err.append(w_net - w_ref[partner])
        fam.append(family[PR.RINT.match_modes(V_net, V_low)])
    f, e, g = np.concatenate(freq), np.concatenate(err), np.concatenate(fam)
    for k, v in (("freq", f), ("err", e), ("fam", g)):
        pooled[k].append(v)
    rows = {}
    for name, a, b in zip(NAMES, EDGES[:-1], EDGES[1:]):
        sel = (f >= a) & (f < b)
        rows[name] = {"bands": int(sel.sum()), "rms": float(np.sqrt(np.mean(e[sel] ** 2))) if sel.any() else None,
                      "by_family": {fm: [int((sel & (g == fm)).sum()),
                                         float(np.sqrt(np.mean(e[sel & (g == fm)] ** 2))) if (sel & (g == fm)).any() else None]
                                    for fm in FAMILIES}}
    fam_rms = {fm: float(np.sqrt(np.mean(e[g == fm] ** 2))) for fm in FAMILIES}
    recorded = {fm: block["product"][fm]["rms"] if isinstance(block.get("product", {}).get(fm), dict) else None for fm in FAMILIES}
    out["sets"][set_name] = {"molecules": len(ids), "bands": int(len(e)), "regions": rows, "family_rms_this_read": fam_rms,
                             "family_rms_recorded": recorded}
    print(f"\n== test set {set_name}: {len(ids)} molecules, {len(e)} bands; per family this read {({k: round(v, 2) for k, v in fam_rms.items()})}"
          f"; recorded {recorded}")
    print("region (cm-1)   bands   rms    | ring-ip        CH-stretch     CH-oop         other")
    for name in NAMES:
        r = rows[name]
        cells = "  ".join(f"{n:4d} {'' if v is None else f'{v:5.2f}':>5s}    " for n, v in r["by_family"].values())
        print(f"{name:14s} {r['bands']:5d}  {'' if r['rms'] is None else f'{r['rms']:5.2f}':>5s}  | {cells}")
    aib = (f >= 500) & (f < 3400)
    three = aib & (g != "other")
    print(f"AIB range 500-3400: all {np.sqrt(np.mean(e[aib] ** 2)):.2f} over {int(aib.sum())} bands; the three target kinds "
          f"{np.sqrt(np.mean(e[three] ** 2)):.2f} over {int(three.sum())}; 'other' inside it "
          f"{np.sqrt(np.mean(e[aib & (g == 'other')] ** 2)):.2f} over {int((aib & (g == 'other')).sum())}; "
          f"share of bands within 2 cm-1 in the range: {np.mean(np.abs(e[aib]) <= 2):.3f}")
Path(sys.argv[1]).write_text(json.dumps(out, indent=1), encoding="utf-8")
