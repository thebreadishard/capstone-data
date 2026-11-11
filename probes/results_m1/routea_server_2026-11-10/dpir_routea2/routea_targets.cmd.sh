#!/bin/bash
cd /root/dpir_routea2 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
PY=/root/miniforge3/envs/qc05/bin/python LANES=4 PYSCF_MAX_MEMORY=24000 bash probes/progress_on_growth.sh --tag RAT --dir /root/routea --name pyscf.log --interval 600 -- bash probes/s2_batch.sh probes/results_m1/routea_2026-11-02/ids_targets.tsv /root/routea 1 8 G:6-31g*:75,302 "$@"
