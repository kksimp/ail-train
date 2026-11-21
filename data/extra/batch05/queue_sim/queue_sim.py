C = [(0, 4), (1, 3), (2, 6), (8, 2), (9, 5), (10, 1), (18, 3), (20, 2)]; fa = 0; W = []
for i, (a, s) in enumerate(C):
    st = max(a, fa); w = st - a; W.append(w); fa = st + s; print(f"customer {i + 1}: arrives {a}, starts {st}, waits {w}")
print(f"average wait {sum(W) / len(W):.2f}, longest {max(W)}, till free at {fa}")
