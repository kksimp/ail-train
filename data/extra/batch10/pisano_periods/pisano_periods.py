def pisano(m):
    a, b, k = 0, 1, 0
    while True:
        a, b = b, (a + b) % m
        k += 1
        if a == 0 and b == 1:
            break
    return k

row = [f"{m}:{pisano(m)}" for m in range(2, 13)]
print(f"periods {', '.join(row)}")
print(f"last digit repeats every {pisano(10)}, last two digits every {pisano(100)}")
for p in [11, 19, 29, 31, 7, 13, 17]:
    per = pisano(p)
    if p % 5 == 1 or p % 5 == 4:
        rule = "divides p - 1"
        holds = (p - 1) % per == 0
    else:
        rule = "divides 2(p + 1)"
        holds = (2 * (p + 1)) % per == 0
    print(f"p = {p:>2}: period {per:>2}, {rule}: {str(holds).lower()}")
