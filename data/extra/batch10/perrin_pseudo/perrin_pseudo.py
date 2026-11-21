def perrin_mod(n):
    a, b, c = 3 % n, 0, 2 % n
    for _ in range(n):
        a, b, c = b, c, (a + b) % n
    return a

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

terms = [3, 0, 2]
while len(terms) < 20:
    k = len(terms)
    terms.append(terms[k - 2] + terms[k - 3])
print(f"P(0..19) = {terms}")
hits = []
mismatches = 0
for n in range(2, 401):
    divides = perrin_mod(n) == 0
    if divides:
        hits.append(n)
    if divides != is_prime(n):
        mismatches += 1
print(f"n <= 400 dividing P(n): {len(hits)}, first {hits[:12]}")
print(f"disagreements with trial division: {mismatches}")
for n in [9, 25, 91, 341, 561]:
    print(f"P({n}) mod {n} = {perrin_mod(n)}")
