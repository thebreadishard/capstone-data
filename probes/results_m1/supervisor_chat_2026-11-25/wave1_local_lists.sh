#!/usr/bin/env bash
# The local copies of wave 1's lists follow the servers' (the four F/Cl molecules taken out on 25 Nov 2026); the dealt list is kept
# beside each under a name the wave-list tool does not read as a list. Then: do the run specs still see matching server copies?
# no-set-e: every step reports its own result
set -u
cd /c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline || exit 1
. tools/hosts.sh
W=probes/results_m1/anchor_waves_2026-11-21
for h in anc2 anc4 anc5; do
  [ -e "$W/$h/dealt_2026-11-21.list" ] || cp -p "$W/$h/wave.txt" "$W/$h/dealt_2026-11-21.list"
  host_ssh "$h" "cat /root/dpir/wave.txt" < /dev/null > "$W/$h/wave.txt.tmp" && [ -s "$W/$h/wave.txt.tmp" ] && mv "$W/$h/wave.txt.tmp" "$W/$h/wave.txt"
  echo "$h: local list $(grep -c . "$W/$h/wave.txt") lines (dealt: $(grep -c . "$W/$h/dealt_2026-11-21.list")), sha $(sha256sum < "$W/$h/wave.txt" | cut -c1-12) = server $(host_ssh "$h" "sha256sum < /root/dpir/wave.txt" < /dev/null | cut -c1-12)"
  PYTHONUTF8=1 python tools/runspec.py validate "probes/runspecs/${h}_wave1.json" 2>&1 | tail -1 | cut -c1-160
done
echo "=== collect the finished one"
bash probes/collect_anchor.sh anc1 B_0d3c79f4c4 2>&1 | tail -2 | cut -c1-200
