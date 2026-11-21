xs = [1, 2, 2, 2, 3, 5, 5, 8, 8, 8, 8, 13, 21]
def lb(v):
    lo, hi, p = 0, len(xs), 0
    while lo < hi:
        m = (lo + hi) // 2; p += 1
        if xs[m] < v: lo = m + 1
        else: hi = m
    return lo, p
def ub(v):
    lo, hi = 0, len(xs)
    while lo < hi:
        m = (lo + hi) // 2
        if xs[m] <= v: lo = m + 1
        else: hi = m
    return lo
for v in [2, 8, 4, 1, 21, 30]:
    f, p = lb(v); l = ub(v)
    print(f"{v:>2}: absent, would go at {f} ({p} probes)" if f == l else f"{v:>2}: at {f}..{l - 1}, {l - f} times ({p} probes)")
