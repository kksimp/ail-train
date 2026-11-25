import sys


def mins(s):
    t = s.split(":")
    if len(t) != 2 or any(len(x) != 2 or not (x.isascii() and x.isdigit()) for x in t):
        return -1
    h, m = int(t[0]), int(t[1])
    if h > 23 or m > 59:
        return -1
    return h * 60 + m


def clock(m):
    return "%02d:%02d" % (m // 60, m % 60)


routes = {}
for k, line in enumerate(sys.stdin.read().split("\n"), 1):
    w = line.split()
    if not w:
        continue
    m = mins(w[1]) if len(w) == 2 else -1
    if m < 0:
        print("line %d: bad" % k)
        continue
    routes.setdefault(w[0], []).append(m)

for route, ts in routes.items():
    ts.sort()
    if len(ts) < 2:
        print("%s n=%d no headway" % (route, len(ts)))
        continue
    gaps = [ts[i] - ts[i - 1] for i in range(1, len(ts))]
    hi, lo = max(gaps), min(gaps)
    i = gaps.index(hi)
    avg = (sum(gaps) * 2 + len(gaps)) // (2 * len(gaps))
    print("%s n=%d min=%d max=%d avg=%d longest=%s-%s" % (route, len(ts), lo, hi, avg, clock(ts[i]), clock(ts[i + 1])))
