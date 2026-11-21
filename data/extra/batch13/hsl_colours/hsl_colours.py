import math

def channel(v):
    return int(math.floor(v * 255.0 + 0.5))

def to_rgb(h, s, l):
    c = (1.0 - abs(2.0 * l - 1.0)) * s
    sector = h // 60
    frac = float(h) / 60.0 - float(sector)
    pos = float(sector % 2) + frac
    x = c * (1.0 - abs(pos - 1.0))
    m = l - c / 2.0
    rgb = [[c, x, 0.0], [x, c, 0.0], [0.0, c, x], [0.0, x, c], [x, 0.0, c]][sector] if sector < 5 else [c, 0.0, x]
    return [channel(v + m) for v in rgb]

swatches = [("tomato", 9, 1.0, 0.64), ("olive", 60, 1.0, 0.25), ("teal", 180, 1.0, 0.25), ("slate", 210, 0.13, 0.5), ("orchid", 302, 0.59, 0.65), ("gold", 51, 1.0, 0.5), ("white", 0, 0.0, 1.0)]
for name, h, s, l in swatches:
    rgb = to_rgb(h, s, l)
    print(f"{name:<7} hsl({h}, {s}, {l}) -> #{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x} {rgb}")
