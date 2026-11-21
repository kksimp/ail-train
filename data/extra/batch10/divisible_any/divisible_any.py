from math import gcd

def by_subsets(n, ds):
    total = 0
    for mask in range(1, 1 << len(ds)):
        l = 1
        bits = 0
        for i in range(len(ds)):
            if ((mask >> i) & 1) == 1:
                l = l // gcd(l, ds[i]) * ds[i]
                bits += 1
        if bits % 2 == 1:
            total += n // l
        else:
            total -= n // l
    return total

def direct(n, ds):
    return sum(1 for x in range(1, n + 1) if any(x % d == 0 for d in ds))

for n in [100, 1000]:
    for ds in [[3, 5], [3, 5, 7], [2, 3, 5, 7], [4, 6, 10], [6, 10, 15]]:
        a = by_subsets(n, ds)
        print(f"N = {n:>4}, divisors {ds}: {a} by inclusion-exclusion, {direct(n, ds)} counted, {n - a} left")
