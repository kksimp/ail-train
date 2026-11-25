import sys
def dg(s, lo, hi):
    return lo <= len(s) <= hi and all(c in "0123456789" for c in s)
def secs(t):
    p = t.split(":")
    if len(p) == 2:
        if not (dg(p[0], 1, 2) and dg(p[1], 2, 2)): return None
        m, s = int(p[0]), int(p[1])
        if m >= 60 or s >= 60: return None
        return m * 60 + s
    if len(p) == 3:
        if not (dg(p[0], 1, 2) and dg(p[1], 2, 2) and dg(p[2], 2, 2)): return None
        h, m, s = int(p[0]), int(p[1]), int(p[2])
        if m >= 60 or s >= 60: return None
        return h * 3600 + m * 60 + s
    return None
best = None
n = 0
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    f = line.split()
    if not f:
        continue
    if len(f) != 2 or not dg(f[0], 1, 6) or int(f[0]) < 1:
        print("line %d: invalid" % k); continue
    t = secs(f[1])
    if t is None or t == 0:
        print("line %d: invalid" % k); continue
    m = int(f[0])
    pace = (t * 2000 + m) // (2 * m)
    tenths = (m * 72 + t) // (2 * t)
    print("%dm %s -> %d:%02d/km %d.%d km/h" % (m, f[1], pace // 60, pace % 60, tenths // 10, tenths % 10))
    n += 1
    key = t * 1000 / m
    if best is None or t * best[1] < best[0] * m:
        best = (t, m, pace, k)
if best is None:
    print("no runs")
else:
    print("fastest: %d:%02d/km (line %d)" % (best[2] // 60, best[2] % 60, best[3]))
