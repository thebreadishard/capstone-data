#!/bin/bash
cd /root/CapstonePlan/plans/05_delta-probed-ir-pipeline/modules/05_support_predictor/corpus_b || exit 1

export CORPUS_QC_PYTHON=/root/miniforge3/envs/qc/bin/python; /root/miniforge3/envs/qc/bin/python run_corpus.py --ids $(tr -d '\n\r' < /root/next_pool_ids_b.txt) --threads 8 --memory-gb 12 "$@"
