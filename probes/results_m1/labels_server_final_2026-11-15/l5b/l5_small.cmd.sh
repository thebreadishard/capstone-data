#!/bin/bash
cd /root/l5b || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
CODE=/root/l5b/modules/05_support_predictor/corpus IDS_FILE=ids_small.tsv CAP_MB=26624 LABEL_ARGS='--max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/l5b L5S /root/cations_c/cations_ccx53.log '^=== \(CX\) all done' "$@"
