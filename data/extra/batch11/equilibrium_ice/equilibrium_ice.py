import math
def shift(a, b, kc):
    qa = 4.0 - kc
    qb = kc * (a + b)
    qc = 0.0 - kc * a * b
    disc = math.sqrt(qb * qb - 4.0 * qa * qc)
    r1 = (0.0 - qb + disc) / (2.0 * qa)
    r2 = (0.0 - qb - disc) / (2.0 * qa)
    limit = a if a < b else b
    return r1 if r1 >= 0.0 and r1 <= limit else r2
kc = 50.0
for a, b in [(1.0, 1.0), (1.0, 2.0), (0.5, 0.2), (2.0, 0.1)]:
    x = shift(a, b, kc)
    h2 = a - x
    i2 = b - x
    hi = 2.0 * x
    check = hi * hi / (h2 * i2)
    print(f"start H2 {a} I2 {b}: H2 {h2:.4f}, I2 {i2:.4f}, HI {hi:.4f} M (Kc check {check:.1f})")
