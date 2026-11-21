def lag(xs, ys, x):
    tot = 0.0
    for i in range(len(xs)):
        t = ys[i]
        for j in range(len(xs)):
            if j != i: t = t * (x - xs[j]) / (xs[i] - xs[j])
        tot += t
    return tot
xs = [0.0, 1.0, 2.0, 3.0]; ys = [1.0, 3.0, 11.0, 31.0]
for x in [0.5, 1.5, 2.5, 4.0]: print(f"x {x}: fit {lag(xs, ys, x):.3f}, cubic {x * x * x + x + 1.0:.3f}")
hs = [6.0, 9.0, 12.0, 15.0, 18.0]; ts = [11.0, 16.0, 21.0, 22.0, 17.0]
for h in [7.5, 10.5, 13.5, 16.5]: print(f"{h:.1f} h: about {lag(hs, ts, h):.1f} C")
