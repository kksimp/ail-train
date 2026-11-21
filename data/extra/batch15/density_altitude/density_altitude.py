def pressure_alt(f): return f[1] + (1013 - f[2]) * 30
def tdiv(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q
def density_alt(f):
    pa = pressure_alt(f)
    isa = 15 - tdiv(2 * pa, 1000)
    return pa + 120 * (f[3] - isa)
fields = [("Seaside", 20, 1021, 12), ("Seaside summer", 20, 1009, 34), ("Highland", 4200, 1015, 22), ("Mountain", 7800, 1006, 28)]
base_roll = 900
for f in fields:
    pa = pressure_alt(f); da = density_alt(f)
    roll = base_roll + tdiv(base_roll * max(da, 0), 10000)
    print(f"{f[0]:<15} PA {pa:>5} ft, DA {da:>6} ft, roll about {roll} m")
worst = max(fields, key=lambda f: density_alt(f))
print(f"hardest take-off: {worst[0]}")
