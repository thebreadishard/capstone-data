#!/usr/bin/env bash
# Downloads the ano-pVTZ and ano-pVQZ basis sets for H and C from the Basis Set Exchange (the user's word, 25 Nov 2026) in psi4 and
# NWChem format, with the BSE's own reference list, into an empty folder; prints sizes, sha256 and the head of each. Text files
# from the web: stored as data, opened by nothing here.
# no-set-e: every download reports its own result
set -u
DST=/c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline/probes/results_m1/ano_step_benzene_2026-11-25/basis
[ -e "$DST" ] && { echo "$DST exists; nothing downloaded"; exit 1; }
mkdir -p "$DST" && cd "$DST" || exit 1
API=https://www.basissetexchange.org/api
for name in ano-pvtz ano-pvqz; do
  for fmt in psi4 nwchem; do
    curl -sS -L --max-time 60 -A "basis-fetch" -o "$name.$fmt.txt" "$API/basis/$name/format/$fmt/?elements=1,6" || echo "DOWNLOAD FAILED $name $fmt"
    sleep 2
  done
  curl -sS -L --max-time 60 -A "basis-fetch" -o "$name.references.txt" "$API/references/$name/format/txt/?elements=1,6" || echo "REFERENCES FAILED $name"
  sleep 2
done
for f in *.txt; do echo "== $f: $(stat -c %s "$f") bytes, sha256 $(sha256sum < "$f" | cut -c1-16)"; head -n 12 "$f" | cut -c1-110; done
{ echo "Source: $API/basis/<name>/format/<fmt>/?elements=1,6 and $API/references/<name>/format/txt/?elements=1,6"; echo "Fetched: $(date '+%F %T')"; sha256sum *.txt; } > SOURCE.md
