#!/bin/bash
cd /root/dpir || exit 1
export OMP_NUM_THREADS=16 MKL_NUM_THREADS=16 OPENBLAS_NUM_THREADS=16
bash probes/anchor_wave_progress.sh /root/dpir/wave2.txt "$@"
