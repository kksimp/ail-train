def bars(v, w):
    tot = sum(v.values()); most = max(v.values())
    names = sorted(v, key=lambda k: (-v[k], k))
    pad = max(len(n) for n in names)
    out = []
    for n in names:
        s = 0 if most == 0 else v[n] * w // most
        p = 0 if tot == 0 else v[n] * 100 // tot
        out.append(f"{n.ljust(pad)} {'#' * s}{' ' * (w - s)} {v[n]:>3} ({p}%)")
    return out
for l in bars({"oak": 41, "birch": 17, "maple": 41, "ash": 6, "elm": 0}, 30):
    print(l.rstrip())
print(bars({"x": 0}, 10)[0].rstrip())
