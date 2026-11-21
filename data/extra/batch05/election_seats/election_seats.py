V = [("Red", 34000), ("Blue", 29000), ("Green", 12500), ("Gold", 8100)]; W = {v[0]: 0 for v in V}; T = sum(v[1] for v in V)
for s in range(1, 10):
    b = max(V, key=lambda v: v[1] * 1000 // (W[v[0]] + 1)); W[b[0]] += 1; print(f"seat {s}: {b[0]}")
for n, c in V: print(f"{n}: {W[n]} seats ({c * 100 // T}% of votes)")
