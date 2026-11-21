tiers = [(6000, 150), (15000, 280), (1000000000, 520)]
def money(c): return f"${c // 100}.{c % 100:02d}"
for name, l in [("flat 2", 4200), ("house 7", 13900), ("farm", 41000), ("empty", 0)]:
    parts, start = [], 0
    for up, rate in tiers:
        if l <= start: break
        used = min(l, up) - start
        parts.append((used, used * rate // 1000)); start = up
    tot = 1250 + sum(p[1] for p in parts)
    t = " + ".join(f"{u}L={money(c)}" for u, c in parts)
    print(f"{name:<8} {t if t else 'no use'}, standing {money(1250)}, total {money(tot)}")
