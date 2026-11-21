import math
for e in [0.0, 5.0, 15.0, 30.0, 45.0, 60.0, 75.0]:
    if e <= 0.0: print(f"{e:>4.0f} deg: sun down"); continue
    t = math.tan(e * 3.141592653589793 / 180.0)
    print(f"{e:>4.0f} deg: " + ", ".join(f"{n} {h / t:.1f} m" for n, h in [("pole", 2.0), ("tree", 9.0), ("tower", 31.0)]))
