V = {}
for ls, v in [("aeioulnstr", 1), ("dg", 2), ("bcmp", 3), ("fhvwy", 4), ("k", 5), ("jx", 8), ("qz", 10)]:
    for c in ls: V[c] = v
def sc(w, d, m): return sum(V[c] * (2 if i == d else 1) for i, c in enumerate(w)) * m
for w in ["quiz", "jazz", "oxen", "rhythm", "cabbage"]: print(f"{w}: {sc(w, -1, 1)}")
P = [("quiz", 0, 1), ("jazz", -1, 2), ("oxen", 1, 3)]; b = max(P, key=lambda p: sc(*p)); print(f"best play: {b[0]} for {sc(*b)}")
