import math

def order(r1, r2, use_a):
    ratio = r2[0] / r1[0] if use_a else r2[1] / r1[1]
    return math.log(r2[2] / r1[2]) / math.log(ratio)

def power(x, n):
    p = 1.0
    for _ in range(n):
        p *= x
    return p

runs = [(0.1, 0.1, 0.0002), (0.2, 0.1, 0.0008), (0.1, 0.3, 0.0006), (0.3, 0.2, 0.0036)]
oa = order(runs[0], runs[1], True)
ob = order(runs[0], runs[2], False)
m = int(round(oa))
n = int(round(ob))
print(f"order in A: {oa:.3f} -> {m}")
print(f"order in B: {ob:.3f} -> {n}")
print(f"rate = k [A]^{m} [B]^{n}")
ks = []
for i, r in enumerate(runs):
    k = r[2] / (power(r[0], m) * power(r[1], n))
    ks.append(k)
    print(f"run {i + 1}: k = {k:.4f} L^2/(mol^2 s)")
acc = 0.0
for k in ks:
    acc = acc + k
mean = acc / float(len(ks))
print(f"mean k {mean:.4f}; overall order {m + n}")
