import sys

DIRS = [("E", 0, 1), ("SE", 1, 1), ("S", 1, 0), ("SW", 1, -1),
        ("W", 0, -1), ("NW", -1, -1), ("N", -1, 0), ("NE", -1, 1)]

lines = sys.stdin.read().split("\n")
grid = []
i = 0
while i < len(lines) and lines[i].strip() != "":
    grid.append(lines[i].strip())
    i += 1
words = [l.strip() for l in lines[i:] if l.strip() != ""]

valid = len(grid) > 0 and all(len(g) == len(grid[0]) for g in grid) and \
    all(all("a" <= c <= "z" for c in g) for g in grid)
if not valid:
    print("invalid grid")
    sys.exit(0)

R, C = len(grid), len(grid[0])

def find(w):
    for r in range(R):
        for c in range(C):
            for name, dr, dc in DIRS:
                ok = True
                for k in range(len(w)):
                    rr, cc = r + dr * k, c + dc * k
                    if not (0 <= rr < R and 0 <= cc < C) or grid[rr][cc] != w[k]:
                        ok = False
                        break
                if ok:
                    return "%d,%d %s" % (r + 1, c + 1, name)
    return None

for w in words:
    res = find(w)
    print("%s: %s" % (w, res if res else "not found"))
