import re
import sys
from math import gcd, isqrt


def triples_upto(n):
    out = []
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c2 = a * a + b * b
            c = isqrt(c2)
            if c * c == c2 and c <= n:
                out.append((a, b, c))
    return out


def get_arg(parts, hi):
    if len(parts) != 2 or not re.fullmatch(r"-?[0-9]+", parts[1]):
        return None
    v = int(parts[1])
    if v < 1 or v > hi:
        return None
    return v


data = sys.stdin.read().split("\n")
for idx, raw in enumerate(data):
    t = raw.strip()
    if t == "" or t.startswith("#"):
        continue
    parts = t.split()
    name = parts[0]
    limits = {"primitive": 300, "perimeter": 1000, "leg": 500}
    if name not in limits:
        print("line %d: unknown command" % (idx + 1))
        continue
    v = get_arg(parts, limits[name])
    if v is None:
        print("line %d: bad argument" % (idx + 1))
        continue
    if name == "primitive":
        al = triples_upto(v)
        prim = sorted((tr for tr in al if gcd(tr[0], tr[1]) == 1), key=lambda tr: (tr[2], tr[0]))
        print("primitive %d:" % v)
        for a, b, c in prim:
            print("  %d %d %d" % (a, b, c))
        print("  count: primitive %d, all %d" % (len(prim), len(al)))
    elif name == "perimeter":
        hits = [tr for tr in triples_upto(v) if sum(tr) == v]
        hits.sort()
        print("perimeter %d:" % v)
        for a, b, c in hits:
            print("  %d %d %d x%d" % (a, b, c, gcd(a, b)))
        print("  count: %d" % len(hits))
    else:
        hits = []
        for o in range(1, v * v + 1):
            c2 = v * v + o * o
            c = isqrt(c2)
            if c * c == c2:
                hits.append((min(o, v), max(o, v), c))
        hits.sort(key=lambda tr: tr[2])
        print("leg %d:" % v)
        for a, b, c in hits:
            print("  %d %d %d" % (a, b, c))
        print("  count: %d" % len(hits))
