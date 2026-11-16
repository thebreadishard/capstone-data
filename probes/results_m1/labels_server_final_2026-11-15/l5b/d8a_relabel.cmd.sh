#!/bin/bash
cd /root/l5b || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
bash probes/run_with_mem_watch.sh /root/l5b/d8a_relabel.log '^  D_8a1c3dddb7 labels started' molecules/D_8a1c3dddb7 /root/l5b/molecules/D_8a1c3dddb7/mem_watch.log -- env CODE=/root/l5b/modules/05_support_predictor/corpus IDS_FILE=ids_d8a.tsv LANES=1 THREADS=8 CAP_MB=26624 LABEL_ARGS='--max-memory 24000 --reuse-existing' bash probes/labels_batch_ccx53.sh /root/l5b D8A /root/t74/tasks74_labels.log '^=== \(T74\) all done' "$@"
