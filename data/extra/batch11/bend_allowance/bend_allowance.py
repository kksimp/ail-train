PI = 3.141592653589793
def k_factor(radius, thick):
    return 0.33 if radius < thick else 0.42
def allowance(angle_deg, radius, thick):
    return angle_deg * PI / 180.0 * (radius + k_factor(radius, thick) * thick)
jobs = [("shelf bracket", [40.0, 60.0], 90.0, 2.0, 1.5), ("drip edge", [25.0, 15.0], 135.0, 1.0, 0.7), ("box lid", [20.0, 300.0, 20.0], 90.0, 0.5, 1.2), ("vent louvre", [30.0, 30.0], 45.0, 3.0, 2.0)]
for name, legs, angle, radius, thick in jobs:
    bends = len(legs) - 1
    ba = allowance(angle, radius, thick)
    straight = 0.0
    for x in legs:
        straight = straight + x
    flat = straight + ba * float(bends)
    print(f"{name:<13} {bends} x {angle} deg, R {radius} T {thick}: BA {ba:.3f} mm, blank {flat:.2f} mm")
