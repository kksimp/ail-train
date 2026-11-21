def ba(d, t): f = d * 20 // t; return "[" + "=" * f + " " * (20 - f) + "]"
for s, d in [(0, 0), (2, 3100), (5, 9800), (9, 17900), (14, 30500), (18, 41200), (21, 48000)]:
    p = d * 100 // 48000; e = "unknown" if d == 0 else "done" if d == 48000 else f"{(48000 - d) * s // d} s left"
    print(f"{ba(d, 48000)} {p:>3}% {e}")
