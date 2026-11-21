import math
PI = 3.141592653589793

def polar(outer, inner):
    return PI * (outer * outer * outer * outer - inner * inner * inner * inner) / 32.0

g = 80000.0
allowed = 40.0
for kw, rpm in [(5.5, 1450.0), (22.0, 960.0), (90.0, 300.0)]:
    torque = kw * 1000.0 / (2.0 * PI * rpm / 60.0) * 1000.0
    d = math.cbrt(16.0 * torque / (PI * allowed))
    j = polar(d, 0.0)
    twist = torque * 1000.0 / (g * j) * 180.0 / PI
    print(f"{kw} kW at {rpm:.0f} rpm: torque {torque / 1000.0:.1f} N m, solid shaft {d:.1f} mm, twist {twist:.2f} deg per metre")
torque = 500000.0
solid = math.cbrt(16.0 * torque / (PI * allowed))
outer = solid * 1.1
inner = 0.0
while polar(outer, inner + 0.1) / (outer / 2.0) >= polar(solid, 0.0) / (solid / 2.0):
    inner += 0.1
saving = 1.0 - (outer * outer - inner * inner) / (solid * solid)
print(f"500 N m: solid {solid:.1f} mm or hollow {outer:.1f} / {inner:.1f} mm, which uses {saving * 100.0:.0f}% less steel")
