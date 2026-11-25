import re, sys

def pint(s):
    return int(s) if re.fullmatch(r'-?[0-9]+', s) else None

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def chain(pts):
    h = []
    for p in pts:
        while len(h) >= 2 and cross(h[-2], h[-1], p) <= 0:
            h.pop()
        h.append(p)
    return h

s = set()
for line in sys.stdin.read().splitlines():
    w = line.strip().split()
    if len(w) == 2 and pint(w[0]) is not None and pint(w[1]) is not None:
        s.add((int(w[0]), int(w[1])))
pts = sorted(s)
print(f"distinct {len(pts)}")
if len(pts) <= 2:
    print(f"hull {len(pts)}")
else:
    print(f"hull {len(chain(pts)) + len(chain(pts[::-1])) - 2}")
