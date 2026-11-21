def ds(n):
    if n == 1: return 0
    s = 1; d = 2
    while d * d <= n:
        if n % d == 0:
            s += d
            if d * d != n: s += n // d
        d += 1
    return s
def kd(n): s = ds(n); return "perfect" if s == n else "abundant" if s > n else "deficient"
for n in [6, 12, 28, 35, 496, 945, 8128]: print(f"{n}: divisors sum to {ds(n)}, {kd(n)}")
C = {}
for n in range(1, 101): C[kd(n)] = C.get(kd(n), 0) + 1
print(f"1..100: {C['deficient']} deficient, {C['perfect']} perfect, {C['abundant']} abundant")
