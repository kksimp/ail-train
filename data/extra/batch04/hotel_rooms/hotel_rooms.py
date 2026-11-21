B = [("Amis", 1, 4), ("Bauer", 2, 3), ("Chen", 3, 6), ("Diaz", 4, 5), ("Endo", 1, 2), ("Faro", 5, 7), ("Gale", 2, 6)]
R, N = 3, 7; t = [[False] * (N + 1) for _ in range(R)]
for nm, a, l in B:
    p = next((r for r in range(R) if all(not t[r][n] for n in range(a, l))), -1)
    if p < 0: print(f"{nm}: no room for nights {a}-{l - 1}"); continue
    for n in range(a, l): t[p][n] = True
    print(f"{nm}: room {p + 101}")
print(f"rooms used per night: {[sum(1 for r in range(R) if t[r][n]) for n in range(1, N)]}")
