def normalise(q):
    t = " ".join(q.strip().lower().split())
    while t.endswith("?") or t.endswith("!") or t.endswith("."):
        t = t[:-1]
    return t

log = [("Return policy", 4), ("return  policy?", 4), ("track order", 2), ("TRACK ORDER", 2), ("gift card balance", 0), ("return policy", 4), ("shipping to norway", 0), ("track order!", 2), ("Gift card balance ", 0), ("size guide", 7)]
counts = {}
zero = {}
for q, results in log:
    n = normalise(q)
    counts[n] = counts.get(n, 0) + 1
    if results == 0:
        zero[n] = zero.get(n, 0) + 1
print(f"{len(log)} searches, {len(counts)} distinct after normalising")
top = sorted(counts.keys(), key=lambda k: -counts[k])[:3]
for q in top:
    print(f"  {counts[q]}x {q}")
total_zero = sum(zero.values())
pct = total_zero * 100 // len(log)
print(f"zero-result rate: {pct}%")
for q, n in zero.items():
    print(f"  no results: {q} ({n}x)")
