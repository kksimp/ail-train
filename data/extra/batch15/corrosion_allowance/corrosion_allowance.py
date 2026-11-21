def rate(c): return 87.6 * c[2] / (c[3] * c[4] * c[5])
def rating(mm):
    if mm < 0.02: return "outstanding"
    if mm < 0.1: return "good"
    if mm < 0.5: return "fair"
    return "poor"
coupons = [("carbon steel", "cooling tower", 412.0, 7.86, 30.0, 720.0), ("carbon steel", "sea spray", 1890.0, 7.86, 30.0, 720.0), ("stainless 316", "sea spray", 6.5, 8.0, 30.0, 720.0), ("copper", "cooling tower", 41.0, 8.96, 30.0, 720.0), ("zinc", "sea spray", 160.0, 7.14, 30.0, 720.0)]
for c in coupons:
    r = rate(c)
    life = 3.0 / r
    print(f"{c[0]:<13} {c[1]:<13} {r:.4f} mm/yr {rating(r):<11} 3 mm lasts {life:>7.1f} years")
poor = [c[1] for c in coupons if rate(c) >= 0.5]
print("sites with poor results: " + ", ".join(poor))
