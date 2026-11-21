def parallel(a, b):
    return a * b / (a + b)

def divide(vin, r1, r2):
    return vin * r2 / (r1 + r2)

vin = 12.0
for pr in [[10000, 10000], [10000, 4700], [2200, 1000], [47000, 33000]]:
    v = divide(vin, float(pr[0]), float(pr[1]))
    print(f"R1 {pr[0]:>6} R2 {pr[1]:>6}: {v:.3f} V unloaded")
ideal = divide(vin, 10000.0, 4700.0)
for load in [1000, 10000, 100000, 1000000]:
    eff = parallel(4700.0, float(load))
    out = divide(vin, 10000.0, eff)
    sag = (ideal - out) / ideal * 100.0
    print(f"load {load:>7} ohm: {out:.3f} V, {sag:>5.1f}% low")
