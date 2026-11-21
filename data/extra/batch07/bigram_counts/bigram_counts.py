W = "the cat sat on the mat the cat ate the fish the dog sat on the log the cat sat on the dog".split(" "); P = {}; F = {}
for i in range(1, len(W)):
    a, b = W[i - 1], W[i]; k = f"{a} {b}"; P[k] = P.get(k, 0) + 1; F.setdefault(a, {}); F[a][b] = F[a].get(b, 0) + 1
for k in sorted(P, key=lambda k: (-P[k], k))[:4]: print(f"{k}: {P[k]}")
for w in ["the", "cat", "sat", "fish"]:
    if w in F: n = F[w]; g = sorted(n, key=lambda k: (-n[k], k))[0]; print(f"after {w}: {g} ({n[g]} of {sum(n.values())})")
    else: print(f"after {w}: no data")
