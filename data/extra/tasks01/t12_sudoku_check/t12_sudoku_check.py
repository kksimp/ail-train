import sys


def first_dup(cells):
    seen = set()
    for c in cells:
        if c == ".":
            continue
        if c in seen:
            return c
        seen.add(c)
    return None


def build_units(g):
    units = []
    for r in range(9):
        units.append((f"row {r + 1}", g[r]))
    for c in range(9):
        units.append((f"column {c + 1}", [g[r][c] for r in range(9)]))
    for b in range(9):
        r0 = b // 3 * 3
        c0 = b % 3 * 3
        cells = []
        for r in range(r0, r0 + 3):
            for c in range(c0, c0 + 3):
                cells.append(g[r][c])
        units.append((f"box {b + 1}", cells))
    return units


def well_formed(rows):
    if len(rows) != 9:
        return False
    for row in rows:
        if len(row) != 9 or not all(c == "." or "1" <= c <= "9" for c in row):
            return False
    return True


def report(rows):
    if not well_formed(rows):
        return "BAD INPUT"
    g = [list(r) for r in rows]
    for label, cells in build_units(g):
        d = first_dup(cells)
        if d is not None:
            return f"INVALID {label} digit {d}"
    empties = sum(row.count(".") for row in g)
    return "VALID complete" if empties == 0 else "VALID incomplete"


def main():
    rows = []
    for line in sys.stdin.read().splitlines():
        t = line.strip()
        if t:
            rows.append(t)
    print(report(rows))


main()
