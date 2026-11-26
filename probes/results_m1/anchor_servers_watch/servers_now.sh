#!/usr/bin/env bash
# Read-only: every host in tools/hosts.tsv; per anchor server how far wave 1 and the MP2 lane are, load, memory and disk.
# no-set-e: a host that does not answer is reported and the loop goes on
set -u
cd /c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline || exit 1
. tools/hosts.sh
echo "hosts.tsv:"; grep -v '^#' tools/hosts.tsv | cut -f1,3- | cut -c1-110
for h in anc1 anc2 anc3 anc4 anc5; do
  echo "== $h"
  host_ssh "$h" "
    n=\$(grep -c . /root/dpir/wave.txt); d=\$(grep -c 'hessian DONE' /root/dpir/anchors.log); a=\$(grep -c 'apt PASS' /root/dpir/anchors.log)
    bad=\$(grep -c -E 'hessian (FAILED|IMAGINARY)|apt FAIL' /root/dpir/anchors.log)
    echo \"wave 1: \$d of \$n Hessians done, \$a APT passed, \$bad failed; last: \$(grep -a '=== (AS3)' /root/dpir/anchors.log | tail -1 | cut -c1-90)\"
    echo \"mp2 rows finished: \$(ls /root/mp2b/rows 2>/dev/null | wc -l) of \$(grep -c . /root/mp2b/list.txt 2>/dev/null); lane running: \$(pgrep -fc '[d]fmp2_lane.sh')\"
    echo \"load \$(cut -d' ' -f1-3 /proc/loadavg); mem free \$(free -g | awk '/Mem/{print \$7}') GB; disk \$(df -h /root | awk 'NR==2{print \$5\" used, \"\$4\" free\"}')\"
  " < /dev/null 2>&1 | cut -c1-200
done
