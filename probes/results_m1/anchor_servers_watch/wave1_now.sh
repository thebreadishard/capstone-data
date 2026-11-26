#!/usr/bin/env bash
# Read-only: per anchor server, wave 1's list in order with each molecule's state (done / running with its gradient count / waiting),
# and the processes of the molecule that runs now.
# no-set-e: a host that does not answer is reported and the loop goes on
set -u
cd /c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline || exit 1
. tools/hosts.sh
for h in anc1 anc2 anc3 anc4 anc5; do
  echo "== $h"
  host_ssh "$h" '
    cd /root/dpir/probes
    while IFS="|" read -r name geom rest; do
      out=results/${name}_ccpvdz
      if [ -f $out/hessian_ccsd_t.npz ]; then s="hessian done$( [ -f $out/apt_ccsd_t_field.npz ] && echo ", apt done" || echo ", apt not yet")"
      elif [ -d $out ]; then s="RUNNING or partial: $(ls $out 2>/dev/null | grep -c "^grad_.*npy") gradient files, newest $(ls -t $out | head -1) $(date -r $out/$(ls -t $out | head -1) +%H:%M)"
      else s="waiting"; fi
      echo "  $name: $s"
    done < /root/dpir/wave.txt
    echo "  processes: $(pgrep -af "anchor_wave.sh|run_anchors_hel23|e8_|cc_apt_field" | sed "s/ --.*//" | cut -c1-110 | tr "\n" ";")"
  ' < /dev/null 2>&1 | cut -c1-330
done
