#!/bin/bash
cd /root/cations_c || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
CODE=/root/cations_c/modules/05_support_predictor/corpus WAIT_COUNT=4 CAP_MB=26624 LABEL_ARGS='--charge 1 --spin 1 --max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/cations_c CX '/root/labels/lane_[0-3].log' 'LANE [0-3] DONE' "$@"
