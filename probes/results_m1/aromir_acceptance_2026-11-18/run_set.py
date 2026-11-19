"""TASKS 269 criteria 1 and 2: run one tool over the fixed set, one molecule after another, each with its wall time and peak memory.

    python run_set.py aromir <aromir executable> <fixed_set.json> <out folder> [--only benzene] [--threads 4] [--dry-run]
    python run_set.py m08 <python with m08> <fixed_set.json> <out folder> [--only benzene] [--threads 4] [--dry-run]

A molecule whose certificate.json exists is skipped, so a stopped run resumes. Each molecule's command, exit code, wall time and
peak memory (GNU time in WSL; on Windows psutil over the process tree, sampled each second) go to <out>/runs.jsonl; the log lines start with '[set] '.
--dry-run prints the commands and checks the inputs; it runs nothing. Registration: GoalGathering/notes/
PreRegistration_2026-11-18_aromir_Acceptance.md.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

M08_DIR = Path(__file__).resolve().parents[3] / "modules" / "08_industry_synthesis"


@dataclass(frozen=True)
class Molecule:
    name: str
    smiles: str


def molecules(path: Path) -> list[Molecule]:
    """The set, each molecule once (benzene is also in hold-out (a)), named by corpus id or by its place among the new ones."""
    rows = json.loads(path.read_text(encoding="utf-8"))["molecules"]
    seen, out = set(), []
    for k, row in enumerate(rows):
        if row["smiles"] in seen:
            continue
        seen.add(row["smiles"])
        out.append(Molecule(row.get("id") or f"new{k:02d}", row["smiles"]))
    return out


def command(tool: str, program: str, molecule: Molecule, out: Path, threads: int) -> tuple[list[str], Path | None]:
    if tool == "aromir":
        return [program, "spectrum", molecule.smiles, "--out", str(out), "--threads", str(threads), "--max-memory-mb", "2048"], None
    return ([program, "-m", "m08.pipeline", "--name", molecule.name, "--smiles", molecule.smiles, "--out", str(out.parent),
             "--threads", str(threads), "--psi4-memory-gb", "4", "--wsl-cap-mb", "6144"], M08_DIR)


def run_linux(cmd: list[str], log, timing: Path) -> tuple[int, float]:
    """Run under GNU time (WSL has no psutil in these environments); return the exit code and the peak RSS in GB."""
    code = subprocess.run(["/usr/bin/time", "-o", str(timing), "-f", "%M", *cmd], stdout=log, stderr=subprocess.STDOUT,
                          check=False).returncode
    return code, int(timing.read_text(encoding="utf-8").split()[-1]) * 1024 / 1e9


def run_windows(cmd: list[str], cwd: Path | None, log) -> tuple[int, float]:
    """Run, sampling the process tree's summed RSS each second; return the exit code and its peak in GB."""
    import psutil  # Windows only: the WSL environments lack it
    process = psutil.Popen(cmd, cwd=cwd, stdout=log, stderr=subprocess.STDOUT)
    peak = 0
    while process.poll() is None:
        try:
            tree = [process, *process.children(recursive=True)]
            peak = max(peak, sum(p.memory_info().rss for p in tree if p.is_running()))
        except psutil.Error:
            pass
        time.sleep(1.0)
    return process.returncode, peak / 1e9


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("tool", choices=("aromir", "m08"))
    ap.add_argument("program")
    ap.add_argument("set", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--only", default=None)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    a.out = a.out.resolve()                     # the pipeline runs in its own folder: every path it is given is absolute
    todo =[m for m in molecules(a.set) if a.only in (None, m.name, m.smiles)]
    if not todo:
        raise SystemExit(f"no molecule of {a.set} is {a.only}")
    a.out.mkdir(parents=True, exist_ok=True)
    print(f"[set] {a.tool}: {len(todo)} molecule(s) into {a.out}", flush=True)
    for molecule in todo:
        folder = a.out / molecule.name if a.tool == "aromir" else a.out / molecule.name / molecule.name
        cmd, cwd = command(a.tool, a.program, molecule, folder, a.threads)
        if (folder / "certificate.json").exists():
            print(f"[set] skip {molecule.name}: done before", flush=True)
            continue
        if a.dry_run:
            print(f"[set] would run {molecule.name}: {' '.join(cmd)} (in {cwd or '.'})", flush=True)
            continue
        print(f"[set] start {molecule.name} {molecule.smiles}", flush=True)
        start = time.time()
        with (a.out / f"{molecule.name}.{a.tool}.log").open("w", encoding="utf-8") as log:
            if sys.platform != "win32":
                code, gb = run_linux(cmd, log, a.out / f"{molecule.name}.time")
            else:
                code, gb = run_windows(cmd, cwd, log)
        row = {"tool": a.tool, "name": molecule.name, "smiles": molecule.smiles, "exit": code, "wall_s": round(time.time() - start, 1),
               "peak_rss_gb": round(gb, 2), "command": cmd}
        with (a.out / "runs.jsonl").open("a", encoding="utf-8") as runs:
            runs.write(json.dumps(row) + "\n")
        print(f"[set] done {molecule.name}: exit {code}, {row['wall_s']} s, {row['peak_rss_gb']} GB", flush=True)
    print("[set] end", flush=True)
    sys.exit(0)


if __name__ == "__main__":
    main()
