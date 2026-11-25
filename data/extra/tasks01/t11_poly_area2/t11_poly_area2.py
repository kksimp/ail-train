import re, sys

def pint(s):
    return int(s) if re.fullmatch(r'-?[0-9]+', s) else None

n = 0
have = False
pts = []
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    if not have:
        have = True
        v = pint(t)
        n = max(v, 0) if v is not None else 0
        continue
    if len(pts) >= n:
        break
    w = t.split()
    if len(w) != 2:
        continue
    x, y = pint(w[0]), pint(w[1])
    if x is None or y is None:
        continue
    pts.append((x, y))
s = 0
for i in range(len(pts)):
    j = (i + 1) % len(pts)
    s += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
o = "ccw" if s > 0 else "cw" if s < 0 else "degenerate"
print(f"doubled_area {abs(s)}")
print(f"orientation {o}")
