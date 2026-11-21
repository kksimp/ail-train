R = [("Ali", "Rovers"), ("Bea", "United"), ("Cem", "City"), ("Dot", "Athletic")]; g = {r[0]: 0 for r in R}
for h, a in [("Rovers", "United"), ("City", "Athletic"), ("Rovers", "City"), ("United", "Athletic"), ("Rovers", "Athletic"), ("United", "City")]:
    f = [r[0] for r in R if r[1] != h and r[1] != a]; p = min(f, key=lambda n: (g[n], n)); g[p] += 1; print(f"{h} v {a}: {p}")
for r in R: print(f"{r[0]}: {g[r[0]]}")
