stations = [("Harbour", 75.4, 98.9), ("Ridge", 62.0, 75.6), ("Valley", 91.3, 126.1)]
def distance_km(lag):
    vp = 6.0
    vs = 3.5
    return lag * vp * vs / (vp - vs)
def clock(seconds):
    whole = int(seconds)
    tenths = int((seconds - float(whole)) * 10.0)
    m = whole // 60
    s = whole % 60
    return f"12:{m:02}:{s:02}.{tenths}"
origins = []
for name, p, s in stations:
    lag = s - p
    d = distance_km(lag)
    origin = p - d / 6.0
    origins.append(origin)
    print(f"{name:<8} S-P lag {lag:>4.1f} s: {d:>6.1f} km away, quake at {clock(origin)}")
mean = sum(origins) / float(len(origins))
nearest = min(stations, key=lambda st: int((st[2] - st[1]) * 10.0))
print(f"average origin time {clock(mean)}, nearest station {nearest[0]}")
