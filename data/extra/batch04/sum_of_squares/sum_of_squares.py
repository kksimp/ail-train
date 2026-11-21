def ways(n):
    o = []; a = 0
    while 2 * a * a <= n:
        r = n - a * a; b = a
        while b * b < r: b += 1
        if b * b == r: o.append((a, b))
        a += 1
    return o
for n in [5, 25, 50, 65, 21, 325]:
    w = [f"{a}^2+{b}^2" for a, b in ways(n)]; print(f"{n}: {', '.join(w) if w else 'none'}")
n = 1
while len(ways(n)) < 3: n += 1
print(f"smallest with three ways: {n}")
print(f"{sum(1 for k in range(1, 101) if ways(k))} of 1..100 are sums of two squares")
