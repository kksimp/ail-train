import math
def ch(h, i): return int(h[1 + 2 * i:3 + 2 * i], 16)
def hx(r, g, b): return f"#{r:02x}{g:02x}{b:02x}"
for a, b in [("#ff0000", "#0000ff"), ("#ffffff", "#000000"), ("#33aa77", "#cc5511"), ("#123456", "#654321")]:
    r, g, bl = [(ch(a, i) + ch(b, i)) // 2 for i in range(3)]
    gr = int(math.floor(0.299 * r + 0.587 * g + 0.114 * bl + 0.5)); print(f"{a} + {b} = {hx(r, g, bl)}, grey {hx(gr, gr, gr)}")
