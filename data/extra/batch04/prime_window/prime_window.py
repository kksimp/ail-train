def sp(l):
    ip = [True] * (l + 1); out = []
    for i in range(2, l + 1):
        if ip[i]:
            out.append(i)
            for m in range(i * i, l + 1, i): ip[m] = False
    return out
def wp(lo, hi):
    r = 1
    while (r + 1) ** 2 <= hi: r += 1
    ok = [True] * (hi - lo + 1)
    for p in sp(r):
        m = max((lo + p - 1) // p * p, p * p)
        while m <= hi: ok[m - lo] = False; m += p
    return [lo + i for i in range(len(ok)) if ok[i] and lo + i > 1]
ps = wp(1000000000, 1000000200)
print(f"{len(ps)} primes between 1,000,000,000 and 1,000,000,200")
print(f"first {ps[:4]}")
print(f"widest gap {max(ps[i] - ps[i - 1] for i in range(1, len(ps)))}")
print(f"small check: {wp(1, 30)}")
