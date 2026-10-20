#!/bin/bash
cd /root/CapstonePlan/plans/05_delta-probed-ir-pipeline/modules/05_support_predictor/corpus_p3b || exit 1

export CORPUS_QC_PYTHON=/root/miniforge3/envs/qc/bin/python; /root/miniforge3/envs/qc/bin/python run_corpus.py --layer P3 --shard 1/2 --threads 8 --memory-gb 12 --worker-max-hours 48 "$@"
