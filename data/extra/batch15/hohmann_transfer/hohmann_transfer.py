import math
def hohmann(mu, r1, r2):
    pi = 3.141592653589793
    sum_r = r1 + r2
    a = math.sqrt(mu / r1) * (math.sqrt(2.0 * r2 / sum_r) - 1.0)
    b = math.sqrt(mu / r2) * (1.0 - math.sqrt(2.0 * r1 / sum_r))
    t = pi * math.sqrt(sum_r * sum_r * sum_r / (8.0 * mu))
    return (abs(a), abs(b), t / 86400.0)
mu = 132712440018.0
au = 149597870.7
for name, dist in [("Venus", 0.723), ("Mars", 1.524), ("Jupiter", 5.203), ("Saturn", 9.537)]:
    d1, d2, days = hohmann(mu, au, dist * au)
    total = d1 + d2
    print(f"Earth to {name:<7}: burns {d1:.2f} + {d2:.2f} = {total:.2f} km/s, {days:>6.0f} days")
d1, d2, days = hohmann(398600.4418, 6678.0, 42164.0)
print(f"low orbit to geostationary: {d1:.3f} + {d2:.3f} km/s, {days * 24.0:.2f} hours")
