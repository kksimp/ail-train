S = [("beans", 4, 6, 48, 12), ("rice", 2, 30, 36, 10), ("pasta", 2, 3, 40, 8), ("soup", 4, 20, 24, 6), ("oats", 1, 0, 20, 5)]; cs = 0
for n, a, o, c, k in sorted(S, key=lambda p: (p[1], p[0])):
    g = c - o; q = 0 if g < k else g // k * k
    if q == 0: continue
    cs += q // k; print(f"aisle {a}: {n} +{q} ({q // k} cases)")
print(f"{cs} cases to fetch")
