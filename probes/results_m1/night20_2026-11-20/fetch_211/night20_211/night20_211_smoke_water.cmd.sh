#!/bin/bash
cd /root/night20_211 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
env MAX_FIRST=1800 LANES=4 PY=/root/miniforge3/envs/qc05/bin/python bash /root/dpir_90cb5e23/plans/05_delta-probed-ir-pipeline/probes/s1_anharmonic_level.sh /root/dpir_90cb5e23/plans/05_delta-probed-ir-pipeline/probes/results_m1/water_dipole_fd_2026-10-02/geometry.json /root/night20_211/smoke_water 2 G:6-31g*:75,302 "$@"
