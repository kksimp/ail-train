def shape_factor(pitch):
    if pitch <= 30.0:
        return 0.8
    if pitch < 60.0:
        return 0.8 * (60.0 - pitch) / 30.0
    return 0.0
regions = [("lowland", 0.5), ("hills", 1.0), ("mountain", 2.5)]
for name, pitch, area in [("flat garage", 2.0, 18.0), ("house", 35.0, 80.0), ("chalet", 50.0, 120.0), ("spire", 65.0, 10.0)]:
    mu = shape_factor(pitch)
    parts = []
    for region, sk in regions:
        total = mu * sk * area
        parts.append(f"{region} {total:.1f}")
    line = ", ".join(parts)
    print(f"{name:<11} {pitch:>4.1f} deg, mu {mu:.3f}: {line} kN")
