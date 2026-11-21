B = ["red-M", "blue-L", "red-M", "black-M", "blue-L", "black-M", "black-M", "white-S", "red-L", "blue-L", "black-M", "white-S", "blue-L", "red-M"]; c = {}
for s in B: c[s] = c.get(s, 0) + 1
tp = 0; od = []
for k in sorted(c):
    p = c[k] // 2; tp += p
    if c[k] % 2: od.append(k)
    print(f"{k}: {c[k]} socks, {p} pairs")
print(f"{tp} pairs, odd socks: {', '.join(od)}")
m = max(v // 2 for v in c.values()); print(f"most pairs ({m}): " + ", ".join(sorted(k for k in c if c[k] // 2 == m)))
