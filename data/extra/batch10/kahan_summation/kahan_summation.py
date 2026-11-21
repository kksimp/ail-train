for n in [10, 1000, 100000, 10000000]:
    naive = 0.0
    total, carry = 0.0, 0.0
    for _ in range(n):
        naive += 0.1
        y = 0.1 - carry
        t = total + y
        carry = (t - total) - y
        total = t
    target = float(n) / 10.0
    print(f"{n:>8} tenths: naive {naive:.10f} (off {abs(naive - target):.10f}), Kahan {total:.10f} (off {abs(total - target):.10f})")
big = 1.0
total, carry = 1.0, 0.0
for _ in range(1000):
    big += 0.0000000000000001
    y = 0.0000000000000001 - carry
    t = total + y
    carry = (t - total) - y
    total = t
print(f"1 + a thousand 1e-16: naive {big:.16f}, Kahan {total:.16f}")
