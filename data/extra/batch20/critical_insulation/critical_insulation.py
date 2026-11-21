import math
PI = 3.141592653589793

def loss(r1, r2, k, h, dt):
    return 2.0 * PI * dt / (math.log(r2 / r1) / k + 1.0 / (h * r2))

k = 0.17
h = 10.0
rc = k / h
print(f"PVC lagging, calm air: critical radius {rc * 1000.0:.0f} mm")
wire = 0.001
best = 0.0
best_r = 0.0
for mm in [1.0, 3.0, 6.0, 10.0, 17.0, 25.0, 40.0, 60.0]:
    r2 = mm / 1000.0
    q = loss(wire, r2, k, h, 40.0)
    if q > best:
        best = q
        best_r = mm
    print(f"wire lagged to {mm:>4.0f} mm: {q:.2f} W/m")
print(f"most heat escapes at {best_r:.0f} mm of radius")
pipe = 0.05
bare = loss(pipe, pipe, k, h, 100.0)
lagged = loss(pipe, 0.08, k, h, 100.0)
print(f"a 50 mm pipe is past the critical radius: {bare:.0f} W/m bare, {lagged:.0f} W/m lagged")
