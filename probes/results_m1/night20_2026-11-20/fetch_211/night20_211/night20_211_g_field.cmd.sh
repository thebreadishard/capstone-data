#!/bin/bash
cd /root/night20_211 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=16 MKL_NUM_THREADS=16 OPENBLAS_NUM_THREADS=16
env MAX_FIRST=1800 LANES=4 PY=/root/miniforge3/envs/qc05/bin/python bash /root/dpir_90cb5e23/plans/05_delta-probed-ir-pipeline/probes/s1_anharmonic_level.sh /root/night20_211/in/B_3100da3761/geometry.json /root/night20_211/g_label/g/benzonitrile 4 G:6-31g*:75,302 "$@"
