def naive(xs):
    s = 0.0
    sq = 0.0
    for x in xs:
        s += x
        sq += x * x
    n = float(len(xs))
    return (sq - s * s / n) / (n - 1.0)

def two_pass(xs):
    s = 0.0
    for x in xs:
        s += x
    m = s / float(len(xs))
    d = 0.0
    for x in xs:
        d += (x - m) * (x - m)
    return d / float(len(xs) - 1)

for shift in [0.0, 1000.0, 1000000.0, 1000000000.0]:
    xs = [shift + 4.0, shift + 7.0, shift + 13.0, shift + 16.0]
    n, mean, m2 = 0, 0.0, 0.0
    for x in xs:
        n += 1
        delta = x - mean
        mean += delta / float(n)
        m2 += delta * (x - mean)
    var = m2 / float(n - 1)
    print(f"shift {shift:>14.1f}: naive {naive(xs):>10.4f}, two-pass {two_pass(xs):.4f}, Welford {var:.4f}")
