"""What the Basis Set Exchange's ano-pVnZ files are (TASKS 319, idea 1): their shapes, and whether the family is nested.

Two readings per pair of members and element, per angular momentum: whether the k-th contracted function of the smaller is the
k-th of the larger (a family cut from one ordered list of natural orbitals), and how much of each function of the smaller lies
outside the space the larger one's functions span (1 − the squared norm of its projection, from the primitives' analytic
overlaps; 0 = the smaller set is a subspace of the larger). Two files with the same content are one member under two names.

    python -I basis_family_check.py <folder with <name>.nwchem.txt files>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np

NAMES = ("ano-pvdz", "ano-pvtz", "ano-pvqz", "ano-pv5z")
LETTERS = "SPDFGHI"
Function = tuple[tuple[float, float], ...]


def parse_nwchem(text: str) -> dict[str, dict[str, list[Function]]]:
    """element -> shell letter -> contracted functions, each a tuple of (exponent, coefficient), zero coefficients left out."""
    found: dict[str, dict[str, list[Function]]] = {}
    columns: list[list[tuple[float, float]]] = []
    for line in text.splitlines():
        header = re.fullmatch(r"\s*([A-Z][a-z]?)\s+([SPDFGHI])\s*", line)
        if header:
            columns = []
            current = found.setdefault(header.group(1), {}).setdefault(header.group(2), [])
            current_start = len(current)
            continue
        fields = line.replace("D", "E").split()
        if not fields or line.lstrip().startswith(("#", "BASIS", "END")):
            continue
        try:
            numbers = [float(field) for field in fields]
        except ValueError:
            continue
        if not columns:
            columns = [[] for _ in numbers[1:]]
        if len(numbers) - 1 != len(columns):
            raise SystemExit(f"a row with {len(numbers) - 1} coefficients in a block of {len(columns)}: {line!r}")
        for column, coefficient in zip(columns, numbers[1:], strict=True):
            if coefficient != 0.0:
                column.append((numbers[0], coefficient))
        del current[current_start:]
        current.extend(tuple(column) for column in columns)
    return found


def shape(shells: dict[str, list[Function]]) -> str:
    """'[3s2p1d] on 16s10p5d' for one element."""
    order = sorted(shells, key=LETTERS.index)
    contracted = "".join(f"{len(shells[letter])}{letter.lower()}" for letter in order)
    primitives = "".join(f"{len({e for f in shells[letter] for e, _ in f})}{letter.lower()}" for letter in order)
    return f"[{contracted}] on {primitives}"


def largest_difference(small: list[Function], large: list[Function]) -> float | None:
    """Largest |coefficient difference| between the functions of `small` and the first ones of `large`; None if they do not pair."""
    if len(small) > len(large):
        return None
    worst = 0.0
    for ours, theirs in zip(small, large, strict=False):
        if [e for e, _ in ours] != [e for e, _ in theirs]:
            return None
        sign = 1.0 if ours[0][1] * theirs[0][1] > 0 else -1.0
        worst = max(worst, *(abs(a - sign * b) for (_, a), (_, b) in zip(ours, theirs, strict=True)))
    return worst


def overlap(a: Function, b: Function, l: int) -> float:
    """Overlap of two contracted functions of angular momentum l, their primitives normalised."""
    power = l + 1.5
    return sum(ca * cb * (2.0 * (ea * eb) ** 0.5 / (ea + eb)) ** power for ea, ca in a for eb, cb in b)


def outside_span(small: list[Function], large: list[Function], l: int) -> float:
    """Largest share of a function of `small` that lies outside the span of `large` (1.0 when `large` has none)."""
    if not large:
        return 1.0
    metric = np.array([[overlap(a, b, l) for b in large] for a in large])
    worst = 0.0
    for function in small:
        cross = np.array([overlap(function, b, l) for b in large])
        worst = max(worst, 1.0 - float(cross @ np.linalg.solve(metric, cross)) / overlap(function, function, l))
    return worst


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        raise SystemExit(__doc__)
    sets = {name: parse_nwchem((Path(argv[0]) / f"{name}.nwchem.txt").read_text(encoding="utf-8")) for name in NAMES}
    for name, elements in sets.items():
        print(name + ": " + "; ".join(f"{element} {shape(shells)}" for element, shells in elements.items()))
    print("same content under two names:",
          ", ".join(f"{a} = {b}" for i, a in enumerate(NAMES) for b in NAMES[i + 1:] if sets[a] == sets[b]) or "none")
    for small in NAMES:
        for large in NAMES[NAMES.index(small) + 1:]:
            for element, shells in sets[small].items():
                worst = [largest_difference(functions, sets[large].get(element, {}).get(letter, []))
                         for letter, functions in shells.items()]
                said = "does not pair" if None in worst else f"largest coefficient difference {max(worst):.1e}"
                outside = {letter: outside_span(functions, sets[large].get(element, {}).get(letter, []), LETTERS.index(letter))
                           for letter, functions in shells.items()}
                spans = ", ".join(f"{letter.lower()} {value:.1e}" for letter, value in outside.items())
                print(f"{small} in {large}, {element}: function by function {said}; outside the larger span: {spans}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
