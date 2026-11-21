sc = lambda g, f, t: (g * t * 2 + f) // (f * 2)
def show(g): return f"{g // 1000}.{g % 1000 // 10:02d} kg" if g >= 1000 else f"{g} g"
r = [("flour", 500), ("butter", 125), ("sugar", 90), ("salt", 3), ("oats", 350)]
for s in [2, 6, 12]:
    print(f"serves {s}: " + ", ".join(f"{n} {show(sc(g, 4, s))}" for n, g in r))
print(f"total for 10: {show(sum(sc(g, 4, 10) for _, g in r))}")
