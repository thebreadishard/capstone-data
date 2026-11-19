#!/bin/bash
# The v1.4 audit's K1 (decided 18 Nov: the eight decide, the ten are shown beside them and decide nothing): v1.4's measurement
# networks read with `aromir evaluate` (branch acceptance-269) on hold-out (a)'s ten molecules, set 'a' of the measurement run's
# own evaluation record. Stored Hessians only. Run from this folder in WSL.
set -euo pipefail
PLAN=/mnt/c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline
SRC=/home/thebreadishard/aromir-wt-269/src
PY=/home/thebreadishard/aromir_dev/bin/python
export PYTHONPATH=$SRC OMP_NUM_THREADS=2 PYTHONUNBUFFERED=1
echo "start $(date -Is)"
rm -rf a10_work && mkdir a10_work
cp -r ../aromir_v14_release_2026-11-18/measurement a10_work/measurement
cp "$SRC/aromir/releases/v1.4/evaluation.json" "$SRC/aromir/releases/v1.4/measured.json" a10_work/measurement/
"$PY" ../aromir_audit_fixes_2026-11-16/holdouts_for_aromir.py "$PLAN" v14/E7_rungC_v14s3clean_c00_control_eval_clean_seed0.json a10_work/holdouts a=a
nice -n 10 /home/thebreadishard/aromir_dev/bin/aromir evaluate a10_work/holdouts --release a10_work/measurement --out a10_measured.json
"$PY" -m json.tool a10_measured.json | grep -E '"(ring-ip|CH-stretch|CH-oop|other)"|rms_cm|n_modes|n_molecules|interval|        [0-9]' | head -60
echo "end $(date -Is)"
