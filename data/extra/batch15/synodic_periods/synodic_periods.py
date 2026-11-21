def synodic(p1, p2): return 1.0 / abs(1.0 / p1 - 1.0 / p2)
earth = 365.256
planets = [("Mercury", 87.969), ("Venus", 224.701), ("Mars", 686.98), ("Jupiter", 4332.59), ("Saturn", 10759.22), ("Neptune", 60190.0)]
longest = ("", 0.0)
for name, period in planets:
    s = synodic(earth, period)
    years = s / earth
    print(f"{name:<8} orbit {period:>8.1f} d, lines up every {s:>6.1f} d ({years:.2f} yr)")
    if s > longest[1]:
        longest = (name, s)
print(f"longest wait: {longest[0]}")
month = synodic(27.32166, earth)
print(f"Moon: sidereal 27.32 d, new moon to new moon {month:.3f} d")
