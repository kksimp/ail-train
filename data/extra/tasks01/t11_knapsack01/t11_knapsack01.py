import re, sys

def pint(s):
    return int(s) if re.fullmatch(r'-?[0-9]+', s) else None

LIMIT = 10000
cap = None
have = False
items = []
skipped = 0
for line in sys.stdin.read().splitlines():
    t = line.strip()
    if not t:
        continue
    if not have:
        have = True
        cap = pint(t)
        continue
    w = t.split()
    if len(w) == 2 and pint(w[0]) is not None and pint(w[1]) is not None \
            and int(w[0]) >= 1 and int(w[1]) >= 0:
        items.append((int(w[0]), int(w[1])))
    else:
        skipped += 1
if cap is None or cap < 0 or cap > LIMIT:
    print("bad capacity")
    sys.exit(0)
dp = [0] * (cap + 1)
for wt, v in items:
    for c in range(cap, wt - 1, -1):
        dp[c] = max(dp[c], dp[c - wt] + v)
best = dp[cap]
weight = next(c for c in range(cap + 1) if dp[c] == best)
print(f"items {len(items)}")
print(f"skipped {skipped}")
print(f"best {best}")
print(f"weight {weight}")
