#!/bin/bash
cd /root/dpir_routea2 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
bash probes/routea_gate_direct.sh "$@"
