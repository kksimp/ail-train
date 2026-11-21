import math
def components(heading, wind_dir, speed):
    pi = 3.141592653589793
    d = float(wind_dir - heading) * pi / 180.0
    v = float(speed)
    return [v * math.cos(d), v * math.sin(d)]
runways = [("09", 90), ("27", 270), ("14", 140), ("32", 320)]
winds = [(250, 18), (20, 12), (165, 25)]
for d, speed in winds:
    best = ""; best_head = -100.0
    for name, heading in runways:
        hc = components(heading, d, speed)
        side = "from the right" if hc[1] > 0.0 else "from the left"
        cross = abs(hc[1])
        ok = cross <= 15.0
        print(f"  runway {name}: head {hc[0]:>5.1f} kt, cross {cross:>4.1f} kt {side}")
        if ok and hc[0] > best_head:
            best_head = hc[0]; best = name
    print(f"wind {d:03} at {speed} kt: use runway {best}")
