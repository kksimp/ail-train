import math
def pk(v):
    if v < 3.0 or v > 25.0: return 0.0
    p = 0.5 * 1.225 * (3.141592653589793 * 40.0 * 40.0) * v * v * v * 0.4 / 1000.0
    return 2000.0 if p > 2000.0 else p
for v in [2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 15.0, 20.0, 26.0]:
    p = pk(v); s = "stopped" if p == 0.0 else "rated" if p == 2000.0 else "partial"
    print(f"{v:>4.1f} m/s: {p:>7.1f} kW {s}")
print(f"steady 7 m/s for a year: {pk(7.0) * 8760.0 / 1000.0:.0f} MWh")
