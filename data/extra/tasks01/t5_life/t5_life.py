import re
import sys

lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
if not lines or not re.fullmatch(r"[0-9]+", lines[0]):
    print("bad steps")
    sys.exit(0)
steps = int(lines[0])
width = max((len(l) for l in lines[1:]), default=0)
grid = [[1 if c < len(l) and l[c] == '#' else 0 for c in range(width)] for l in lines[1:]]


def step(g):
    out = []
    for r in range(len(g)):
        row = []
        for c in range(len(g[r])):
            n = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(g) and 0 <= nc < len(g[nr]):
                        n += g[nr][nc]
            alive = (n == 2 or n == 3) if g[r][c] == 1 else n == 3
            row.append(1 if alive else 0)
        out.append(row)
    return out


for _ in range(steps):
    grid = step(grid)
for row in grid:
    print("".join("#" if v else "." for v in row))
