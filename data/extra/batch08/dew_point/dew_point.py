import math
def dp(t, rh):
    g = math.log(rh / 100.0) + 17.62 * t / (243.12 + t); return 243.12 * g / (17.62 - g)
def feel(d): return "dry" if d < 10.0 else "comfortable" if d < 16.0 else "humid" if d < 21.0 else "oppressive"
for t, rh in [(30.0, 40.0), (25.0, 80.0), (18.0, 55.0), (33.0, 65.0), (12.0, 95.0), (5.0, 50.0)]:
    d = dp(t, rh); print(f"{t:>4.1f} C at {rh:.0f}%: dew point {d:>5.1f} C, gap {t - d:.1f}, {feel(d)}")
