import bisect
import re
import sys

lines = sys.stdin.read().splitlines()
if lines:
    xs = [int(w) for w in lines[0].split()]
    for k, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        p = line.split()
        if len(p) != 2 or p[0] not in ("find", "lower", "upper", "count") or not re.fullmatch(r"-?[0-9]+", p[1]):
            print("error line %d" % k)
            continue
        x = int(p[1])
        lo = bisect.bisect_left(xs, x)
        hi = bisect.bisect_right(xs, x)
        if p[0] == "find":
            print(lo if lo < len(xs) and xs[lo] == x else -1)
        elif p[0] == "lower":
            print(lo)
        elif p[0] == "upper":
            print(hi)
        else:
            print(hi - lo)
