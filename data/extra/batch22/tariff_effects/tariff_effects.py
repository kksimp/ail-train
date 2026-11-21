def demand(p):
    return max(200 - 2 * p, 0)

def supply(p):
    return max(2 * p - 20, 0)

world = 40
d0 = demand(world)
s0 = supply(world)
print(f"free trade: demand {d0}, home supply {s0}, imports {d0 - s0}")
for t in [3, 6, 9, 12, 15]:
    p = world + t
    d = demand(p)
    s = supply(p)
    imports = max(d - s, 0)
    revenue = t * imports
    consumers = t * (d0 + d) // 2
    producers = t * (s0 + s) // 2
    lost = consumers - producers - revenue
    print(f"tariff {t:>2}: price {p}, imports {imports:>3}, revenue {revenue:>3}, consumers lose {consumers:>4}, producers gain {producers:>4}, deadweight {lost}")
