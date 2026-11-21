N = 10000; spf = [0] * (N + 1)
for i in range(2, N + 1):
    if spf[i] == 0:
        for m in range(i, N + 1, i):
            if spf[m] == 0: spf[m] = i
def fac(x):
    o = []
    while x > 1: o.append(spf[x]); x //= spf[x]
    return o
for x in [12, 97, 360, 1001, 9999, 8192]: print(f"{x} = {' x '.join(map(str, fac(x)))}")
b = 0; h = []
for x in range(2, N + 1):
    k = len(set(fac(x)))
    if k > b: b = k; h = [x]
    elif k == b: h.append(x)
print(f"most distinct primes below 10000: {b}, e.g. {h[:5]}")
