"""Double check before s1 is deleted (28 Oct): is every file on s1 (outside miniforge3 and the pip/conda download cache) present on the
laptop with the same sha256 content, anywhere under the plan-05 tree? Content-addressed, so a file counts wherever its copy lives.
Prints per top-level directory on s1: files, found, missing; then every missing path."""
import collections
import hashlib
import os
import sys

SP = os.path.dirname(os.path.abspath(__file__))
PLAN = r"C:\Users\thebr\Documents\CapstonePlan\plans\05_delta-probed-ir-pipeline"
SKIP_DIRS = {".git", "node_modules", "website"}

remote = []
with open(os.path.join(SP, "s1_sha.txt"), encoding="utf-8") as fh:
    for line in fh:
        parts = line.rstrip("\n").split("  ", 1)
        if len(parts) == 2 and len(parts[0]) == 64:
            remote.append((parts[0], parts[1]))
sizes = {}
with open(os.path.join(SP, "s1_sizes.tsv"), encoding="utf-8") as fh:
    for line in fh:
        s, p = line.rstrip("\n").split("\t", 1)
        sizes[p] = int(s)
if len(remote) != len(sizes):
    sys.exit(f"listings differ: {len(remote)} hashes, {len(sizes)} sizes")
wanted_sizes = set(sizes.values())

local = set()
n_hashed = 0
for root, dirs, files in os.walk(PLAN):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in files:
        p = os.path.join(root, f)
        try:
            if os.path.getsize(p) not in wanted_sizes:
                continue
            h = hashlib.sha256()
            with open(p, "rb") as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(chunk)
            local.add(h.hexdigest())
            n_hashed += 1
        except OSError:
            continue

per_dir = collections.defaultdict(lambda: [0, 0])
missing = []
for sha, path in remote:
    top = path.split("/")[1] if path.count("/") > 1 else path
    per_dir[top][0] += 1
    if sha in local:
        per_dir[top][1] += 1
    else:
        missing.append((top, path, sizes[path]))
print(f"s1: {len(remote)} files; laptop files hashed (size-matched): {n_hashed}")
for top, (n, found) in sorted(per_dir.items()):
    print(f"  {top:40s} {n:5d} files, {found:5d} found, {n - found:5d} missing")
print(f"missing: {len(missing)} files, {sum(m[2] for m in missing)} bytes")
with open(os.path.join(SP, "s1_missing.tsv"), "w", encoding="utf-8") as fh:
    for top, path, size in missing:
        fh.write(f"{size}\t{path}\n")
