class Flat:
    def __init__(s, price, max_g): s.price, s.max_g = price, max_g
    def name(s): return "flat"
    def quote(s, g): return -1 if g > s.max_g else s.price
class PerKilo:
    def __init__(s, base, per_kg): s.base, s.per_kg = base, per_kg
    def name(s): return "per-kilo"
    def quote(s, g): return s.base + s.per_kg * ((g + 999) // 1000)
class Banded:
    def __init__(s, limits, prices): s.limits, s.prices = limits, prices
    def name(s): return "banded"
    def quote(s, g):
        for i in range(len(s.limits)):
            if g <= s.limits[i]:
                return s.prices[i]
        return -1
def line(c, g):
    q = c.quote(g)
    if q < 0:
        return f"{c.name()} n/a"
    return f"{c.name()} {q // 100}.{q % 100:02}"
carriers = [Flat(890, 5000), PerKilo(300, 150), Banded([500, 2000, 10000], [320, 760, 1490])]
for g in [350, 1200, 4800, 9500, 12000]:
    parts = [line(c, g) for c in carriers]
    best = "none"; best_q = -1
    for c in carriers:
        q = c.quote(g)
        if q >= 0 and (best_q < 0 or q < best_q):
            best_q = q; best = c.name()
    print(f"{g:>5} g: {' | '.join(parts)} -> {best}")
