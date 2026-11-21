import math
def et0(m):
    tmean = (m[2] + m[3]) / 2.0
    return 0.0023 * m[4] * (tmean + 17.8) * math.sqrt(m[2] - m[3])
season = [("Apr", 30, 19.0, 7.0, 13.6, 45.0, 0.4), ("May", 31, 24.0, 11.0, 15.6, 38.0, 0.7), ("Jun", 30, 28.0, 15.0, 16.5, 22.0, 1.15), ("Jul", 31, 31.0, 17.0, 16.1, 12.0, 1.15), ("Aug", 31, 30.0, 17.0, 14.5, 20.0, 0.8)]
total = 0.0
for m in season:
    e = et0(m)
    need = e * m[6] * float(m[1])
    irrigate = max(need - m[5], 0.0)
    total += irrigate
    print(f"{m[0]}: ET0 {e:.2f} mm/day, crop uses {need:>5.1f} mm, rain {m[5]:>4.0f} mm, irrigate {irrigate:>5.1f} mm")
cubic = total * 10.0
print(f"season irrigation {total:.0f} mm = {cubic:.0f} m3 per hectare")
