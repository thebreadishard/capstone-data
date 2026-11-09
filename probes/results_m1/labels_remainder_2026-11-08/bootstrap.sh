#!/usr/bin/env bash
# Bootstrap ubuntu-128gb-hel1-2 CCX53 (157.180.32.149), 2 Oct 2026: miniforge + env qc05 (python 3.12, pyscf 2.14.0 wheel — the kernels link against its bundled OpenBLAS/libgomp), build tools.
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq && apt-get install -y -qq build-essential git htop > /root/apt.log 2>&1
cd /root
curl -sSL -o Miniforge3.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3.sh -b -p /root/miniforge3 > /root/miniforge_install.log 2>&1
/root/miniforge3/bin/mamba create -y -q -n qc05 python=3.12 numpy scipy h5py pip > /root/env_create.log 2>&1
/root/miniforge3/envs/qc05/bin/pip install -q pyscf==2.14.0 geometric psutil > /root/pip.log 2>&1
/root/miniforge3/envs/qc05/bin/python -c "import pyscf, numpy, geometric; print('pyscf', pyscf.__version__, 'numpy', numpy.__version__)"
echo "BOOTSTRAP DONE $(date -u)"
