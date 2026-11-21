import math

def point(deg):
    names = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    i = int(math.floor((deg + 11.25) / 22.5)) % 16
    return names[i]

def back(deg):
    return deg - 180.0 if deg >= 180.0 else deg + 180.0

legs = [("harbour to lighthouse", 7.0), ("lighthouse to bay", 58.0), ("bay to ridge", 100.5), ("ridge to tarn", 147.0), ("tarn to farm", 200.0), ("farm to mill", 260.0), ("mill to church", 301.0), ("church to harbour", 349.0)]
counts = {}
for name, deg in legs:
    p = point(deg)
    counts[p[0]] = counts.get(p[0], 0) + 1
    mils = deg * 6400.0 / 360.0
    b = back(deg)
    print(f"{name:<22} {deg:>5.1f} {p:<3} back {b:>5.1f} {point(b):<3} {mils:>6.0f} mils")
summary = ", ".join(f"{k} {v}" for k, v in counts.items())
print(f"first letters: {summary}")
