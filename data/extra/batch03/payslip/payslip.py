def tax(t):
    if t <= 0: return 0
    if t <= 375000: return t * 20 // 100
    return 375000 * 20 // 100 + (t - 375000) * 40 // 100
mo = lambda c: f"{c // 100:,}.{c % 100:02d}"
for y in [1500000, 3000000, 6000000, 9000000]:
    g = y // 12; p = g * 5 // 100; t = tax(g - p - 104750); n = g - p - t
    print(f"salary {mo(y)}: gross {mo(g)}, pension {mo(p)}, tax {mo(t)}, net {mo(n)}")
