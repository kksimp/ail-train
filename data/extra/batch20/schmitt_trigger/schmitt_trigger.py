def noise(seed):
    seed[0] = (seed[0] * 1103515245 + 12345) % 2147483648
    return seed[0] % 601 - 300

def signal(seed):
    out = []
    for t in range(160):
        phase = t % 80
        base = 1000 + phase * 75 if phase < 40 else 1000 + (80 - phase) * 75
        out.append(base + noise(seed))
    return out

def plain(xs):
    high = False
    flips = 0
    for x in xs:
        now = x > 2500
        if now != high:
            flips += 1
            high = now
    return flips

def schmitt(xs):
    high = False
    flips = 0
    for x in xs:
        if not high and x > 2800:
            high = True
            flips += 1
        elif high and x < 2200:
            high = False
            flips += 1
    return flips

seed = [2024]
xs = signal(seed)
print(f"first samples (mV): {xs[0:8]}")
print(f"plain comparator switches {plain(xs)} times")
print(f"Schmitt trigger switches {schmitt(xs)} times")
print("the ramp itself crosses 2500 mV 4 times")
