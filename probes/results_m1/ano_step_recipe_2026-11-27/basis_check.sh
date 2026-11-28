#!/usr/bin/env bash
# The two checks of the downloaded ano-pVQZ file (H, C, N, O, S), in WSL: psi4 (env vpt2) and pyscf (~/qc05), on HSNO; output to
# basis_check.txt beside this script. Run: wsl -e bash <this file>
set -eu
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$HERE/basis/psi"
cp "$HERE/basis/ano-pvqz.psi4.txt" "$HERE/basis/psi/ano-pvqz.gbs"
export PSI_SCRATCH=$HOME/psi4_scratch OMP_NUM_THREADS=4
{
  date '+%F %T'
  PSIPATH="$HERE/basis/psi" "$HOME/miniforge3/envs/vpt2/bin/python" "$HERE/basis_check_psi4.py"
  OMP_NUM_THREADS=4 "$HOME/qc05/bin/python" "$HERE/basis_check_pyscf.py" "$HERE/basis/ano-pvqz.nwchem.txt"
} 2>&1 | tee "$HERE/basis_check.txt.tmp"
mv "$HERE/basis_check.txt.tmp" "$HERE/basis_check.txt"
echo "=== BASIS CHECK done $(date '+%F %T')"
