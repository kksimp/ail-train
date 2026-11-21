import math
legs = [("abyssal plain", 1800.0, 5000.0), ("ocean ridge", 600.0, 2500.0), ("continental slope", 120.0, 400.0), ("shelf", 60.0, 50.0), ("bay", 8.0, 10.0)]
def speed_ms(depth):
    return math.sqrt(9.81 * depth)
hours = 0.0
for name, km, depth in legs:
    v = speed_ms(depth)
    t = km * 1000.0 / v / 3600.0
    hours += t
    print(f"{name:<17} {depth:>6.1f} m deep: {v * 3.6:>5.1f} km/h, {t:.2f} h")
whole = int(hours)
minutes = int((hours - float(whole)) * 60.0)
print(f"arrives after {whole} h {minutes} min")
height = 0.5 * (5000.0 / 10.0) ** 0.25
print(f"a 0.5 m wave in deep water stands about {height:.2f} m high in the bay")
