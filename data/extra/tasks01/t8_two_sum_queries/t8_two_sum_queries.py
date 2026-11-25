import re
import sys

lines = sys.stdin.read().splitlines()
if lines:
    xs = [int(w) for w in lines[0].split()]
    for line in lines[1:]:
        t = line.strip()
        if not t:
            continue
        if not re.fullmatch(r"-?[0-9]+", t):
            print("bad query")
            continue
        target = int(t)
        first = {}
        ans = "none"
        for j, v in enumerate(xs):
            if target - v in first:
                ans = "%d %d" % (first[target - v], j)
                break
            first.setdefault(v, j)
        print(ans)
