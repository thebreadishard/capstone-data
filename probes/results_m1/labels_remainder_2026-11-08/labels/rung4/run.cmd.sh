#!/bin/bash
cd /root/labels/rung4 || exit 1

bash /root/labels/labels_batch_ccx53.sh /root/labels/rung4 R4 /root/labels/large_pah/run.log '=== \(L5\) all done' "$@"
