def power(b, k):
    x = 1.0
    for _ in range(k):
        x *= b
    return x

def pv(pay, rate, n, due):
    shift = 0 if due else 1
    total = 0.0
    for t in range(n):
        total += pay / power(1.0 + rate, t + shift)
    return total

def fv(pay, rate, n, due):
    shift = 1 if due else 0
    total = 0.0
    for t in range(n):
        total += pay * power(1.0 + rate, n - 1 - t + shift)
    return total

print("five yearly payments of 1000")
for p in [3, 5, 8]:
    r = float(p) / 100.0
    a = pv(1000.0, r, 5, False)
    b = pv(1000.0, r, 5, True)
    c = fv(1000.0, r, 5, False)
    d = fv(1000.0, r, 5, True)
    ratio = b / a
    print(f"{p}%: PV ordinary {a:.2f}, due {b:.2f} (x{ratio:.4f}); FV ordinary {c:.2f}, due {d:.2f}")
