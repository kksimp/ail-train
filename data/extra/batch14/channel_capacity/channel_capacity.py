import math
def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    q = 1.0 - p
    return -(p * math.log(p) + q * math.log(q)) / math.log(2.0)
def z_rate(x, flip):
    return h2(x * (1.0 - flip)) - x * h2(flip)
for p in [0.0, 0.01, 0.05, 0.11, 0.25, 0.5]:
    print(f"symmetric, flip {p:.2f}: capacity {1.0 - h2(p):.4f} bits")
for e in [0.1, 0.3]:
    print(f"erasure, lost {e:.1f}: capacity {1.0 - e:.4f} bits")
flip = 0.3
best_x, best = 0.0, 0.0
for i in range(1001):
    x = i / 1000.0
    r = z_rate(x, flip)
    if r > best:
        best, best_x = r, x
print(f"Z channel, a sent 1 reads as 0 with chance 0.3: capacity {best:.4f} bits with 1s sent {best_x * 100.0:.1f}% of the time")
