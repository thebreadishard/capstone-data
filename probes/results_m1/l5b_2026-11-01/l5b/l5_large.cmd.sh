#!/bin/bash
cd /root/l5b || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
CODE=/root/l5b/modules/05_support_predictor/corpus IDS_FILE=ids_large.tsv LANES=1 THREADS=32 CAP_MB=112640 LABEL_ARGS='--max-memory 100000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/l5b L5L /root/l5b/l5_small.log '^=== \(L5S\) all done' "$@"
