import math
def speed(k, vf, kj):
    return vf * (1.0 - k / kj)
vf = 100.0
kj = 120.0
for k in [0, 20, 40, 60, 80, 100, 120]:
    kf = float(k)
    v = speed(kf, vf, kj)
    q = kf * v
    state = "free" if kf < kj / 2.0 else ("capacity" if kf == kj / 2.0 else "congested")
    print(f"{k:>3} veh/km: {v:>5.1f} km/h, {q:>6.1f} veh/h ({state})")
capacity = vf * kj / 4.0
print(f"lane capacity {capacity} veh/h at {kj / 2.0} veh/km")
target = 2000.0
disc = math.sqrt(kj * kj / 4.0 - target * kj / vf)
k1 = kj / 2.0 - disc
k2 = kj / 2.0 + disc
print(f"{target} veh/h happens at {k1:.1f} veh/km ({speed(k1, vf, kj):.1f} km/h) and {k2:.1f} veh/km ({speed(k2, vf, kj):.1f} km/h)")
