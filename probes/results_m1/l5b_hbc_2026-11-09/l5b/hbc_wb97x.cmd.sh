#!/bin/bash
cd /root/l5b || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=24 MKL_NUM_THREADS=24 OPENBLAS_NUM_THREADS=24
CODE=/root/l5b/modules/05_support_predictor/corpus IDS_FILE=ids_hbc.tsv LANES=1 THREADS=24 CAP_MB=112640 LABEL_ARGS='--max-memory 100000 --reuse-existing --newton-finish' bash probes/labels_batch_ccx53.sh /root/l5b HBC /root/t74/tasks74_labels.log '^=== \(T74\) all done' "$@"
