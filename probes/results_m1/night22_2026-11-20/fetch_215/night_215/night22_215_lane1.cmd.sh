#!/bin/bash
cd /root/night_215 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
env PY=/root/miniforge3/envs/qc215/bin/python MAX_MEMORY_MB=24000 bash /root/dpir_6ec8af75/plans/05_delta-probed-ir-pipeline/probes/imaginary_reopt_lane.sh /root/night_215/in/molecules /root/night_215/out/lane1 /root/night_215/in/ids_night22_lane1.txt 8 "$@"
