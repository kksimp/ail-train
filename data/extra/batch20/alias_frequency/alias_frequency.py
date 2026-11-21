def alias(f, fs):
    r = f % fs
    return min(r, fs - r)

fs = 1000
for f in [100, 400, 600, 900, 1100, 1900, 2350]:
    a = alias(f, fs)
    note = "passes as is" if a == f else f"folds to {a} Hz"
    print(f"{f:>4} Hz sampled at {fs} Hz: {note}")
fps = 24
spokes = 12
for rpm in [60, 100, 115, 125, 240]:
    spoke_hz100 = rpm * spokes * 100 // 60
    r = spoke_hz100 % (fps * 100)
    seen = r if r <= fps * 50 else r - fps * 100
    d = "forwards" if seen > 0 else ("backwards" if seen < 0 else "frozen in place")
    print(f"wheel at {rpm:>3} rpm: spokes pass at {spoke_hz100 // 100}.{spoke_hz100 % 100:02} Hz, film shows {d}")
