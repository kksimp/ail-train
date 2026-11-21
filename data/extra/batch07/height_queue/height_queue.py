P = [(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)]; Q = []
for p in sorted(P, key=lambda p: (-p[0], p[1])): Q.insert(p[1], p)
print(" ".join(f"[{a},{b}]" for a, b in Q))
ok = all(sum(1 for q in Q[:i] if q[0] >= p[0]) == p[1] for i, p in enumerate(Q))
print(f"all counts match: {'true' if ok else 'false'}")
