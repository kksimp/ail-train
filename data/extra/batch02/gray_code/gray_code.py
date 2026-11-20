g = lambda n: n ^ (n >> 1)
def fg(x):
    n, s = x, x >> 1
    while s:
        n ^= s; s >>= 1
    return n
for n in range(8):
    print(f"{n} {n:03b} -> {g(n):03b} -> {fg(g(n))}")
print(f"single-bit steps: {sum(1 for n in range(255) if bin(g(n) ^ g(n + 1)).count('1') == 1)} of 255")
print(f"wraps: {str(bin(g(0) ^ g(255)).count('1') == 1).lower()}")
