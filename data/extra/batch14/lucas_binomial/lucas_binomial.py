from math import comb
def lucas(n, k, p):
    result = 1
    while n > 0 or k > 0:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        result = result * comb(ni, ki) % p
        n //= p
        k //= p
    return result
def pascal(n, k, p):
    row = [1]
    for r in range(1, n + 1):
        row = [1] + [(row[i - 1] + row[i]) % p for i in range(1, r)] + [1]
    return row[k]
for n, k, p in [[1000, 300, 13], [1000, 500, 7], [2026, 1000, 11], [100, 50, 3]]:
    print(f"C({n}, {k}) mod {p}: Lucas {lucas(n, k, p)}, Pascal {pascal(n, k, p)}")
for n in [10, 63, 64, 100]:
    odd = len([k for k in range(n + 1) if lucas(n, k, 2) == 1])
    ones = bin(n).count("1")
    print(f"row {n}: {odd} odd entries, 2^{ones} = {1 << ones}")
