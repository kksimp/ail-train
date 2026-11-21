clays = [("stoneware", 88.0), ("porcelain", 86.0), ("earthenware", 93.0)]
pieces = [("mug height", 100.0), ("bowl width", 150.0), ("plate width", 260.0)]
for name, fired in clays:
    s = (100.0 - fired) / 100.0
    print(f"{name} shrinks {s * 100.0:.1f}%")
    for what, mm in pieces:
        t = mm / (1.0 - s)
        print(f"  {what:<11} {mm:.0f} mm fired: throw {t:.1f} mm (+{t - mm:.1f})")
