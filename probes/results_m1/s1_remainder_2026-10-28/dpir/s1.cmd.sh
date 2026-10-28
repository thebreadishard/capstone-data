#!/bin/bash
cd /root/dpir || exit 1

PY=/root/miniforge3/envs/qc05/bin/python PARALLEL=1 bash probes/s1_anharmonic_level.sh modules/05_support_predictor/corpus/molecules/A_8448043181/geometry.json /root/s1_benzene 5 R:6-31g*:99,590 G:6-31g*:75,302 B:6-31g:99,590 "$@"
