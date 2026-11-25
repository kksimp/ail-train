import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if not lines:
    sys.exit(0)

toks = lines[0].split()
if any(t not in ("l", "r", "c") for t in toks):
    print("bad spec")
    sys.exit(0)

rows = []
for line in lines[1:]:
    if not line.split():
        continue
    rows.append([c.strip(" \t") for c in line.split("|")])

ncols = max((len(r) for r in rows), default=0)
widths = [max((len(r[j]) for r in rows if j < len(r)), default=0) for j in range(ncols)]


def pad(cell, width, a):
    gap = width - len(cell)
    if a == "l":
        return cell + " " * gap
    if a == "r":
        return " " * gap + cell
    left = gap // 2
    return " " * left + cell + " " * (gap - left)


for r in rows:
    cells = []
    for j in range(ncols):
        cell = r[j] if j < len(r) else ""
        a = toks[j] if j < len(toks) else "l"
        cells.append(pad(cell, widths[j], a))
    print(" | ".join(cells).rstrip(" "))
