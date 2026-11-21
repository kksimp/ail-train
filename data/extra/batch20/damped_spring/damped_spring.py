import math
PI = 3.141592653589793

def classify(z):
    if z < 0.999:
        return "Under"
    elif z > 1.001:
        return "Over"
    return "Critical"

m = 1.0
k = 100.0
w0 = math.sqrt(k / m)
print(f"natural frequency {w0} rad/s")
for c in [2.0, 6.0, 10.0, 20.0, 40.0]:
    zeta = c / (2.0 * math.sqrt(k * m))
    kind = classify(zeta)
    print(f"c = {c}: zeta {zeta:.2f}, Damping.{kind}")
    if kind == "Under":
        wd = w0 * math.sqrt(1.0 - zeta * zeta)
        q = 1.0 / (2.0 * zeta)
        per = math.exp(-zeta * w0 * 2.0 * PI / wd)
        cycles = math.log(0.05) / math.log(per)
        print(f"  rings at {wd / (2.0 * PI):.3f} Hz, Q {q:.1f}, each swing keeps {per * 100.0:.1f}%, under 5% after {cycles:.1f} cycles")
    elif kind == "Critical":
        print("  returns fastest without overshoot")
    else:
        print("  creeps back slowly without overshoot")
