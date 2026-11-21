def ip(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True
def co(s):
    t = s * s; return [t - 3 * (s - 1), t - 2 * (s - 1), t - (s - 1), t]
print(f"ring corners for sides 3, 5, 7: {co(3)} {co(5)} {co(7)}")
for size in [5, 101, 1001]:
    print(f"diagonal sum for {size}x{size}: {1 + sum(sum(co(s)) for s in range(3, size + 1, 2))}")
p, c, s = 0, 1, 3
while True:
    p += sum(1 for x in co(s) if ip(x)); c += 4
    if p * 100 < c * 15: break
    s += 2
print(f"primes on the diagonals first fall below 15% at side {s} ({p} of {c})")
