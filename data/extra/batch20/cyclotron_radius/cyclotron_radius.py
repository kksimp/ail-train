import math
PI = 3.141592653589793
E = 0.0000000000000000001602
AMU = 0.000000000000000000000000001661
b = 1.5
ps = [("proton", 1.007 * AMU, E), ("deuteron", 2.014 * AMU, E), ("alpha", 4.002 * AMU, 2.0 * E), ("carbon-12 ion", 12.0 * AMU, 6.0 * E)]
for kev in [100.0, 1000.0]:
    print(f"{kev:.0f} keV in {b} T:")
    for name, mass, charge in ps:
        joules = kev * 1000.0 * E
        v = math.sqrt(2.0 * joules / mass)
        r = mass * v / (charge * b)
        mhz = charge * b / (2.0 * PI * mass) / 1000000.0
        print(f"  {name:<14} v {v / 1000000.0:>6.2f} Mm/s, radius {r * 100.0:>6.2f} cm, {mhz:.2f} MHz")
