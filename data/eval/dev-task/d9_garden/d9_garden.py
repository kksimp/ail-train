import re
import sys


def num(tok):
    return int(tok) if re.fullmatch(r"[0-9]+", tok) else None


lines = sys.stdin.read().splitlines()
toks = lines[0].split() if lines else []
dims = [num(t) for t in toks]
if len(dims) != 2 or None in dims or not all(1 <= d <= 8 for d in dims):
    print("bad header")
    sys.exit()
rows, cols = dims
plant = [[False] * cols for _ in range(rows)]
height = [[0] * cols for _ in range(rows)]
water = [[0] * cols for _ in range(rows)]
dry = [[0] * cols for _ in range(rows)]
days = blooms = dead = 0

for n, raw in enumerate(lines[1:], 2):
    line = raw.strip()
    if not line or line.startswith("#"):
        continue
    w = line.split()
    cmd = w[0]
    if cmd not in ("plant", "water", "day", "show"):
        print(f"error line {n}: unknown command")
        continue
    if cmd in ("day", "show"):
        if len(w) != 1:
            print(f"error line {n}: bad arguments")
            continue
    else:
        if len(w) != 3 or num(w[1]) is None or num(w[2]) is None:
            print(f"error line {n}: bad arguments")
            continue
        r, c = num(w[1]), num(w[2])
        if not (1 <= r <= rows and 1 <= c <= cols):
            print(f"error line {n}: out of range")
            continue
        r -= 1
        c -= 1
    if cmd == "plant":
        if plant[r][c]:
            print(f"error line {n}: cell occupied")
        else:
            plant[r][c] = True
            height[r][c] = 1
            dry[r][c] = 0
    elif cmd == "water":
        water[r][c] += 3
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                water[rr][cc] += 1
    elif cmd == "day":
        grew = died = 0
        for r in range(rows):
            for c in range(cols):
                if plant[r][c]:
                    if water[r][c] >= 2:
                        water[r][c] -= 2
                        dry[r][c] = 0
                        if height[r][c] < 9:
                            height[r][c] += 1
                            grew += 1
                            if height[r][c] == 9:
                                blooms += 1
                    else:
                        dry[r][c] += 1
                        if dry[r][c] >= 3:
                            plant[r][c] = False
                            height[r][c] = 0
                            dry[r][c] = 0
                            died += 1
        for r in range(rows):
            for c in range(cols):
                water[r][c] //= 2
        days += 1
        dead += died
        print(f"day {days}: grew {grew} died {died}")
    else:
        for r in range(rows):
            print("".join(str(height[r][c]) if plant[r][c] else "." for c in range(cols)))

alive = sum(1 for r in range(rows) for c in range(cols) if plant[r][c])
print(f"summary: blooms {blooms} dead {dead} alive {alive}")
