import sys

lines = sys.stdin.read().split("\n")
grid = []
i = 0
while i < len(lines) and lines[i].strip() != "":
    grid.append([c for c in lines[i].strip()])
    i += 1
moves_line = ""
if i + 1 < len(lines):
    moves_line = lines[i + 1].strip()
if not grid or any(len(r) != len(grid[0]) for r in grid) or any(c not in "0123456789" for r in grid for c in r):
    print("invalid grid")
    sys.exit(0)
R, C = len(grid), len(grid[0])

def region():
    col = grid[0][0]
    seen = {(0, 0)}
    stack = [(0, 0)]
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and grid[nr][nc] == col:
                seen.add((nr, nc))
                stack.append((nr, nc))
    return seen

moves = moves_line.split(" ") if moves_line else []
for k, m in enumerate(moves, 1):
    if len(m) != 1 or m not in "0123456789":
        print("invalid move %d" % k)
        continue
    for (r, c) in region():
        grid[r][c] = m
    print("move %d colour %s region %d" % (k, m, len(region())))
print("flooded" if len(region()) == R * C else "not flooded")
