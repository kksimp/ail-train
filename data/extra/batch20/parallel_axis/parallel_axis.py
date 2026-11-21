import math
PI = 3.141592653589793

def moment(parts, axis):
    total = 0.0
    for m, i, pos in parts:
        d = pos - axis
        total += i + m * d * d
    return total

bar = (2.0, 2.0 * 0.6 * 0.6 / 12.0, 0.0)
left = (5.0, 0.4 * 5.0 * 0.01, -0.3)
right = (5.0, 0.4 * 5.0 * 0.01, 0.3)
bell = [bar, left, right]
for axis in [0.0, 0.15, 0.3]:
    print(f"dumbbell about x = {axis}: I = {moment(bell, axis):.4f} kg m2")
rod = (1.0, 1.0 / 12.0, 0.5)
bob = (2.0, 0.4 * 2.0 * 0.0025, 1.0)
pend = [rod, bob]
i_pivot = moment(pend, 0.0)
total_m = 0.0
for p in pend:
    total_m = total_m + p[0]
acc = 0.0
for p in pend:
    acc = acc + p[0] * p[2]
d_cm = acc / total_m
t = 2.0 * PI * math.sqrt(i_pivot / (total_m * 9.81 * d_cm))
simple = 2.0 * PI * math.sqrt(1.0 / 9.81)
print(f"pendulum: I {i_pivot:.4f} kg m2, centre of mass {d_cm:.4f} m below the pivot")
print(f"period {t:.4f} s, a simple 1 m pendulum {simple:.4f} s")
