import math

def scale(f, w, h, bw, bh):
    sx = bw / w
    sy = bh / h
    if f in ("Fill", "Keep"):
        return 1.0
    if f == "Contain":
        return min(sx, sy)
    if f == "Cover":
        return max(sx, sy)
    return min(min(sx, sy), 1.0)

def layout(f, w, h, bw, bh):
    if f == "Fill":
        return f"{bw}x{bh}"
    s = scale(f, w, h, bw, bh)
    dw = int(math.floor(w * s + 0.5))
    dh = int(math.floor(h * s + 0.5))
    if dw > bw or dh > bh:
        cw = max(dw - bw, 0)
        ch = max(dh - bh, 0)
        return f"{dw}x{dh} crop {cw}x{ch}"
    return f"{dw}x{dh} pad {(bw - dw) // 2},{(bh - dh) // 2}"

bw, bh = 400, 300
images = [(1600, 900), (600, 800), (300, 200), (400, 300), (250, 600)]
modes = ["Fill", "Contain", "Cover", "Keep", "ScaleDown"]
for w, h in images:
    print(f"{w}x{h} into {bw}x{bh}:")
    parts = [f"{m} {layout(m, w, h, bw, bh)}" for m in modes]
    print("  " + " | ".join(parts))
