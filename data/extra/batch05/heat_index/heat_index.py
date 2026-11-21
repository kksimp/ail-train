import math
def dp(t, rh): a = 17.27; b = 237.7; g = a * t / (b + t) + math.log(rh / 100); return b * g / (a - g)
def cf(d): return "dry" if d < 10 else "pleasant" if d < 16 else "sticky" if d < 21 else "oppressive"
for d, t, rh in [("Mon", 24.0, 35.0), ("Tue", 27.0, 60.0), ("Wed", 31.0, 70.0), ("Thu", 22.0, 80.0), ("Fri", 33.0, 40.0)]:
    x = dp(t, rh); print(f"{d}: {t:.0f}C {rh:.0f}% dew point {x:.1f}C, {cf(x)}")
