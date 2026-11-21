F = [0, 0]
for i, (a, s) in enumerate([(0, 5), (1, 3), (2, 8), (3, 2), (4, 4), (6, 6), (7, 1), (9, 3)]):
    p = 0 if F[0] <= F[1] else 1; st = max(F[p], a); F[p] = st + s; print(f"customer {i + 1} (arrives {a}): counter {p + 1}, {st}-{st + s}")
print(f"all served by {max(F)}")
