def deposit(t, r, n):
    return t * r / ((1.0 + r) ** float(n) - 1.0)

target = 50000.0
for p in [2, 4, 6, 8]:
    rate = float(p) / 100.0
    d = deposit(target, rate, 10)
    plain = target / 10.0
    saved = plain - d
    print(f"{p}% a year: deposit {d:.2f} a year for 10 years ({saved:.2f} less than {plain:.2f})")
d = deposit(target, 0.04, 10)
bal = 0.0
for y in range(1, 11):
    interest = bal * 0.04
    bal = bal + interest + d
    if y % 3 == 1:
        print(f"year {y:>2}: interest {interest:>8.2f}, balance {bal:>9.2f}")
print(f"final balance {bal:.2f}")
