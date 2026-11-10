#!/bin/bash
cd /root/hbcf || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=24 MKL_NUM_THREADS=24 OPENBLAS_NUM_THREADS=24
CAP_SCOPE=system L5F_DIR=/root/hbcf/probes/results_m1/hbc_apt_field_2026-11-01 L5F_PYTHON=/root/miniforge3/envs/qc05/bin/python L5F_THREADS=24 L5F_CAP_MB=32768 L5F_MAX_MEMORY_MB=12000 bash probes/wait_then_run.sh /root/l5b/hbc_wb97x.log '^=== \(HBC\) all done' -- bash probes/l5_apt_field_run.sh "$@"
