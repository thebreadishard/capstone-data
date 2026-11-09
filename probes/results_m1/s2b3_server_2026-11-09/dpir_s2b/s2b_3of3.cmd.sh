#!/bin/bash
cd /root/dpir_s2b || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=15 MKL_NUM_THREADS=15 OPENBLAS_NUM_THREADS=15
PY=/root/miniforge3/envs/qc05/bin/python bash probes/progress_on_growth.sh --tag S2B3 --dir /root/s2b --name '*.json' --interval 600 -- bash probes/s2_batch.sh probes/results_m1/s2b_training_set_2026-10-19/plan/s2b_ids_3of3.tsv /root/s2b 3 5 G:6-31g*:75,302 "$@"
