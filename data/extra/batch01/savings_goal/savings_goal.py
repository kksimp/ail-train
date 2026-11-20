def mtg(start, dep, bps, goal):
    b, m = start, 0
    while b < goal:
        if m >= 600: return None
        b += b * bps // 10000
        b += dep; m += 1
    return m
def eur(c): return f"{c // 100:,}.{c % 100:02d}"
for start, dep, bps, goal in [(0, 20000, 25, 500000), (100000, 5000, 40, 1000000), (0, 0, 50, 100), (250000, 0, 100, 500000)]:
    label = f"start {eur(start)}, +{eur(dep)}/m, {bps}bp"
    m = mtg(start, dep, bps, goal)
    if m is not None:
        print(f"{label}: {m} months ({m // 12}y {m % 12}m) to {eur(goal)}")
    else:
        print(f"{label}: never reaches {eur(goal)}")
