import math

drop = 2.0
for name, e in [("superball", 0.9), ("basketball", 0.8), ("tennis ball", 0.7), ("clay ball", 0.3)]:
    h = drop
    dist = drop
    air = math.sqrt(2.0 * drop / 9.81)
    n = 0
    while True:
        h = h * e * e
        if h < 0.01:
            break
        n += 1
        dist += 2.0 * h
        air += 2.0 * math.sqrt(2.0 * h / 9.81)
    limit = drop * (1.0 + e * e) / (1.0 - e * e)
    print(f"{name:<12} e {e}: {n:>2} bounces over 1 cm, path {dist:.2f} m (limit {limit:.2f} m), {air:.2f} s in the air")
