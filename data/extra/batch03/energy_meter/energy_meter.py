rd = [(1, 40210), (8, 40295), (15, 40388), (19, 40371), (22, 40440), (30, 40552)]
g = []
for d, v in rd:
    if g and v < g[-1][1]: print(f"day {d}: reading {v} is below {g[-1][1]}, ignored"); continue
    g.append((d, v))
for i in range(1, len(g)):
    (d0, v0), (d1, v1) = g[i - 1], g[i]; u = v1 - v0
    print(f"days {d0}-{d1}: {u} kWh, {u // (d1 - d0)} a day")
t = g[-1][1] - g[0][1]; c = t * 28
print(f"total {t} kWh, about {c // 100}.{c % 100:02d}")
