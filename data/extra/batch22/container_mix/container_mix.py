def ceil_div(a, b):
    return (a + b - 1) // b

def plan(volume):
    best = [-1, 0, 0, 0]
    for big in range(ceil_div(volume, 67) + 1):
        rest = max(volume - big * 67, 0)
        small = ceil_div(rest, 33)
        opts = [[big * 2600 + small * 1800, big, small, 0]]
        if rest > 0:
            full = rest // 33
            loose = rest - full * 33
            opts.append([big * 2600 + full * 1800 + loose * 70, big, full, loose])
        for o in opts:
            if best[0] < 0 or o[0] < best[0]:
                best = o
    return best

for v in [12, 30, 45, 70, 95, 140, 210]:
    p = plan(v)
    loose = f", {p[3]} m3 shared" if p[3] > 0 else ""
    print(f"{v:>3} m3: {p[1]} x 40ft, {p[2]} x 20ft{loose}, cost {p[0]}")
