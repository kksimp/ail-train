import math

def plain(start):
    x = start
    steps = 0
    while steps < 1000:
        nxt = math.cos(x)
        steps += 1
        if abs(nxt - x) < 0.0000000001:
            x = nxt
            break
        x = nxt
    return [x, float(steps)]

def steffensen(start):
    x = start
    steps = 0
    while steps < 100:
        a = math.cos(x)
        b = math.cos(a)
        den = b - 2.0 * a + x
        if den == 0.0:
            break
        nxt = x - (a - x) * (a - x) / den
        steps += 1
        if abs(nxt - x) < 0.000001:
            x = nxt
            break
        x = nxt
    return [x, float(steps)]

for start in [0.0, 1.0, 3.0]:
    p = plain(start)
    s = steffensen(start)
    print(f"start {start:.1f}: plain {p[0]:.10f} in {int(p[1])} steps, Steffensen {s[0]:.10f} in {int(s[1])} steps")
x = 1.0
row = []
for _ in range(8):
    x = math.cos(x)
    row.append(f"{x:.5f}")
print(f"first iterates from 1: {' '.join(row)}")
