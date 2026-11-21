O = [("Mira", [("loaf", 2), ("bun", 6)]), ("Noor", [("bun", 12), ("pie", 1)]), ("Olu", [("loaf", 1), ("pie", 2), ("bun", 4)]), ("Pia", [("loaf", 3)])]
T = {"loaf": 4, "bun": 12, "pie": 2}; F = {"loaf": 500, "bun": 60, "pie": 250}; w = {}
for _, ls in O:
    for p, n in ls: w[p] = w.get(p, 0) + n
g = 0
for p in ["loaf", "bun", "pie"]:
    tr = -(-w[p] // T[p]); m = tr * T[p]; g += m * F[p]; print(f"{p}: ordered {w[p]}, {tr} trays, {m - w[p]} spare")
print(f"flour: {g // 1000}.{g % 1000:03} kg")
