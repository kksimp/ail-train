import re
import sys

vals = []
bad = 0
for line in sys.stdin.read().splitlines():
    s = line.strip()
    if not s:
        continue
    if re.fullmatch(r"-?[0-9]+", s):
        vals.append(int(s))
    else:
        bad += 1


def tenths(v):
    return ("-" if v < 0 else "") + f"{abs(v) // 10}.{abs(v) % 10}"


print(f"count {len(vals)}")
print(f"skipped {bad}")
if vals:
    n = len(vals)
    t = sum(vals)
    q = (abs(t) * 2 + n) // (2 * n)
    mean = -q if t < 0 else q
    print("range", tenths(min(vals)), tenths(max(vals)))
    print("mean", tenths(mean))
    print("above", sum(1 for x in vals if x > mean))
