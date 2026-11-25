#!/bin/bash
cd /root/dft1 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4 OPENBLAS_NUM_THREADS=4
CODE=/root/dft1/modules/05_support_predictor/corpus LANES=1 THREADS=4 CAP_MB=8192 LABEL_ARGS='--max-memory 6000' bash probes/labels_batch_ccx53.sh /root/dft1 AD /root/dft1/ids.txt '^#' "$@"
