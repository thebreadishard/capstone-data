#!/bin/bash
cd /root/dpir_s2 || exit 1

PY=/root/miniforge3/envs/qc05/bin/python bash probes/s2_batch.sh probes/results_m1/s2_training_set_2026-10-14/s2_ids.tsv /root/s2 3 5 G:6-31g*:75,302 "$@"
