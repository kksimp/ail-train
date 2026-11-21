def al(i): return 12570 if i <= 100000 else max(0, 12570 - (i - 100000) // 2)
def tx(i):
    l = max(0, i - al(i)); d = 0
    for w, r in [(37700, 20), (87440, 40), (1000000000, 45)]:
        p = min(l, w); d += p * r // 100; l -= p
    return d
for i in [10000, 30000, 50270, 80000, 110000, 150000]: t = tx(i); print(f"{i:>7,}: allowance {al(i):>6,}, tax {t:>6,} ({t * 100 / i:.1f}%)")
