#!/usr/bin/env bash
# night20_status_remote.sh <job>… — the server side of probes/night20_status.sh (20 Nov 2026): per job, given as
# 'name|workdir|total|glob of the files that count as done' (the glob relative to the workdir), one line per lane (a lane is a
# <name>.pid that tools/remote_launch.sh wrote in the workdir): alive or its exit code, the last log line and its age; then the
# done count, and at the end the load and the free memory. Reads only.
# no-set-e: a job whose folder or log is missing is reported on its line, the others still print
set -u
now=$(date +%s)
for job in "$@"; do
  IFS='|' read -r name work total glob <<< "$job"
  if [ ! -d "$work" ]; then echo "== $name: no folder $work"; continue; fi
  cd "$work" || continue
  # the glob is expanded here on purpose: it names the files that count as done
  # shellcheck disable=SC2086
  done_n=$(ls -d $glob 2>/dev/null | wc -l)
  alive=0; lanes=0; lines=()
  for pidfile in *.pid; do
    [ -f "$pidfile" ] || continue
    lane=${pidfile%.pid}; lanes=$((lanes + 1))
    if kill -0 "$(cat "$pidfile")" 2>/dev/null; then state=alive; alive=$((alive + 1))
    elif [ -f "$lane.exit" ]; then state="exit $(cat "$lane.exit")"
    else state="GONE without an exit file"; fi
    if [ -f "$lane.log" ]; then
      age=$(( (now - $(stat -c %Y "$lane.log")) / 60 ))
      last=$(tail -n 1 "$lane.log" | cut -c1-140)
    else age="?"; last="(no log)"; fi
    lines+=("   $lane: $state; last line ${age} min ago: $last")
  done
  echo "== $name: $alive of $lanes lanes alive, $done_n / $total done"
  [ "${#lines[@]}" -eq 0 ] || printf '%s\n' "${lines[@]}"
done
echo "== load $(cut -d' ' -f1-3 /proc/loadavg) on $(nproc) cores; $(free -g | awk '/^Mem:/ {print $7 " GB of " $2 " GB available"}'); disk $(df -h /root | awk 'NR==2 {print $4 " free"}'); $(date -u '+%F %T UTC')"
