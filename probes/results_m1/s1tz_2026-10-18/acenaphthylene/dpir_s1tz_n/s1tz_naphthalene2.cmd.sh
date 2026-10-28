#!/bin/bash
cd /root/dpir_s1tz_n || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=5 MKL_NUM_THREADS=5 OPENBLAS_NUM_THREADS=5
GUESS_FROM_PREVIOUS=1 MAX_FIRST=5400 bash probes/s1tz_run.sh S1TZN probes/results_m1/s1tz_2026-10-18/ids_naphthalene.tsv /root/s1tz_naphthalene 1 5 "$@"
