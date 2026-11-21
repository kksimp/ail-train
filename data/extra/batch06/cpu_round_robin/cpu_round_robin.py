P = [("P1", 0, 7), ("P2", 1, 4), ("P3", 2, 9), ("P4", 4, 2), ("P5", 6, 5)]; L = [p[2] for p in P]; F = [0] * 5; Q = []; a = 0; c = 0; T = []
while a < 5 and P[a][1] <= c: Q.append(a); a += 1
while Q or a < 5:
    if not Q: c = P[a][1]; Q.append(a); a += 1; continue
    p = Q.pop(0); r = min(L[p], 3); T.append(f"{P[p][0]}@{c}"); c += r; L[p] -= r
    while a < 5 and P[a][1] <= c: Q.append(a); a += 1
    if L[p] > 0: Q.append(p)
    else: F[p] = c
print(" ".join(T)); tw = 0
for i, p in enumerate(P): w = F[i] - p[1] - p[2]; tw += w; print(f"{p[0]}: finishes {F[i]}, waited {w}")
print(f"average wait {tw / 5:.1f}")
