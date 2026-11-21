#!/bin/bash
cd /root/night20_218c || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
/root/miniforge3/envs/qc215/bin/python /root/dpir/plans/05_delta-probed-ir-pipeline/probes/low_mode_patch_run.py /root/night20_218/in/molecules /root/night20_218c/out --ids /root/night20_218c/in/ids_q2test.txt --threads 8 --max-memory 2048 --below 60 --step 0.04 "$@"
