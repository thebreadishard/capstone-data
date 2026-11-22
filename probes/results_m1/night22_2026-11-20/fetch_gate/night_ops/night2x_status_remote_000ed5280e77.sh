#!/usr/bin/env bash
# night2x_status_remote.sh <server name> — the server side of probes/night2x_status.sh (20 Nov 2026): TASKS 215's four lanes in
# /root/night_215 on night21 or night22. Per lane (a lane is <server>_215_lane<k>.pid, written by tools/remote_launch.sh): alive, its
# exit code or stopped; the molecules labelled (analytic_check.json) and optimised (geometry.json) of the lane's list; the molecule it
# is on; the last log line and its age. Then the load and the free memory. Reads only.
# no-set-e: a lane whose folder or log is missing is reported on its line, the others still print
set -u
SERVER=${1:?server name}
WORK=/root/night_215
now=$(date +%s)
cd "$WORK" 2>/dev/null || { echo "== 215 on $SERVER: no folder $WORK"; exit 0; }
alive_n=0; done_all=0; total_all=0; lines=()
for k in 0 1 2 3; do
  lane=${SERVER}_215_lane$k; ids=in/ids_${SERVER}_lane$k.txt; out=out/lane$k
  total=$(grep -v '^#' "$ids" 2>/dev/null | awk 'NF' | wc -l)
  labelled=$(find "$out" -mindepth 2 -maxdepth 2 -name analytic_check.json 2>/dev/null | wc -l)
  optimised=$(find "$out" -mindepth 2 -maxdepth 2 -name geometry.json 2>/dev/null | wc -l)
  total_all=$((total_all + total)); done_all=$((done_all + labelled))
  if [ ! -s "$lane.pid" ]; then lines+=("   lane $k: NOT LAUNCHED (no pid file); 0 / $total"); continue; fi
  if pgrep -g "$(cat "$lane.pid")" > /dev/null; then state=alive; alive_n=$((alive_n + 1))
  elif [ -f "$lane.exit" ]; then state="exit $(cat "$lane.exit")"
  else state="stopped (no process, no exit file)"; fi
  if [ -f "$lane.log" ]; then
    age=$(( (now - $(stat -c %Y "$lane.log")) / 60 ))
    last=$(tail -n 1 "$lane.log" | cut -c1-120)
    on=$(grep -E '^=== \(IRL\) [A-Za-z0-9_]+: start' "$lane.log" | tail -n 1 | sed -E 's/^=== \(IRL\) ([A-Za-z0-9_]+): start.*/\1/')
    steps=$(awk -v id="$on" '/^=== \(IRL\) / { cur = ($3 == id ":") } cur && /^\(RLS\) step / { n++ } END { print n + 0 }' "$lane.log")
  else age="?"; last="(no log)"; on="?"; steps=0; fi
  lines+=("   lane $k: $state; $labelled / $total labelled, $optimised optimised; on ${on:-none} ($steps optimisation steps logged); last line $age min ago: $last")
done
echo "== 215 on $SERVER: $alive_n of 4 lanes alive, $done_all / $total_all molecules labelled"
printf '%s\n' "${lines[@]}"
echo "== load $(cut -d' ' -f1-3 /proc/loadavg) on $(nproc) cores; $(free -g | awk '/^Mem:/ {print $7 " GB of " $2 " GB available"}'); disk $(df -h /root | awk 'NR==2 {print $4 " free"}'); $(date -u '+%F %T UTC')"
