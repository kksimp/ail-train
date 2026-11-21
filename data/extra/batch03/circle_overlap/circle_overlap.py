def rel(a, b):
    d2 = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2; s = a[2] + b[2]; df = abs(a[2] - b[2])
    if d2 > s * s: return "separate"
    if d2 == s * s: return "touching outside"
    if d2 == 0 and df == 0: return "same circle"
    if d2 < df * df: return "one inside the other"
    if d2 == df * df: return "touching inside"
    return "overlapping"
for a, b in [((0, 0, 2), (5, 0, 2)), ((0, 0, 2), (3, 4, 3)), ((0, 0, 5), (1, 1, 1)), ((0, 0, 5), (3, 0, 2)), ((1, 1, 3), (2, 2, 3)), ((4, 4, 1), (4, 4, 1))]:
    print(f"({a[0]},{a[1]}) r{a[2]} and ({b[0]},{b[1]}) r{b[2]}: {rel(a, b)}")
