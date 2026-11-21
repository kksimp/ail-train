kit = [("phone", 15000, 1800), ("phone", 15000, 300), ("laptop 3-cell", 55500, 9000), ("earbuds", 400, 130)]
ch = [35, 35, 60, 25]
hs = []
for i, (n, c, d) in enumerate(kit):
    h = float(c * ch[i] // 100) / float(d); hs.append(h)
    st = "charge now" if h < 1.0 else ("charge soon" if h < 4.0 else "fine")
    print(f"{n:<14} {ch[i]:>3}% {h:>5.1f} h  {st}")
