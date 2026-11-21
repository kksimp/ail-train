P = sorted([("yogurt", 118), ("rice", 400), ("spinach", 121), ("eggs", 126), ("milk", 122), ("cheese", 140), ("bread", 119), ("tofu", 123)], key=lambda p: (p[1], p[0]))
G = {"expired": [], "use soon": [], "fine": []}
for n, d in P:
    l = d - 120; g = "expired" if l < 0 else "use soon" if l <= 3 else "fine"; G[g].append(f"{n}({l})")
for g in G: print(f"{g}: {' '.join(G[g])}")
