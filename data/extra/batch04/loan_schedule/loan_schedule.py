import math
def rd(x): return int(math.floor(abs(x) + 0.5)) * (1 if x >= 0 else -1)
b = 1200000; r = 0.005; n = 12
p = rd(b * r / (1 - (1 + r) ** -n)); print(f"payment: {p // 100}.{p % 100:02}"); ti = 0
for m in range(1, n + 1):
    it = rd(b * r); pr = p - it
    if m == n: pr = b
    b -= pr; ti += it
    print(f"{m:>2}: interest {it:>6} principal {pr:>7} balance {b:>8}")
print(f"total interest: {ti // 100}.{ti % 100:02}")
