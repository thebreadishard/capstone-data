#!/bin/bash
cd /root/dpir_routea || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
PY=/root/miniforge3/envs/qc05/bin/python PM_SAVING=1 LANES=4 PYSCF_MAX_MEMORY=24000 bash probes/progress_on_growth.sh --tag RAG --dir /root/routea_gate --name pyscf.log --interval 600 -- bash probes/s2_batch.sh probes/results_m1/routea_2026-11-02/ids_gate.tsv /root/routea_gate 1 8 G:6-31g*:75,302 "$@"
