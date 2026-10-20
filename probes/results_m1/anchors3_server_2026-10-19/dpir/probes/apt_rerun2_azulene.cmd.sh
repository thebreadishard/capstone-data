#!/bin/bash
cd /root/dpir/probes || exit 1

bash anchor_apt_rerun.sh azulene 8 6000 "$@"
