#!/bin/bash
cd /root/t74 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
CODE=/root/t74/modules/05_support_predictor/corpus CAP_MB=26624 LABEL_ARGS='--max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/t74 T74 /root/l5b/l5_large.log '^=== \(L5L\) all done' "$@"
