def dec(n, d):
    w, r = divmod(n, d)
    if r == 0: return str(w)
    ds, seen = [], {}
    while r:
        if r in seen:
            a = seen[r]; return f"{w}.{''.join(ds[:a])}({''.join(ds[a:])})"
        seen[r] = len(ds); r *= 10; ds.append(str(r // d)); r %= d
    return f"{w}.{''.join(ds)}"
for a, b in [(1, 2), (1, 3), (1, 7), (22, 7), (1, 6), (5, 4), (1, 81), (3, 1)]:
    print(f"{a}/{b} = {dec(a, b)}")
best = 2
for d in range(2, 50):
    if len(dec(1, d)) > len(dec(1, best)): best = d
print(f"longest under 50: 1/{best} = {dec(1, best)}")
