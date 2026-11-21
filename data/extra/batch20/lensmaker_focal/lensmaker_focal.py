def curv(r):
    return 0.0 if r == 0.0 else 1.0 / r

def focal(r1, r2, n):
    return 1.0 / ((n - 1.0) * (curv(r1) - curv(r2)))

lenses = [("biconvex", 100.0, -100.0), ("plano-convex", 60.0, 0.0), ("meniscus", 40.0, 100.0), ("biconcave", -80.0, 80.0)]
red = 1.514
blue = 1.522
for name, r1, r2 in lenses:
    fr = focal(r1, r2, red)
    fb = focal(r1, r2, blue)
    kind = "converging" if fr > 0.0 else "diverging"
    diopters = 1000.0 / fr
    spread = abs(fr - fb)
    print(f"{name:<13} f red {fr:>8.2f} mm, blue {fb:>8.2f} mm, {diopters:>6.2f} D, {kind}, colours {spread:.2f} mm apart")
