vessels = [("soda can", 0.6, 33.0, 0.1), ("propane bottle", 1.8, 150.0, 2.5), ("boiler drum", 4.0, 600.0, 40.0), ("hydraulic hose", 20.0, 6.0, 3.0)]
for name, mpa, r, w in vessels:
    h = mpa * r / w
    thin = r / w >= 10.0
    note = "thin-wall formula fits" if thin else "wall too thick for the formula"
    print(f"{name:<15} hoop {h:>6.1f} MPa, lengthwise {h / 2.0:>6.1f} MPa ({note})")
allowed = 140.0
joint = 0.85
for p in [1.0, 2.5, 6.0]:
    t = p * 600.0 / (allowed * joint)
    print(f"a 1.2 m drum at {p} MPa needs a {t:.1f} mm wall")
sphere = 4.0 * 600.0 / (2.0 * allowed * joint)
print(f"a sphere of the same radius at 4.0 MPa needs only {sphere:.1f} mm")
