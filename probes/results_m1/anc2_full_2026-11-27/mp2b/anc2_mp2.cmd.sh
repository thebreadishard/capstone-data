#!/bin/bash
cd /root/mp2b || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
WAIT_PGREP='[l]abels_batch_ccx53.sh /root/dft1' bash probes/dfmp2_lane.sh /root/mp2b MP /root/dft1/anc2_dft1.log '=== \(AD\) all done' "$@"
