def nv(r, F):
    t = 0.0; f = 1.0
    for x in F: t += x / f; f *= 1.0 + r
    return t
P = [("solar roof", [-24000.0] + [3100.0] * 10), ("new oven", [-8000.0, 2500.0, 2500.0, 2500.0, 2500.0]), ("van", [-30000.0, 9000.0, 9000.0, 8000.0, 7000.0, 6000.0]), ("website", [-5000.0, 800.0, 1200.0, 1500.0, 1500.0])]
for n, v in sorted(((n, nv(0.08, F)) for n, F in P), key=lambda r: -r[1]): print(f"{n:<10} NPV {v:>10.2f} {'worth it' if v > 0.0 else 'not worth it'}")
