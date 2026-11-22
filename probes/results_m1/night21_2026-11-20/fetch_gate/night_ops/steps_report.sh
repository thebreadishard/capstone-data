#!/usr/bin/env bash
# steps_report.sh <server> — per lane of /root/night_215: every molecule started, its optimisation steps and the mean seconds
# between its step lines, and the lane's marker lines. Reads only.
# no-set-e: a lane without a log is reported and the others still print
set -u
SERVER=${1:?server}
cd /root/night_215 || exit 1
for k in 0 1 2 3; do
  log=${SERVER}_215_lane$k.log
  echo "-- lane $k ($(grep -v '^#' in/ids_${SERVER}_lane$k.txt | awk 'NF {printf "%s(%s) ", $1, $2}'))"
  [ -f "$log" ] || { echo "   no log"; continue; }
  awk '
    function secs(d, t,   a, b) { split(d, a, "-"); split(t, b, ":"); return mktime(a[1] " " a[2] " " a[3] " " b[1] " " b[2] " " b[3]) }
    /^=== \(IRL\) [A-Za-z0-9_]+: start/ { if (id != "") flush(); id = $3; sub(":", "", id); n = 0; first = 0; last = 0; start = secs($(NF-1), $NF) }
    /^\(RLS\) step / { n++; t = secs($(NF-1), $NF); if (n == 1) first = t; last = t; gmax = $7 }
    function flush() { printf "   %s: %d steps", id, n; if (n > 1) printf ", %.0f s per step (first step after %d s)", (last - first) / (n - 1), first - start; if (n > 0) printf ", last gmax %s", gmax; printf "\n" }
    END { if (id != "") flush() }' "$log"
  grep -E '^=== \(IRL\) .*(optimisation done|labels done|no imaginary mode|STILL IMAGINARY|FAILED|lane done)|Traceback' "$log" | cut -c1-160 | sed 's/^/   /'
done
echo "-- $(date -u '+%F %T UTC'); load $(cut -d' ' -f1-3 /proc/loadavg)"
