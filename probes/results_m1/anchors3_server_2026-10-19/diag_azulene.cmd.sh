#!/bin/bash
cd /root || exit 1

OMP_NUM_THREADS=2 nice -n 10 /root/miniforge3/envs/qc05/bin/python diag_azulene_field.py --ccsd "$@"
