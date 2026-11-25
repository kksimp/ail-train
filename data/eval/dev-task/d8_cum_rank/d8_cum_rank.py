import re
import sys
from collections import Counter

toks = sys.stdin.read().split()
for t in toks:
    if not re.fullmatch(r"-?[0-9]+", t):
        print("bad value: " + t)
        sys.exit(0)
vals = [int(t) for t in toks]
if not vals:
    print("no data")
    sys.exit(0)
n = len(vals)
cnt = Counter(vals)
print("n: %d" % n)
cum = 0
for v in sorted(cnt):
    cum += cnt[v]
    print("%d\t%d\t%d\t%d%%" % (v, cnt[v], cum, (cum * 200 + n) // (2 * n)))
