#!/usr/bin/env bash
# build_qc215.sh (night20, 20 Nov 2026) — env qc215 on the server as tools/build_env_beside.py built it on the laptop: a venv on qc05's
# interpreter, the laptop's pin list (build-requirements.txt of ~/qc215) installed with --no-deps, pip check, freeze equal to the pins,
# pyscf imports. The target is never overwritten; nothing is deleted. Records pip freeze of both envs into /root/night20_ops/.
set -euo pipefail
OPS=/root/night20_ops
SRC=/root/miniforge3/envs/qc05/bin/python
DST=/root/miniforge3/envs/qc215
REQ=$OPS/qc215_build-requirements.txt
[ -x "$SRC" ] || { echo "no qc05 interpreter"; exit 1; }
[ -f "$REQ" ] || { echo "no pin list $REQ"; exit 1; }
[ ! -e "$DST" ] || { echo "$DST exists; it is never overwritten"; exit 1; }
"$SRC" -m venv "$DST"
cp "$REQ" "$DST/build-requirements.txt"
"$DST/bin/python" -m pip install --no-input --no-deps -r "$DST/build-requirements.txt" > "$OPS/qc215_install.log" 2>&1
"$DST/bin/python" -m pip check
"$DST/bin/python" -m pip freeze > "$OPS/pip_freeze_qc215.txt"
"$SRC" -m pip freeze > "$OPS/pip_freeze_qc05.txt"
diff <(sort -f "$REQ") <(sort -f "$OPS/pip_freeze_qc215.txt") || { echo "FREEZE DIFFERS FROM THE PINS"; exit 1; }
"$DST/bin/python" -VV
"$DST/bin/python" -c 'import pyscf, numpy, scipy; print("qc215: pyscf", pyscf.__version__, "numpy", numpy.__version__, "scipy", scipy.__version__)'
"$SRC" -c 'import pyscf, numpy, scipy; print("qc05: pyscf", pyscf.__version__, "numpy", numpy.__version__, "scipy", scipy.__version__)'
echo "QC215 BUILT"
