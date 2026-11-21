#!/bin/bash
cd /root/night20_218 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
/root/miniforge3/envs/qc215/bin/python /root/dpir/plans/05_delta-probed-ir-pipeline/probes/low_mode_patch_run.py /root/night20_218/in/molecules /root/night20_218/out_lane2 --ids /root/night20_218/in/ids_lane2.txt --threads 8 --max-memory 2048 --below 60 "$@"
