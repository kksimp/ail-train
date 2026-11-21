import math
R = 8.314

def mixing(gases):
    total = 0.0
    for g in gases:
        total = total + g[1]
    s = 0.0
    for name, n in gases:
        x = n / total
        s -= R * n * math.log(x)
    return s

mixes = [[("N2", 1.0), ("O2", 1.0)], [("N2", 0.78), ("O2", 0.21), ("Ar", 0.01)], [("He", 0.1), ("Ne", 1.9)], [("H2", 1.0), ("N2", 1.0), ("O2", 1.0), ("CO2", 1.0)]]
for mix in mixes:
    names = " and ".join(f"{n} {name}" for name, n in mix)
    ds = mixing(mix)
    tot = 0.0
    for g in mix:
        tot = tot + g[1]
    per = ds / tot
    print(f"{names}: dS {ds:.3f} J/K, {per:.3f} J/K per mole")
q = 1000.0
for th, tc in [(400.0, 300.0), (600.0, 300.0), (301.0, 300.0)]:
    print(f"1 kJ from {th:.0f} K to {tc:.0f} K: dS {q / tc - q / th:.4f} J/K")
