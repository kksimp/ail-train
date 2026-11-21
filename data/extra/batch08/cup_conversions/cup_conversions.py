def am(t):
    s = 0.0
    for p in t.split(" "):
        if "/" in p: a, b = p.split("/"); s += float(a) / float(b)
        else: s += float(p)
    return s
P = {"flour": 120.0, "sugar": 200.0, "butter": 226.0, "oats": 90.0, "honey": 340.0}; T = 0.0
for c, w in [("2 1/4", "flour"), ("3/4", "sugar"), ("1/2", "butter"), ("1 1/3", "oats"), ("1/3", "honey")]:
    g = am(c) * P[w]; T += g; print(f"{c} cup {w}: {g:.0f} g")
print(f"total {T:.0f} g")
