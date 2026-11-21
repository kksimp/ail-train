def grow(start, lags, count):
    xs = list(start)
    while len(xs) < count:
        n = len(xs)
        xs.append(sum(xs[n - l] for l in lags))
    return xs

def report(name, xs, a, b, c):
    n = len(xs)
    ratio = float(xs[n - 1]) / float(xs[n - 2])
    residual = ratio * ratio * ratio - (a * ratio * ratio + b * ratio + c)
    print(f"{name}: {xs[:15]}")
    print(f"    ratio after {n} terms {ratio:.9f}, cubic residual {str(abs(residual) < 0.000001).lower()}")

trib = grow([0, 0, 1], [1, 2, 3], 40)
pad = grow([1, 1, 1], [2, 3], 80)
perrin = grow([3, 0, 2], [2, 3], 80)
report("Tribonacci", trib, 1.0, 1.0, 1.0)
report("Padovan", pad, 0.0, 1.0, 1.0)
report("Perrin", perrin, 0.0, 1.0, 1.0)
print("Padovan and Perrin share the plastic ratio, about 1.324718")
