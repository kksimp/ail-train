import math

def nearest(x, y, w, h):
    best = (0, 0, 1000000.0)
    for px in [w // 3, w * 2 // 3]:
        for py in [h // 3, h * 2 // 3]:
            dx = float(x - px)
            dy = float(y - py)
            d = math.sqrt(dx * dx + dy * dy)
            if d < best[2]:
                best = (px, py, d)
    return best

def crop_top(y, h, crop):
    best = 0
    gap = h
    for line in [crop // 3, crop * 2 // 3]:
        top = min(max(y - line, 0), h - crop)
        miss = abs(y - top - line)
        if miss < gap:
            gap = miss
            best = top
    return best

w, h = 4000, 3000
diag = 5000.0
spots = [("lighthouse", 1300, 1050), ("boat", 2000, 1500), ("gull", 2700, 900), ("rock", 3500, 2400), ("child", 600, 2200)]
for name, x, y in spots:
    px, py, d = nearest(x, y, w, h)
    share = d / diag * 100.0
    tag = "on a third" if share <= 5.0 else "off the thirds"
    top = crop_top(y, h, 2250)
    print(f"{name:<10} nearest ({px},{py}) at {share:>4.1f}% {tag:<14} 16:9 crop top {top}")
