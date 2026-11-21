speeds = [30.0, 50.0, 80.0, 110.0]
roads = [("Dry", 0.8), ("Wet", 0.5), ("Snow", 0.2), ("Ice", 0.1)]
def stopping(kmh, g):
    v = kmh / 3.6
    return v * 1.5 + v * v / (2.0 * g * 9.81)
heads = "  ".join(f"{int(s):>3} km/h" for s in speeds)
print(f"road   {heads}")
for name, g in roads:
    cells = " ".join(f"{stopping(s, g):>8.1f}" for s in speeds)
    print(f"{name:<5} {cells}")
gap = stopping(50.0, 0.5) - stopping(50.0, 0.8)
print(f"at 50 km/h a wet road adds {gap:.1f} m")
