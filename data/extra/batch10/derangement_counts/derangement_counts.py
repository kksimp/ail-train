import math

def brute(n, pos, used):
    if pos == n:
        return 1
    total = 0
    for v in range(n):
        if v != pos and not used[v]:
            used[v] = True
            total += brute(n, pos + 1, used)
            used[v] = False
    return total

d = [1, 0]
fact = [1, 1]
for n in range(2, 16):
    d.append((n - 1) * (d[n - 1] + d[n - 2]))
    fact.append(fact[n - 1] * n)
for n in range(1, 8):
    used = [False] * n
    print(f"n = {n}: D = {d[n]:>4}, brute force {brute(n, 0, used):>4}, of {fact[n]:>4} orderings")
for n in [10, 15]:
    ratio = float(d[n]) / float(fact[n])
    print(f"D({n}) = {d[n]}, share {ratio:.9f}")
print(f"1/e = {1.0 / math.exp(1.0):.9f}")
