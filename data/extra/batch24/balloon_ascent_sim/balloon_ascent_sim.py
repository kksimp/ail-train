def accel(h, v):
    air = 1.2 - 0.0001 * h
    lift = 9.8 * (air * 3.0 - 3.0) / 0.9
    return lift - 0.004 * v * abs(v)
h = 0.0; v = 0.0; top = 0.0
for t in range(1, 901):
    v += accel(h, v)
    h += v
    if h > top: top = h
    if t % 100 == 0:
        print(f"t {t:>3} s: height {h:>7.1f} m, speed {v:>5.2f} m/s")
print(f"highest {top:.1f} m; neutral height is {(1.2 - 1.0) / 0.0001:.1f} m")
