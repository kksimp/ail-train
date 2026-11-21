from math import comb
n = 10
total = float(1 << n)
target = [comb(n, k) / total for k in range(n + 1)]
p = [0.0] * (n + 1)
p[n] = 1.0
t = 0
for stop in [5, 10, 20, 40, 80]:
    while t < stop:
        q = [0.0] * (n + 1)
        for k in range(n + 1):
            q[k] += 0.5 * p[k]
            if k > 0:
                q[k - 1] += 0.5 * p[k] * float(k) / float(n)
            if k < n:
                q[k + 1] += 0.5 * p[k] * float(n - k) / float(n)
        p = q
        t += 1
    tv = sum(abs(p[k] - target[k]) for k in range(n + 1))
    print(f"after {t:>2} steps: P(5 in A) = {p[5]:.4f}, distance from binomial {tv / 2.0:.4f}")
print(f"binomial P(5 in A) = {target[5]:.4f}")
print(f"Kac: mean time to return to all-in-A is 1 / {1.0 / total} = {1 << n} steps (lazy chain: twice that)")
