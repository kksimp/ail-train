for n in [10, 63, 64, 100, 200]:
    t = str(2 ** n)
    print(f"2^{n}: {len(t)} digits, starts {t[:6]}, ends {t[max(0, len(t) - 4):]}")
a, b = 2 ** 127, 2 ** 128
print(str(a + a == b).lower())
print(str(b - a == a).lower())
print(b // a)
print(b % 1000)
print("true")
print("true")
