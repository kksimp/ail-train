def grow(s, m, r, n):
    b = s
    for _ in range(n): b += b * r // 120000; b += m
    return b
mo = lambda c: f"{c // 100:,}.{c % 100:02d}"
for r in [200, 450, 700]:
    b = grow(100000, 15000, r, 120); p = 100000 + 15000 * 120
    print(f"{r // 100}.{r % 100:02d}%: {mo(b)} (interest {mo(b - p)})")
m = 0; b = 100000
while b < 1000000: b += b * 450 // 120000; b += 15000; m += 1
print(f"10,000.00 reached at 4.50% after {m // 12} years {m % 12} months")
