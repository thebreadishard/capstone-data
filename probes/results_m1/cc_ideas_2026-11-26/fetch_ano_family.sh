#!/usr/bin/env bash
# Downloads the whole ano-pVnZ family (n = D, T, Q, 5) for H, C and N from the Basis Set Exchange (the user's word, 26 Nov 2026:
# 'Download alvast een gecontroleerd ano-pVDZ-bestand') in psi4 and NWChem format, with the BSE's own reference list and its
# version notes, into an empty folder; prints sizes and sha256. Text files from the web: stored as data, opened by nothing here.
# The check of what the files are is basis_family_check.py (TASKS 319, idea 1).
# no-set-e: every download reports its own result
set -u
DST=/c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline/probes/results_m1/cc_ideas_2026-11-26/basis
[ -e "$DST" ] && { echo "$DST exists; nothing downloaded"; exit 1; }
mkdir -p "$DST" && cd "$DST" || exit 1
API=https://www.basissetexchange.org/api
for name in ano-pvdz ano-pvtz ano-pvqz ano-pv5z; do
  for fmt in psi4 nwchem; do
    curl -sS -L --max-time 60 -A "basis-fetch" -o "$name.$fmt.txt" "$API/basis/$name/format/$fmt/?elements=1,6,7" || echo "DOWNLOAD FAILED $name $fmt"
    sleep 2
  done
  curl -sS -L --max-time 60 -A "basis-fetch" -o "$name.references.txt" "$API/references/$name/format/txt/?elements=1,6,7" || echo "REFERENCES FAILED $name"
  curl -sS -L --max-time 60 -A "basis-fetch" -o "$name.notes.txt" "$API/notes/$name" || echo "NOTES FAILED $name"
  sleep 2
done
for f in *.txt; do echo "== $f: $(stat -c %s "$f") bytes, sha256 $(sha256sum < "$f" | cut -c1-16)"; done
grep -H 'BASIS SET' ./*.nwchem.txt
{ echo "Source: $API/basis/<name>/format/<fmt>/?elements=1,6,7, $API/references/<name>/format/txt/?elements=1,6,7 and $API/notes/<name>"; echo "Fetched: $(date '+%F %T')"; sha256sum *.txt; } > SOURCE.md
