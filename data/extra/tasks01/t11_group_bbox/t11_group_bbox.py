import re, sys

def pint(s):
    return int(s) if re.fullmatch(r'-?[0-9]+', s) else None

g = {}
skipped = 0
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    w = t.split()
    if len(w) != 3 or pint(w[1]) is None or pint(w[2]) is None:
        skipped += 1
        continue
    x, y = int(w[1]), int(w[2])
    if w[0] in g:
        b = g[w[0]]
        b[0] = min(b[0], x); b[1] = min(b[1], y)
        b[2] = max(b[2], x); b[3] = max(b[3], y); b[4] += 1
    else:
        g[w[0]] = [x, y, x, y, 1]
for k, b in g.items():
    print(k, *b)
print(f"skipped {skipped}")
