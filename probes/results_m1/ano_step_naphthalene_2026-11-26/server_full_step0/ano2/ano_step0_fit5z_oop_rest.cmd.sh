#!/bin/bash
cd /root/ano2 || exit 1
export PYTHONUNBUFFERED=1 OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 OPENBLAS_NUM_THREADS=8
while pgrep -f '[d]fmp2_rows.py rows' > /dev/null; do sleep 30; done; test "$(cat /root/ano2/ano_step0_fit5z_oop.exit)" = 0 || { echo 'refusing to start: ano_step0_fit5z_oop did not end with exit 0'; exit 1; }; PSIPATH=/root/ano2/basis/psi PSI_SCRATCH=/root/psi4_scratch CAP_SCOPE=system bash probes/wsl_capped.sh 28000 -- /root/miniforge3/envs/qc/bin/python probes/dfmp2_rows.py rows --geometry /root/ano2/geom/A_01f3186607/geometry.json --basis ano-pvqz --threads 8 --memory-gb 20 --out /root/ano2/rows_step0/rows_mp2_anopvqz_fit5z_oop.npz --df-basis-scf cc-pv5z-jkfit --df-basis-mp2 cc-pv5z-ri --only-row 2 --only-row 8 --only-row 32 "$@"
