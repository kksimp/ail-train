def parallel(a, b):
    return a * b / (a + b)

def load_power(volts, ohms, load):
    i = volts / (ohms + load)
    return i * i * load

v = 12.0
r1 = 4000.0
r2 = 6000.0
r3 = 1000.0
tv = v * r2 / (r1 + r2)
tr = parallel(r1, r2) + r3
print(f"Vth {tv:.2f} V, Rth {tr:.0f} ohm")
best = 0.0
best_load = 0.0
for load in [500.0, 1000.0, 2000.0, 3400.0, 5000.0, 10000.0]:
    p = load_power(tv, tr, load)
    if p > best:
        best = p
        best_load = load
    direct = v * parallel(r2, r3 + load) / (r1 + parallel(r2, r3 + load)) * load / (r3 + load)
    print(f"load {load:>6.0f} ohm: {tv * load / (tr + load):.3f} V (direct {direct:.3f} V), {p * 1000.0:.3f} mW")
print(f"most power at {best_load:.0f} ohm: {best * 1000.0:.3f} mW")
