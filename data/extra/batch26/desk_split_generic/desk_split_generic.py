by_name = [("desk A", "A", "Gz"), ("desk B", "H", "Mz"), ("desk C", "N", "Zz")]
by_age = [("junior 2 km", 8, 15), ("open 5 km", 16, 59), ("veterans 5 km", 60, 99)]
def assign(ds, x):
    for n, lo, hi in ds:
        if lo <= x <= hi: return n
    return "help desk"
q = {}
for s, a in [("Okafor", 34), ("Brennan", 67), ("Haas", 12), ("Zubiri", 45), ("mcleod", 29), ("Ito", 5)]:
    d = assign(by_name, s); r = assign(by_age, a)
    q[d] = q.get(d, 0) + 1
    print(f"{s:<8} age {a:>2}: {d}, {r}")
for d, n in q.items():
    print(f"{d}: {n} in the queue")
