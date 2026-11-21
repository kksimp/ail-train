def br(d): return 4 if d >= -55 else 3 if d >= -67 else 2 if d >= -75 else 1 if d >= -85 else 0
S = [("home", "ap1", -48), ("home", "ap2", -63), ("cafe", "ap1", -71), ("cafe", "ap2", -82), ("guest", "ap1", -88), ("home", "ap3", -59)]
for n, a, d in S: print(f"{n}/{a}: {d} dBm = {10.0 ** (d / 10.0) * 1000000000.0:.1f} pW [{'|' * br(d):<4}]")
for n in sorted({s[0] for s in S}): b = max([s for s in S if s[0] == n], key=lambda s: s[2]); print(f"{n}: best {b[1]} at {b[2]} dBm")
