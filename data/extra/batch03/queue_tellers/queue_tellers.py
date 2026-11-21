C = [(0, 5), (1, 3), (2, 8), (3, 2), (4, 4), (6, 6), (7, 1), (9, 3)]
fa = [0, 0]; w = []
for i, (a, s) in enumerate(C):
    t = 1 if fa[1] < fa[0] else 0
    st = max(a, fa[t]); fa[t] = st + s; w.append(st - a)
    print(f"customer {i + 1}: teller {t + 1}, starts {st}, waits {st - a}")
x = sum(w) * 10 // len(w)
print(f"average wait {x // 10}.{x % 10} min, longest {max(w)}")
print(f"all done at minute {max(fa)}")
