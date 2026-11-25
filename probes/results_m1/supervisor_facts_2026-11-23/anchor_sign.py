"""Read-only (TASKS 297, fact 2 on today's registry): per kind of vibration, the first-order shift of B3LYP's modes under the CC
composite's correction (CC − B3LYP) and under the proxy's (ωB97X − B3LYP), per carried anchor — `set3_decompose.anchor_parts`, the
function of the 27 Oct read (one implementation). Labels only: no network is run, so the registered read of the new anchors
(new_anchor_table.py) is not touched. Summary: the median over anchors of the ratio of mean shifts (anchor_price_plan's 'mean
factor'), the centred slope, the correlation, and how many anchors have the two means on opposite sides of zero — for the eleven
anchors carried before 21 Nov, the seven collected on 23 Nov, and all."""
import json
import statistics
import sys
from pathlib import Path

PLAN = Path(r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline")
sys.path.insert(0, str(PLAN / "probes"))
import set3_decompose as SD  # noqa: E402

M05 = PLAN / "modules" / "05_support_predictor"
entries = [e for e in json.loads((M05 / "out" / "ANCHORS_STATUS.json").read_text(encoding="utf-8"))["anchors"] if e["status"] == "carried"]
res = {}
for e in entries:
    tz = PLAN / e["path"]
    parts = SD.anchor_parts(M05 / "corpus" / "molecules" / e["mol_id"], tz, tz)
    res[e["mol_id"]] = {"name": e["name"], "new": "new_anchors_2026-11" in e["path"], **parts}
Path(sys.argv[1]).write_text(json.dumps(res, indent=1), encoding="utf-8")

for fam in ("ring-ip", "CH-stretch", "CH-oop", "other"):
    print(f"\n== {fam}: mean shift cm-1 CC | proxy | ratio | centred slope | corr | n modes")
    for mol_id, r in res.items():
        if fam in r:
            t = r[fam]["total"]
            print(f"  {'*' if r['new'] else ' '} {r['name'][:16]:16s} {t['mean']:+7.2f} | {r[fam]['proxy mean']:+7.2f} | "
                  f"{t['mean'] / r[fam]['proxy mean']:+6.2f} | {t['centred_slope']:+5.2f} | {t['corr']:+5.2f} | {r[fam]['n']}")
    for label, pick in (("eleven before 21 Nov", lambda r: not r["new"]), ("seven of 23 Nov", lambda r: r["new"]), ("all", lambda r: True)):
        rows = [r[fam] for r in res.values() if fam in r and pick(r)]
        if not rows:
            continue
        ratio = [v["total"]["mean"] / v["proxy mean"] for v in rows]
        opposite = sum(1 for v in rows if v["total"]["mean"] * v["proxy mean"] < 0)
        print(f"  {label:22s} n {len(rows):2d}: median ratio {statistics.median(ratio):+.2f}, opposite sign of the mean in {opposite}, "
              f"median centred slope {statistics.median(v['total']['centred_slope'] for v in rows):+.2f}, "
              f"median corr {statistics.median(v['total']['corr'] for v in rows):+.2f}, "
              f"median CC mean {statistics.median(v['total']['mean'] for v in rows):+.1f}, proxy mean {statistics.median(v['proxy mean'] for v in rows):+.1f}")
