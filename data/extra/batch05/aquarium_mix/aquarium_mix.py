F = [("neon tetra", 6, 3, 21, 26), ("guppy", 4, 4, 22, 28), ("corydoras", 5, 6, 22, 26), ("danio", 6, 5, 18, 24)]; cm = 0; lo = -100; hi = 100
for n, c, s, a, b in F: cm += c * s; lo = max(lo, a); hi = min(hi, b); print(f"{c} x {n} ({s} cm, {a}-{b} C)")
print(f"stock {cm} cm of fish for 60 cm capacity: {'ok' if cm <= 60 else 'overstocked'}")
print(f"shared temperature {lo}-{hi} C" if lo <= hi else f"no shared temperature ({lo} > {hi})")
