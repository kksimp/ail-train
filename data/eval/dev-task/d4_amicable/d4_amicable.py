import re
import sys


def s(n):
    total = 1 if n > 1 else 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            if d * d != n:
                total += n // d
        d += 1
    return total


for raw in sys.stdin.read().split("\n"):
    t = raw.strip()
    if t == "":
        continue
    if not re.fullmatch(r"-?[0-9]+", t) or not (1 <= int(t) <= 50000):
        print(t + ": invalid")
        continue
    n = int(t)
    pairs = []
    for a in range(2, n + 1):
        b = s(a)
        if a < b <= n and s(b) == a:
            pairs.append((a, b))
    print("N=%d: %d" % (n, len(pairs)))
    for a, b in pairs:
        print("  %d %d" % (a, b))
