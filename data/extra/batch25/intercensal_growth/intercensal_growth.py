import math

counts = [(1901, 412300), (1911, 468900), (1921, 455200), (1931, 512800), (1951, 640400)]

def rate(a, b):
    ratio = b[1] / a[1]
    return math.pow(ratio, 1.0 / float(b[0] - a[0])) - 1.0

for i in range(len(counts) - 1):
    a, b = counts[i], counts[i + 1]
    r = rate(a, b)
    pct = r * 100.0
    note = f"doubles in {math.log(2.0) / math.log(1.0 + r):.0f} years" if r > 0.0 else "shrinking"
    print(f"{a[0]}-{b[0]}: {pct:>6.3f}% a year, {note}")
for y in [1906, 1916, 1941]:
    i = 0
    while counts[i + 1][0] < y:
        i += 1
    a = counts[i]
    base = 1.0 + rate(a, counts[i + 1])
    est = float(a[1]) * math.pow(base, float(y - a[0]))
    print(f"estimate for {y}: {int(math.floor(est / 100.0 + 0.5)) * 100}")
