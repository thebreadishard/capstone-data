#!/bin/bash
# TASKS 269 criterion 3 in WSL: v1.4's invariance spreads with the clean install, capped. Extra arguments go to invariance_v14.py.
set -euo pipefail
export OMP_NUM_THREADS=2 PYTHONUNBUFFERED=1 PYTHONUTF8=1
C=../../../modules/05_support_predictor/corpus
OUT=invariance
for arg in "$@"; do [ "$arg" = "--only" ] && OUT=dry_invariance; done
nice -n 10 bash ../../wsl_capped.sh 1024 -- /usr/bin/time -f '(INV) max RSS %M kB, wall %e s' \
  /home/thebreadishard/aromir_clean_269/bin/python invariance_v14.py "$C/molecules" "$C/manifest.csv" "$OUT" "$@"
echo "(INV) done"
