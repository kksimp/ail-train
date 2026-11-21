def jacobi(a0, n0):
    a = a0 % n0
    n = n0
    t = 1
    while a != 0:
        while a % 2 == 0:
            a = a // 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        tmp = a
        a = n
        n = tmp
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a = a % n
    return t if n == 1 else 0

def pow_mod(a, e, n):
    x = 1
    base = a % n
    k = e
    while k > 0:
        if (k & 1) == 1:
            x = x * base % n
        base = base * base % n
        k = k >> 1
    return x

def passes(a, n):
    j = jacobi(a, n)
    return j != 0 and pow_mod(a, (n - 1) // 2, n) == (j + n) % n

syms = [jacobi(q, 15) for q in range(1, 15)]
print(f"(a/15) for a = 1..14: {syms}")
for n in [91, 561, 1105, 1729, 15841]:
    fermat = 0
    euler = 0
    for w in range(1, n):
        if pow_mod(w, n - 1, n) == 1:
            fermat += 1
        if passes(w, n):
            euler += 1
    print(f"{n:>5}: Fermat liars {fermat:>5}, Euler liars {euler:>4} of {n - 1}")
state = 7
for n in [7919, 1729, 104729, 999999937, 999999929]:
    verdict = "probably prime"
    for _ in range(10):
        state = (state * 1103515245 + 12345) % 2147483648
        pick = 2 + (state >> 8) % (n - 3)
        if not passes(pick, n):
            verdict = "composite"
    print(f"{n}: {verdict}")
