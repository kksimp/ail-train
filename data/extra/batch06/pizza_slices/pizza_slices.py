W = [("Abi", 3), ("Bas", 2), ("Cat", 4), ("Dev", 1), ("Eli", 3), ("Fen", 2), ("Gio", 5)]; t = sum(w[1] for w in W); p = (t + 7) // 8; s = p * 8 - t
print(f"{t} slices wanted, {p} pizzas, {s} spare"); l = s
for n, k in sorted(W, key=lambda w: (w[1], w[0])):
    e = 1 if l > 0 else 0; l -= e; print(f"{n}: {k + e}{' (+1)' if e else ''}")
