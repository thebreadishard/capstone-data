#!/bin/bash
cd /root/dpir_s1tz_d || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=5 MKL_NUM_THREADS=5 OPENBLAS_NUM_THREADS=5
MAX_FIRST=7400 bash probes/s1tz_run.sh S1TZC probes/results_m1/s1tz_2026-10-18/ids_acenaphthylene.tsv /root/s1tz_acenaphthylene 1 5 "$@"
