#!/usr/bin/env bash
# gate_run.sh (night21 / night22, 20 Nov 2026) — the gate night20 passed, on this server, in env qc215:
#   (a) tests/test_low_mode_patch_run.py (the runner's water test);
#   (b) B_1e0fa2d7f0 of the 13 Nov repair recomputed with that run's arguments (--below 20, step 0.01, 8 threads, --max-memory 2048)
#       from the pre-swap labels, into /root/night_gate/out (a fresh folder; refused when it exists).
# The comparison with the laptop's stored points is made on the laptop. Nothing is deleted.
set -euo pipefail
R=/root/dpir_6ec8af75/plans/05_delta-probed-ir-pipeline
PY=/root/miniforge3/envs/qc215/bin/python
G=/root/night_gate
[ -d "$G/in/molecules/B_1e0fa2d7f0" ] || { echo "no gate inputs"; exit 1; }
[ ! -e "$G/out" ] || { echo "$G/out exists; the gate runs once into a fresh folder"; exit 1; }
export PYTHONUNBUFFERED=1
cd "$R"
echo "=== gate (a) pytest $(date -u '+%F %T')"
"$PY" -m pytest tests/test_low_mode_patch_run.py -q -p no:cacheprovider 2>&1 | tee "$G/gate_pytest.log"
export OMP_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8 MKL_NUM_THREADS=8
echo "=== gate (b) B_1e0fa2d7f0 $(date -u '+%F %T')"
"$PY" "$R/probes/low_mode_patch_run.py" "$G/in/molecules" "$G/out" --ids "$G/in/ids_gate.txt" --threads 8 --max-memory 2048 --below 20 --step 0.01 2>&1 | tee "$G/gate.log"
echo "=== gate run done $(date -u '+%F %T')"
