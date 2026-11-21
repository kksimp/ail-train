import math

def rate(half):
    return math.log(2.0) / half

def daughter(n0, la, lb, t):
    return n0 * la / (lb - la) * (math.exp(-la * t) - math.exp(-lb * t))

la = rate(66.0)
lb = rate(6.01)
n0 = 1000000.0
for t in [0.0, 6.0, 12.0, 23.0, 48.0, 96.0, 168.0]:
    parent = n0 * math.exp(-la * t)
    d = daughter(n0, la, lb, t)
    act_ratio = lb * d / (la * parent)
    print(f"t {t:>5.0f} h: Mo-99 {parent:>8.0f}, Tc-99m {d:>7.0f}, activity ratio {act_ratio:.3f}")
peak = math.log(lb / la) / (lb - la)
print(f"Tc-99m peaks after {peak:.1f} h; the generator is milked about daily")
b = 0.0
a = n0
dt = 0.01
for _ in range(2300):
    da = -la * a * dt
    b += (la * a - lb * b) * dt
    a += da
print(f"small-step check at 23 h: {b:.0f} against {daughter(n0, la, lb, 23.0):.0f}")
