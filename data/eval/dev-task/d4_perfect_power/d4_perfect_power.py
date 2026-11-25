import re
import sys

for raw in sys.stdin.read().split("\n"):
    t = raw.strip()
    if t == "":
        continue
    if not re.fullmatch(r"-?[0-9]+", t) or int(t) < 2 or int(t) > 10**12:
        print(t + ": invalid")
        continue
    n = int(t)
    found = None
    for e in range(40, 1, -1):
        r = round(n ** (1.0 / e))
        for b in (r - 1, r, r + 1):
            if b >= 2 and b ** e == n:
                found = (b, e)
                break
        if found:
            break
    if found:
        print("%d = %d^%d" % (n, found[0], found[1]))
    else:
        print("%d is not a perfect power" % n)
