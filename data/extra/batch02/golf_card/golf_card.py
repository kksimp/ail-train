def nm(d):
    m = {-3: "albatross", -2: "eagle", -1: "birdie", 0: "par", 1: "bogey", 2: "double bogey"}
    if d in m: return m[d]
    return "condor" if d < -3 else f"+{d}"
pars = [4, 3, 5, 4, 4, 3, 5, 4, 4]; st = [4, 2, 6, 7, 3, 3, 3, 5, 4]
names = {}
for i, (p, g) in enumerate(zip(pars, st)):
    n = nm(g - p); names[n] = names.get(n, 0) + 1
    print(f"hole {i + 1}: par {p}, {g} strokes, {n}")
t = sum(st); d = t - sum(pars)
print(f"round: {t} ({'+' + str(d) if d > 0 else 'E' if d == 0 else str(d)})")
for k, v in names.items():
    print(f"  {k}: {v}")
