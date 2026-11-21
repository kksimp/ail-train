import math
def per(s): return 20.0 if s == "Point" else 10.0
def level_at(s, l1, r1, r2):
    ratio = r2 / r1
    return l1 - per(s) * math.log10(ratio)
def limit_distance(s, l1, r1, limit):
    return r1 * math.pow(10.0, (l1 - limit) / per(s))
for kind, name, l1 in [("Point", "generator", 85.0), ("Line", "motorway", 78.0)]:
    print(f"{name} (Source.{kind}): {l1:.1f} dB at 10 m")
    for r in [20.0, 40.0, 80.0, 160.0]:
        l = level_at(kind, l1, 10.0, r)
        print(f"  at {r:>5.0f} m: {l:.1f} dB")
    d = limit_distance(kind, l1, 10.0, 55.0)
    print(f"  under 55 dB beyond {d:.0f} m")
