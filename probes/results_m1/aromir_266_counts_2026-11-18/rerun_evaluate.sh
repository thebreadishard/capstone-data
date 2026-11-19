#!/bin/bash
# TASKS 266: `aromir evaluate` again on v1.3 and v1.4 with the code that counts each family's molecules (aromir branch
# acceptance-269, ~/aromir-wt-269), and the records of format 3 composed from it. No quantum chemistry: stored Hessians.
# Run from this folder in WSL: bash rerun_evaluate.sh
set -euo pipefail
PY=~/aromir_dev/bin/python
AROMIR=~/aromir_dev/bin/aromir
SRC=~/aromir-wt-269/src
REL=$SRC/aromir/releases
export PYTHONPATH=$SRC OMP_NUM_THREADS=2 PYTHONUNBUFFERED=1
"$PY" -c "import aromir, sys; sys.exit(0 if aromir.__file__.startswith('$SRC') else 'aromir is not the branch: ' + aromir.__file__)"
echo "start $(date -Is)"
rm -rf work && mkdir work
# v1.4: the measurement networks (make_folders.py's conversion), whose errors the release carries
cp -r ../aromir_v14_release_2026-11-18/measurement work/v14
"$PY" upgrade_record.py placeholder "$REL/v1.4/evaluation.json" work/v14/evaluation.json
nice -n 10 "$AROMIR" evaluate ../aromir_v14_release_2026-11-18/holdouts --release work/v14 --out work/measured_v14.json
"$PY" upgrade_record.py compose "$REL/v1.4/evaluation.json" "$REL/v1.4/measured.json" work/measured_v14.json counts_v14.json \
  work/evaluation_v14.json
# v1.3: the networks it ships are the ones its errors were measured on
cp -r "$REL/v1.3" work/v13
"$PY" upgrade_record.py placeholder "$REL/v1.3/evaluation.json" work/v13/evaluation.json
nice -n 10 "$AROMIR" evaluate holdouts_v13 --release work/v13 --out work/measured_v13.json
"$PY" upgrade_record.py compose "$REL/v1.3/evaluation.json" "$REL/v1.3/measured.json" work/measured_v13.json counts_v13.json \
  work/evaluation_v13.json
echo "end $(date -Is)"
