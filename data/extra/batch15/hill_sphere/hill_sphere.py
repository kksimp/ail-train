import math
def hill(o): return o[1] * math.cbrt(o[2] / 3.0)
bodies = [("Earth", 149598000.0, 0.000003003, 384400.0), ("Mars", 227939000.0, 0.0000003227, 23460.0), ("Jupiter", 778570000.0, 0.0009545, 24500000.0), ("Neptune", 4498400000.0, 0.00005149, 49300000.0)]
for b in bodies:
    r = hill(b)
    share = b[3] / r
    verdict = "well inside" if share < 0.5 else "outer half" if share < 1.0 else "outside"
    print(f"{b[0]:<8} Hill radius {r / 1000000.0:>6.3f} million km, farthest moon at {share:.3f} of it ({verdict})")
moon = ("Moon", 384400.0, 0.0123, 0.0)
print(f"a moon of the Moon would need to stay within {hill(moon) / 2.0:.0f} km")
