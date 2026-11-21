def stop_point(speed):
    x = 0.0; v = speed; dt = 0.01
    while abs(v) > 0.005:
        decel = -0.5 if v > 0.0 else 0.5
        v += decel * dt
        x += v * dt
        if x > 20.0:
            x = 40.0 - x; v = -0.6 * v
    return x
good = []
for k in range(10):
    speed = 4.0 + 0.5 * float(k)
    at = stop_point(speed)
    mark = "  <- in the zone" if 12.0 <= at <= 14.0 else ""
    print(f"launch {speed:.1f} m/s: stops at {at:.2f} m{mark}")
    if mark != "": good.append(speed)
print(f"{len(good)} launch speeds land in the zone")
