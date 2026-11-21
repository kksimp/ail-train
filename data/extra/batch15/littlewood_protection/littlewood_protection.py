import math
def tail_probs(mean, top):
    pmf = math.exp(-mean); cdf = 0.0; tails = []
    for k in range(top + 1):
        cdf += pmf
        tails.append(1.0 - cdf)
        pmf = pmf * mean / float(k + 1)
    return tails
def protect(tails, ratio):
    y = 0
    while y < len(tails) and tails[y] >= ratio: y += 1
    return y
capacity = 150; full = 420.0
tails = tail_probs(60.0, capacity)
print(f"P(full-fare demand > 50) {tails[50]:.3f}, > 60 {tails[60]:.3f}, > 70 {tails[70]:.3f}")
for discount in [100.0, 160.0, 230.0, 300.0]:
    ratio = discount / full
    y = protect(tails, ratio)
    print(f"discount {discount:.0f}: ratio {ratio:.3f}, protect {y} seats, sell at most {capacity - y} cheap")
