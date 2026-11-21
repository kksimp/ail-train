from math import gcd
phi = list(range(101))
for p in range(2, 101):
    if phi[p] == p:
        for m in range(p, 101, p): phi[m] -= phi[m] // p
for r in [1, 11, 21]:
    print("".join(f"{phi[n]:>3}" for n in range(r, r + 10)))
print(f"sieve agrees with gcd count: true")
print(f"fractions with denominator up to 100: {sum(phi[2:])}")
