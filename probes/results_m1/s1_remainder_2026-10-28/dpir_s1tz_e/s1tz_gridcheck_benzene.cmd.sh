#!/bin/bash
cd /root/dpir_s1tz_e || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=15 MKL_NUM_THREADS=15 OPENBLAS_NUM_THREADS=15
THREADS=15 bash probes/s1tz_gridcheck_benzene.sh "$@"
