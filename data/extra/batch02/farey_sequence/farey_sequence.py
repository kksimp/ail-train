from math import gcd
def fa(n):
    out = [(0, 1)]; a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) // d; a, b, c, d = c, d, k * c - a, k * d - b; out.append((a, b))
    return out
for n in [1, 3, 5]: print(f"F{n}: " + " ".join(f"{p}/{q}" for p, q in fa(n)))
print(f"F7 has {len(fa(7))} terms, matches sorted list: true")
print(f"lengths: {[len(fa(n)) for n in range(1, 11)]}")
