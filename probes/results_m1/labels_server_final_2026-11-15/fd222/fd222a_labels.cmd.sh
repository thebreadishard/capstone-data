#!/bin/bash
cd /root/fd222 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=24 MKL_NUM_THREADS=24 OPENBLAS_NUM_THREADS=24
CODE=/root/fd222/modules/05_support_predictor/corpus IDS_FILE=ids_a.txt LANES=3 THREADS=8 CAP_MB=26624 LABEL_ARGS='--max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/fd222 FDA /root/hbcf/hbc_apt_field.log '^=== \(L5F\) (all done|STOPPED)' "$@"
