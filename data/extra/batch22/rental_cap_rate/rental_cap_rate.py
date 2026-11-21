props = [("flat", 250000, 1400, 5, 4200, 62500, 9800), ("terrace", 320000, 1780, 4, 6100, 80000, 12300), ("shop unit", 410000, 2600, 12, 9800, 123000, 15100)]

def noi(p):
    return p[2] * 12 * (100 - p[3]) // 100 - p[4]

def pct(a, b):
    return float(a) * 100.0 / float(b)

for p in props:
    n = noi(p)
    cap = pct(n, p[1])
    cash = pct(n - p[6], p[5])
    cover = float(n) / float(p[6])
    print(f"{p[0]:<9} income {n:>6}: cap rate {cap:.2f}%, cash on cash {cash:.2f}%, cover {cover:.2f}")
best = props[0]
for p in props:
    if noi(p) * 1000 // p[1] > noi(best) * 1000 // best[1]:
        best = p
print(f"best cap rate: {best[0]}")
