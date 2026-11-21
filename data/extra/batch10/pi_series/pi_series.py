def leibniz(n):
    s = 0.0
    sign = 1.0
    for k in range(n):
        s += sign / float(2 * k + 1)
        sign = -sign
    return 4.0 * s

def nilakantha(n):
    s = 3.0
    sign = 1.0
    for k in range(1, n + 1):
        a = float(2 * k)
        s += sign * 4.0 / (a * (a + 1.0) * (a + 2.0))
        sign = -sign
    return s

def wallis(n):
    p = 1.0
    for k in range(1, n + 1):
        t = float(2 * k)
        p *= t * t / ((t - 1.0) * (t + 1.0))
    return 2.0 * p

pi = 3.141592653589793
print("terms        Leibniz     Nilakantha         Wallis")
for n in [1, 10, 100, 1000, 10000]:
    l = leibniz(n)
    k = nilakantha(n)
    w = wallis(n)
    print(f"{n:>5}  {l:>13.10f}  {k:>13.10f}  {w:>13.10f}")
print(f"pi     {pi:>13.10f}")
print(f"Leibniz error after 10000 terms {abs(leibniz(10000) - pi):.10f}, about 1/10000")
