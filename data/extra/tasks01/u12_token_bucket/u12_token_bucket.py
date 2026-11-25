import sys

lines = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
cap = rate = -1
if lines:
    f = lines[0].split()
    if len(f) == 4 and f[0] == "capacity" and f[2] == "rate":
        try:
            cap, rate = int(f[1]), int(f[3])
        except ValueError:
            cap = -1
if cap < 1 or rate < 0:
    print("bad header")
    sys.exit(0)
buckets = {}
stats = {}
out = []
prev = 0
for l in lines[1:]:
    f = l.split()
    ok = len(f) in (2, 3)
    if ok:
        try:
            t = int(f[0])
            cost = int(f[2]) if len(f) == 3 else 1
            ok = t >= 0 and cost >= 1 and t >= prev
        except ValueError:
            ok = False
    if not ok:
        out.append("? " + l)
        continue
    prev = t
    key = f[1]
    if key not in buckets:
        buckets[key] = [cap, t]
        stats[key] = [0, 0]
    b = buckets[key]
    b[0] = min(cap, b[0] + (t - b[1]) * rate)
    b[1] = t
    if b[0] >= cost:
        b[0] -= cost
        stats[key][0] += 1
        res = "allow"
    else:
        stats[key][1] += 1
        res = "deny"
    out.append(f"{t} {key} {cost} {res} left={b[0]}")
for k, (a, d) in stats.items():
    out.append(f"{k} allowed={a} denied={d}")
print("\n".join(out))
