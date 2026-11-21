laid = 15.0
members = [("steel rail", 18.0, 0.000012), ("bridge deck", 120.0, 0.00001), ("alu window", 2.4, 0.000023), ("copper pipe", 30.0, 0.000017)]
def change_mm(m, dt):
    return m[2] * m[1] * dt * 1000.0
for m in members:
    grow = change_mm(m, 45.0 - laid)
    shrink = change_mm(m, laid - (0.0 - 20.0))
    swing = grow + shrink
    print(f"{m[0]:<12} {m[1]:>6.1f} m: +{grow:.2f} mm hot, -{shrink:.2f} mm cold, swing {swing:.2f} mm")
w = max(members, key=lambda m: int(m[1] * m[2] * 1000000.0))
print(f"largest movement: {w[0]}")
