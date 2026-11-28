#!/bin/bash
cd /root/ano2 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
PY=/root/miniforge3/envs/qc/bin/python PSI_SCRATCH=/root/psi4_scratch THREADS=8 MEMORY_GB=20 CAP_SCOPE=system bash probes/wsl_capped.sh 28000 -- bash probes/ano_step_naphthalene.sh /root/ano2/rows /root/ano2/basis/psi /root/ano2/geom/A_01f3186607/geometry.json "$@"
