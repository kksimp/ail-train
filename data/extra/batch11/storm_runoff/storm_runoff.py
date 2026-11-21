parts = [("roofs", 1.2, 0.9), ("roads", 0.8, 0.85), ("lawns", 2.5, 0.2), ("woodland", 1.5, 0.1)]
def weighted_c(ps):
    area = 0.0
    for p in ps:
        area = area + p[1]
    t = 0.0
    for p in ps:
        t = t + p[1] * p[2]
    return t / area
area = 0.0
for p in parts:
    area = area + p[1]
c = weighted_c(parts)
print(f"catchment {area:.1f} ha, weighted C {c:.3f}")
pipe = 0.5
for intensity in [10.0, 25.0, 50.0, 100.0]:
    q = c * intensity * area / 360.0
    note = "over the pipe" if q > pipe else "fits the pipe"
    print(f"{intensity:>5.1f} mm/h storm: peak {q:.3f} m3/s, {note}")
q2 = weighted_c([("car park", 6.0, 0.9)]) * 50.0 * 6.0 / 360.0
print(f"if it were all car park, a 50 mm/h storm gives {q2:.3f} m3/s")
