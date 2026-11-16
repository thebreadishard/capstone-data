#!/bin/bash
cd /root/fd222 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=32 MKL_NUM_THREADS=32 OPENBLAS_NUM_THREADS=32
CODE=/root/fd222/modules/05_support_predictor/corpus CAP_MB=26624 WAIT_COUNT=2 LABEL_ARGS='--max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/fd222 FD2 '/root/l5b/hbc_wb97x.log /root/l5b/d8a_relabel.log' '^=== \((HBC|D8A)\) all done' "$@"
