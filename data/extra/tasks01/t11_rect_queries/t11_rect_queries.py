import re, sys

def ints(t):
    out = []
    for w in t.split():
        if not re.fullmatch(r'-?[0-9]+', w):
            return None
        out.append(int(w))
    return out

have = False
a = b = c = d = 0
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    if not have:
        v = ints(t)
        if v is None or len(v) != 4:
            print("no rectangle")
            sys.exit(0)
        have = True
        lx, hx = min(v[0], v[2]), max(v[0], v[2])
        ly, hy = min(v[1], v[3]), max(v[1], v[3])
        continue
    q = ints(t)
    if q is None or len(q) != 2:
        print("bad"); d += 1; continue
    x, y = q
    if x < lx or x > hx or y < ly or y > hy:
        print("outside"); c += 1
    elif x == lx or x == hx or y == ly or y == hy:
        print("boundary"); b += 1
    else:
        print("inside"); a += 1
if not have:
    print("no rectangle")
else:
    print(f"inside {a} boundary {b} outside {c} bad {d}")
