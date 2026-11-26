"""How many rows benzene's own plan has (for the run's estimate): python plan_rows.py, from the plan folder; no psi4 needed."""
import sys
from pathlib import Path

PLAN = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PLAN / "probes"))
import dfmp2_rows  # noqa: E402

plan = dfmp2_rows.plan_from_geometry(str(PLAN / "modules/05_support_predictor/corpus/molecules/A_8448043181/geometry.json"), "cc-pvtz")
print(f"benzene: {len(plan.ks)} rows {list(plan.ks)}, frozen {plan.frozen}, step {plan.step}")
