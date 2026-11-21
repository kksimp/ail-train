R = 8.314

def pressure(a, b, n, v, t):
    return n * R * t / (v - n * b) - a * n * n / (v * v)

gases = [("helium", 0.00346, 0.0000238), ("nitrogen", 0.137, 0.0000387), ("carbon dioxide", 0.364, 0.00004267), ("water vapour", 0.5536, 0.00003049)]
t = 300.0
for litres in [22.4, 1.0, 0.2]:
    v = litres / 1000.0
    ideal = R * t / v / 100000.0
    print(f"1 mol in {litres} L at 300 K: ideal {ideal:.2f} bar")
    for name, a, b in gases:
        p = pressure(a, b, 1.0, v, t) / 100000.0
        dev = (p / ideal - 1.0) * 100.0
        print(f"  {name:<15} {p:>8.2f} bar ({dev:>6.1f}%)")
