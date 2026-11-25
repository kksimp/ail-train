import re, sys

def pint(s):
    return int(s) if re.fullmatch(r'-?[0-9]+', s) else None

pts = []
skipped = 0
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    w = t.split()
    if len(w) == 2 and pint(w[0]) is not None and pint(w[1]) is not None:
        pts.append((int(w[0]), int(w[1])))
    else:
        skipped += 1
print(f"points {len(pts)}")
print(f"skipped {skipped}")
if len(pts) < 2:
    print("closest none")
else:
    best = None
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2
            if best is None or d < best[0]:
                best = (d, i + 1, j + 1)
    print(f"closest {best[1]} {best[2]} {best[0]}")
