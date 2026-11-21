riders = [("Mia", 28.0, -2.0), ("Leo", 35.0, 1.5), ("Ana", 22.0, -1.0)]
def moment(rs):
    t = 0.0
    for r in rs:
        t = t + r[1] * r[2]
    return t
for r in riders:
    side = "left" if r[2] < 0.0 else "right"
    print(f"{r[0]} {r[1]} kg at {abs(r[2])} m {side}: {r[1] * r[2]:>6.1f} kg m")
net = moment(riders)
dips = "left" if net < 0.0 else ("right" if net > 0.0 else "neither")
print(f"net moment {net:.1f} kg m, {dips} side dips")
spot = 0.0 - net / 30.0
if abs(spot) <= 2.5:
    print(f"Sam (30 kg) balances it at {spot:.2f} m")
    riders.append(("Sam", 30.0, spot))
else:
    print("Sam cannot reach the balance point")
after = moment(riders)
print(f"after: {abs(after):.3f} kg m with {len(riders)} riders")
