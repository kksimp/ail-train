import math
def depth(rp, rs):
    r = rp / rs
    return r * r
sun = 696000.0
for name, rp in [("Earth", 6371.0), ("Neptune", 24622.0), ("Jupiter", 69911.0)]:
    ppm = depth(rp, sun) * 1000000.0
    print(f"{name:<8} across the Sun: dip {ppm:>8.0f} ppm")
pi = 3.141592653589793
for name, dip, days, rstar in [("KOI-A", 0.0084, 3.52, 1.2), ("KOI-B", 0.00062, 45.0, 0.9), ("KOI-C", 0.00011, 290.0, 1.0)]:
    rs = rstar * sun
    rp = math.sqrt(dip) * rs
    years = days / 365.25
    a_au = math.cbrt(years * years)
    hours = days * 24.0 * rs / (pi * a_au * 149597870.7)
    print(f"{name}: dip {dip * 100.0:.3f}% -> radius {rp / 6371.0:.2f} Earths, orbit {a_au:.3f} AU, transit {hours:.1f} h")
