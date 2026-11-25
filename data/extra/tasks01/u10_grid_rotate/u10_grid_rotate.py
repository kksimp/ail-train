import sys
lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
grid = []
i = 0
while i < len(lines) and lines[i] != "":
    grid.append(list(lines[i])); i += 1
cmds = [l.strip() for l in lines[i + 1:] if l.strip() != ""]
for c in cmds:
    if c not in ("R", "L", "H", "V"):
        print("error: bad command " + c); sys.exit(0)
    if not grid:
        continue
    if c == "R":
        grid = [[grid[len(grid) - 1 - r][k] for r in range(len(grid))] for k in range(len(grid[0]))]
    elif c == "L":
        w = len(grid[0])
        grid = [[grid[r][w - 1 - k] for r in range(len(grid))] for k in range(w)]
    elif c == "H":
        grid = [row[::-1] for row in grid]
    else:
        grid = grid[::-1]
for row in grid:
    print("".join(row))
