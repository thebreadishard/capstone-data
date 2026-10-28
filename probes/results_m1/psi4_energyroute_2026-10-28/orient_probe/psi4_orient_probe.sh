#!/usr/bin/env bash
# Runs the scratch orientation diagnostic in WSL with the vpt2 environment's psi4.
set -euo pipefail
SP=/mnt/c/Users/thebr/AppData/Local/Temp/claude/C--Users-thebr-Documents-CapstonePlan/080ff7ed-d45b-451f-8c06-e90bcbbe88a0/scratchpad
"$HOME/miniforge3/envs/vpt2/bin/python" -u "$SP/psi4_orient_probe.py" "$SP/psi4_orient_out"
grep -n "Symmetry:" "$SP/psi4_orient_out/psi4.log" | awk '{print $NF}' | uniq -c
