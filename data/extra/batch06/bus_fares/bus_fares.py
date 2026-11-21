def fa(z): return {1: 180, 2: 240, 3: 310}.get(z, 380)
S = {}
for w, z in [("Ivy", 1), ("Joe", 3), ("Ivy", 2), ("Ivy", 1), ("Joe", 4), ("Ivy", 3), ("Kim", 2), ("Joe", 1)]:
    b = S.get(w, 0); f = fa(z); c = 690 - b if b + f > 690 else f; S[w] = b + c; print(f"{w} {z} zones: {c}{' (capped)' if c < f else ''}")
for w in sorted(S): print(f"{w}: {S[w] // 100}.{S[w] % 100:02}")
