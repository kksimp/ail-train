import math

def delta(x, y):
    dl = x[1] - y[1]
    da = x[2] - y[2]
    db = x[3] - y[3]
    return math.sqrt(dl * dl + da * da + db * db)

def verdict(d):
    if d < 1.0:
        return "invisible"
    if d < 2.3:
        return "just noticeable"
    if d < 10.0:
        return "visible side by side"
    return "different colour"

chips = [("sage", 62.0, -12.0, 18.0), ("moss", 48.0, -15.0, 30.0), ("clay", 55.0, 22.0, 28.0), ("slate", 45.0, -2.0, -9.0), ("linen", 90.0, 1.0, 9.0), ("rust", 42.0, 30.0, 38.0)]
samples = [("wall A", 61.2, -11.5, 18.6), ("wall B", 52.0, -14.0, 26.0), ("door", 47.5, 25.5, 34.0), ("trim", 88.4, 0.6, 10.2), ("shutter", 30.0, 5.0, -25.0)]
for s in samples:
    best = chips[0]
    for c in chips:
        if delta(s, c) < delta(s, best):
            best = c
    d = delta(s, best)
    print(f"{s[0]:<8} closest {best[0]:<6} dE {d:>5.2f}  {verdict(d)}")
