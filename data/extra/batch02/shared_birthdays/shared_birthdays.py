def ch(n):
    p = 1.0
    for i in range(n): p = p * float(365 - i) / 365.0
    return 1.0 - p
for n in [2, 10, 23, 30, 50, 70]:
    print(f"{n:>2} people: {ch(n) * 100.0:>6.2f}%")
n = 1
while ch(n) < 0.5: n += 1
print(f"first group over 50%: {n}")
k = 1
while ch(k) < 0.99: k += 1
print(f"first group over 99%: {k}")
