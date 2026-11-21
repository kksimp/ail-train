def pt(c, s): return 0 if not c else max(2, 10 - s // 5)
S = {}
for w, q, ok, s in [("Ana", 1, True, 4), ("Ben", 1, True, 12), ("Cy", 1, False, 3), ("Ana", 2, False, 20), ("Ben", 2, True, 7), ("Cy", 2, True, 2), ("Ana", 3, True, 45), ("Ben", 3, True, 31), ("Cy", 3, True, 9)]:
    p = pt(ok, s); S[w] = S.get(w, 0) + p; print(f"q{q} {w}: {'right' if ok else 'wrong'} in {s}s, +{p}")
for n in sorted(S, key=lambda k: (-S[k], k)): print(f"{n}: {S[n]}")
