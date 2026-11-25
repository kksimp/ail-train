import sys

grid = [l for l in sys.stdin.read().splitlines() if l.strip()]


def land(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == '1'


seen = set()
count = 0
largest = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if not land(r, c) or (r, c) in seen:
            continue
        count += 1
        size = 0
        seen.add((r, c))
        stack = [(r, c)]
        while stack:
            cr, cc = stack.pop()
            size += 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = cr + dr, cc + dc
                if land(nr, nc) and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        largest = max(largest, size)
print(f"islands: {count}")
print(f"largest: {largest}")
