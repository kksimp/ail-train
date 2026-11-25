import sys
lines = sys.stdin.read().split("\n")
head = lines[0].split() if lines else []
def isd(s):
    return s != "" and all(c in "0123456789" for c in s) and len(s) < 6
if len(head) != 2 or not isd(head[0]) or not isd(head[1]) or int(head[0]) < 1 or int(head[1]) < 1:
    print("error: bad header")
    sys.exit(0)
R, C = int(head[0]), int(head[1])
names = sorted(l.strip() for l in lines[1:] if l.strip() != "")
if len(names) > R * C:
    print("error: too many students (%d > %d)" % (len(names), R * C))
    sys.exit(0)
order = []
for p in (0, 1):
    for r in range(R):
        for c in range(C):
            if c % 2 == p:
                order.append((r, c))
grid = [["........"] * C for _ in range(R)]
for n, (r, c) in zip(names, order):
    grid[r][c] = n[:8].ljust(8)
for row in grid:
    print("|".join(row))
