import math
lever = 8.0
push = 150.0
for name, big, small in [("trolley jack", 50.0, 12.0), ("bottle jack", 40.0, 10.0), ("workshop press", 100.0, 16.0)]:
    r = big / small
    ratio = r * r
    lift_n = push * lever * ratio
    tonnes = lift_n / 9.81 / 1000.0
    rise = 25.0 / ratio
    strokes = int(math.ceil(150.0 / rise))
    print(f"{name:<14} ratio {ratio:>5.1f}: lifts {tonnes:.2f} t, {rise:.2f} mm per stroke, {strokes} strokes for 150 mm")
pressure = push * lever / (3.141592653589793 * 6.0 * 6.0)
print(f"trolley jack oil pressure: {pressure:.2f} N/mm2 = {pressure * 10.0:.1f} bar")
