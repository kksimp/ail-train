import math
PI = 3.141592653589793
soils = [("loose sand", 28.0, 17.0), ("dense gravel", 38.0, 20.0), ("stiff clay", 22.0, 19.0)]
def ka(phi):
    s = math.sin(phi * PI / 180.0)
    return (1.0 - s) / (1.0 + s)
for name, phi, gamma in soils:
    print(f"{name}: Ka {ka(phi):.3f}")
    for h in [1.0, 2.0, 3.0]:
        thrust = 0.5 * ka(phi) * gamma * h * h
        moment = thrust * h / 3.0
        print(f"  {h} m wall: thrust {thrust:>6.2f} kN/m, overturning {moment:>6.2f} kNm/m")
