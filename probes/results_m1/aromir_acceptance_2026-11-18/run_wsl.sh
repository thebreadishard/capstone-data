#!/bin/bash
# TASKS 269 criteria 1-2 in WSL: the clean install's `aromir spectrum` over the fixed set, capped beside whatever else runs.
# Run from this folder in WSL; extra arguments (--dry-run, --only <name>) go to run_set.py.
set -euo pipefail
export OMP_NUM_THREADS=8 PYTHONUNBUFFERED=1 PYTHONUTF8=1 PYSCF_TMPDIR=/home/thebreadishard/qc_tmp TMPDIR=/home/thebreadishard/qc_tmp
mkdir -p "$PYSCF_TMPDIR"
nice -n 5 bash ../../wsl_capped.sh 3584 -- /home/thebreadishard/aromir_dev/bin/python run_set.py aromir \
  /home/thebreadishard/aromir_clean_269/bin/aromir fixed_set.json aromir_wsl --threads 8 "$@"
