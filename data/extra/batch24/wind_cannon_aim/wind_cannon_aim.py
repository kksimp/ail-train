import math
def flight(share):
    speed = 30.0
    vx = speed * share
    vy = speed * math.sqrt(1.0 - share * share)
    x = 0.0; y = 0.0; t = 0.0; dt = 0.01
    while y >= 0.0:
        ax = -0.1 * (vx + 4.0)
        ay = -9.8 - 0.1 * vy
        vx += ax * dt; vy += ay * dt
        x += vx * dt; y += vy * dt
        t += dt
    return [x, t]
lo = 0.70; hi = 0.99
for share in [0.3, 0.5, 0.7, 0.9, 0.99]:
    r = flight(share)
    print(f"share {share:.2f}: lands at {r[0]:.2f} m after {r[1]:.2f} s")
for k in range(30):
    mid = (lo + hi) / 2.0
    if flight(mid)[0] > 50.0: lo = mid
    else: hi = mid
r = flight(lo)
print(f"aim with share {lo:.4f} of the speed forward: lands at {r[0]:.2f} m")
