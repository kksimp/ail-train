S = [1, 7, 12, 25]
for t in [14, 24, 30, 37, 50, 61]:
    B = [0]; P = [0]
    for v in range(1, t + 1):
        b = 10 ** 6; p = 0
        for s in S:
            if s <= v and B[v - s] + 1 < b: b = B[v - s] + 1; p = s
        B.append(b); P.append(p)
    u = []; v = t
    while v > 0: u.append(P[v]); v -= P[v]
    print(f"{t}: {B[t]} stamps ({' + '.join(map(str, sorted(u, reverse=True)))})")
