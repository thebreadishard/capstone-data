#!/bin/bash
cd /root/scf_guess_test || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=5 MKL_NUM_THREADS=5 OPENBLAS_NUM_THREADS=5
/root/miniforge3/envs/qc05/bin/python probes/scf_guess_test.py /root/s1tz_acenaphthylene/A_45187bb7c8/T/stubs/mode00_p.json /root/s1tz_acenaphthylene/A_45187bb7c8/T/stubs/mode01_m.json --basis def2-tzvp --grid 75,302 --threads 5 --out /root/scf_guess_test/result.json "$@"
