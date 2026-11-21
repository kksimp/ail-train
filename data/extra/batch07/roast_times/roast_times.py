R = {"beef": (40, 20, 20), "lamb": (50, 25, 15), "pork": (60, 30, 20), "chicken": (45, 20, 15)}
for k, g in [("beef", 1800), ("lamb", 2200), ("pork", 1500), ("chicken", 2000)]:
    p, e, r = R[k]; c = p * g // 1000 + e; s = 1110 - c - r; print(f"{k:<8} {g} g: cook {c} min, rest {r}, oven in at {s // 60:02}:{s % 60:02}")
