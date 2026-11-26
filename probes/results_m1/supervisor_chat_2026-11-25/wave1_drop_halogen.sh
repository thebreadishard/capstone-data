#!/usr/bin/env bash
# The user, 25 Nov 2026 ('Nee, stop ze'): the four waiting F/Cl molecules of wave 1 leave their servers' lists. The wave reads its list
# line by line as it goes (anchor_wave.sh: while read … done < list), so a later line taken out of the SAME file (same inode, the
# earlier bytes untouched) is simply never reached; the running molecule is not touched. Per server: refuse unless every molecule
# to drop is still waiting (no result folder) and lies after the running one; keep the dealt list beside it; rewrite in place;
# check inode, earlier lines and the wave's processes; write a line into the wave's log.
# no-set-e: every step checks its own result and names the host
set -u
cd /c/Users/thebr/Documents/CapstonePlan/plans/05_delta-probed-ir-pipeline || exit 1
. tools/hosts.sh
drop() {  # host id...
  local h=$1; shift
  local ids="$*" n=$#
  local pat=${ids// /|}
  echo "== $h: drop $ids"
  host_ssh "$h" "
    set -u; cd /root/dpir || exit 1
    for i in $ids; do
      grep -q \"^\$i|\" wave.txt || { echo \"REFUSED: \$i is not in wave.txt\"; exit 1; }
      [ -e probes/results/\${i}_ccpvdz ] && { echo \"REFUSED: \$i has a result folder (running or done)\"; exit 1; }
    done
    running=\$(pgrep -af 'e8_cc_hessian_fd.py|cc_apt_field.py' | grep -o 'geoms/[A-Za-z0-9_][A-Za-z0-9_]*' | head -1 | cut -d/ -f2)
    [ -n \"\$running\" ] || { echo 'REFUSED: no molecule is running, the wave may be between two molecules'; exit 1; }
    rl=\$(grep -n \"^\$running|\" wave.txt | cut -d: -f1)
    for i in $ids; do
      il=\$(grep -n \"^\$i|\" wave.txt | cut -d: -f1)
      [ \"\$il\" -gt \"\$rl\" ] || { echo \"REFUSED: \$i (line \$il) is not after the running \$running (line \$rl)\"; exit 1; }
    done
    [ -e wave.txt.dealt_2026-11-21 ] || cp -p wave.txt wave.txt.dealt_2026-11-21
    before=\$(stat -c %i wave.txt); head -n \"\$rl\" wave.txt | sha256sum > /tmp/head_before
    grep -v -E '^($pat)[|]' wave.txt > wave.txt.new || exit 1
    [ \$(( \$(grep -c . wave.txt) - \$(grep -c . wave.txt.new) )) -eq $n ] || { echo 'REFUSED: the new list does not differ by exactly the molecules to drop'; rm wave.txt.new; exit 1; }
    cat wave.txt.new > wave.txt && rm wave.txt.new
    after=\$(stat -c %i wave.txt); head -n \"\$rl\" wave.txt | sha256sum > /tmp/head_after
    [ \"\$before\" = \"\$after\" ] && cmp -s /tmp/head_before /tmp/head_after || { echo 'CHECK FAILED: inode or earlier lines changed'; exit 1; }
    echo \"=== (AS3) list edited: $ids taken out of wave.txt while waiting (F/Cl out of scope, the user 25 Nov 2026) \$(date '+%F %T')\" >> anchors.log
    echo \"ok: inode \$after kept, lines 1-\$rl unchanged, running \$running; list now: \$(cut -d'|' -f1 wave.txt | tr '\n' ' ')\"
    echo \"wave process alive: \$(pgrep -fc '[a]nchor_wave.sh /root/dpir/wave.txt'), workers: \$(pgrep -fc 'e8_cc_hessian_fd.py')\"
  " < /dev/null 2>&1 | cut -c1-260
}
if [ "${1:-}" = "--dry" ]; then
  for h in anc2 anc4 anc5; do echo "== $h"; host_ssh "$h" "cd /root/dpir && stat -c 'inode %i, %s bytes' wave.txt && cut -d'|' -f1 wave.txt | tr '\n' ' '; echo; pgrep -af 'e8_cc_hessian_fd.py' | grep -o 'geoms/[A-Za-z0-9_]*' | sort -u | tr '\n' ' '" < /dev/null 2>&1 | cut -c1-240; done
  exit 0
fi
drop anc2 B_14ba9f1827 B_16116c90de
drop anc4 B_1a63ca9865
drop anc5 B_96f5f1990a
