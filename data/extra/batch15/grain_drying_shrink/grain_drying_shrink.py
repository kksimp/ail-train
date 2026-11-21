def water_removed(t, m1, m2):
    if m1 <= m2: return 0.0
    return t * (m1 - m2) / (100.0 - m2)
target = 14.0; per_point = 1.85
loads = [("A1", 28.4, 19.5), ("A2", 31.0, 22.0), ("B1", 26.7, 16.2), ("B2", 29.9, 13.1), ("C1", 30.5, 24.8)]
sold = 0.0; charge = 0.0
for lid, t, m in loads:
    w = water_removed(t, m, target)
    dry = t - w
    points = m - target if m > target else 0.0
    fee = points * per_point * t
    sold += dry; charge += fee
    shrink = w / t * 100.0
    print(f"{lid}: {t:.1f} t at {m:.1f}% -> {dry:.2f} t ({shrink:.2f}% shrink), drying {fee:.2f}")
print(f"delivered {sold:.2f} t, drying charges {charge:.2f}")
