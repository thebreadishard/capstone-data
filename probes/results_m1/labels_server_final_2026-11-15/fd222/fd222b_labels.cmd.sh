#!/bin/bash
cd /root/fd222 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
CODE=/root/fd222/modules/05_support_predictor/corpus IDS_FILE=ids_b.txt LANES=1 THREADS=8 CAP_MB=26624 LABEL_ARGS='--max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/fd222 FDB '/root/l5b/d8a_relabel.log /root/fd222/fd222a_labels.log' '^=== \((D8A|FDA)\) (all done|STOPPED)' "$@"
