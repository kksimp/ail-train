import math
def roche(p, factor): return factor * p[1] * math.cbrt(p[2] / p[4])
pairs = [("Earth", 6371.0, 5.51, "Moon", 3.34, 384400.0), ("Mars", 3390.0, 3.93, "Phobos", 1.88, 9376.0), ("Saturn", 58232.0, 0.687, "ice ring", 0.92, 120000.0), ("Jupiter", 69911.0, 1.33, "Io", 3.53, 421700.0)]
for p in pairs:
    fluid = roche(p, 2.44)
    rigid = roche(p, 1.26)
    state = "inside even the rigid limit" if p[5] < rigid else "between the limits" if p[5] < fluid else "safe"
    print(f"{p[3]:<8} at {p[5]:>8.0f} km of {p[0]}: limits {rigid:>7.0f} / {fluid:>7.0f} km, {state}")
    print(f"         orbit is {p[5] / fluid:.2f} times the fluid limit")
