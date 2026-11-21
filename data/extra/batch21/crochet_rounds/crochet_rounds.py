items = [("coaster", 100), ("potholder", 180), ("cushion", 400), ("rug", 900)]
for name, d in items:
    n = (d // 2 + 5) // 6
    st = 3 * n * (n + 1)
    cm = st * 25 // 10
    balls = (cm + 7999) // 8000
    print(f"{name:<9} {d} mm: {n} rounds, last round {6 * n} stitches, {st} in all, {cm // 100} m of yarn, {balls} balls")
print(f"rounds 1-5: [{', '.join(str(6 * k) for k in range(1, 6))}]")
