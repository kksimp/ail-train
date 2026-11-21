import math

def eff(inertia, radius):
    return inertia / (radius * radius)

def accel(m1, m2, p):
    return 9.81 * (m1 - m2) / (m1 + m2 + eff(*p))

light = (0.0, 0.1)
heavy = (0.02, 0.1)
print(f"heavy pulley acts like {eff(*heavy):.2f} kg more mass")
for m1, m2 in [(2.0, 1.0), (5.0, 4.0), (10.0, 9.5), (3.0, 3.0)]:
    a0 = accel(m1, m2, light)
    a1 = accel(m1, m2, heavy)
    t1 = m1 * (9.81 - a1)
    t2 = m2 * (9.81 + a1)
    print(f"{m1} kg vs {m2} kg: a = {a0:.3f} light, {a1:.3f} heavy, tensions {t1:.2f} and {t2:.2f} N")
a = accel(2.0, 1.0, heavy)
t = math.sqrt(2.0 / a)
print(f"2 kg vs 1 kg on the heavy pulley drops 1 m in {t:.3f} s")
