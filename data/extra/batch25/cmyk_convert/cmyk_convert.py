import math

def pct(x):
    return int(math.floor(x * 100.0 + 0.5))

def to_cmyk(r, g, b):
    top = max(r, g, b)
    if top == 0:
        return (0.0, 0.0, 0.0, 1.0)
    k = 1.0 - top / 255.0
    rf = r / 255.0
    gf = g / 255.0
    bf = b / 255.0
    return ((1.0 - rf - k) / (1.0 - k), (1.0 - gf - k) / (1.0 - k), (1.0 - bf - k) / (1.0 - k), k)

def back(x):
    c, m, y, k = x
    return [int(math.floor(255.0 * (1.0 - v) * (1.0 - k) + 0.5)) for v in [c, m, y]]

colours = [("tomato", 255, 99, 71), ("navy", 0, 0, 128), ("olive", 128, 128, 0), ("teal", 0, 128, 128), ("black", 0, 0, 0), ("plum", 142, 69, 133), ("mustard", 225, 173, 1), ("slate", 47, 79, 79)]
for name, r, g, b in colours:
    x = to_cmyk(r, g, b)
    ink = pct(x[0]) + pct(x[1]) + pct(x[2]) + pct(x[3])
    flag = " too heavy for newsprint" if ink > 240 else ""
    shown = "[" + ", ".join(str(v) for v in back(x)) + "]"
    print(f"{name:<8} C{pct(x[0]):>3} M{pct(x[1]):>3} Y{pct(x[2]):>3} K{pct(x[3]):>3}  ink {ink}%  back {shown}{flag}")
