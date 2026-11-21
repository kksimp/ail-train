import math

def binom(n, k):
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r

def pmf(n, k, p):
    return float(binom(n, k)) * math.pow(p, float(k)) * math.pow(1.0 - p, float(n - k))

n = 10
p = 0.7
mean = 0.0
at_least_8 = 0.0
total = 0.0
for k in range(n + 1):
    q = pmf(n, k, p)
    total += q
    mean += float(k) * q
    if k >= 8:
        at_least_8 += q
    bar = "#" * int(round(q * 100.0))
    sep = "" if bar == "" else " "
    print(f"{k:>2} made: {q:.4f}{sep}{bar}")
print(f"total {total:.6f}, mean {mean:.4f} (np = {float(n) * p:.4f}), at least 8: {at_least_8:.4f}")
