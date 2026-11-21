def money(c):
    return f"{c // 100}.{c % 100:02d}"

def run(principal, payment, extra):
    bal = principal
    months = 0
    interest = 0
    while bal > 0:
        i = bal * 5 // 1000
        interest += i
        bal += i
        bal -= min(payment + extra, bal)
        months += 1
    return months, interest

base = run(20000000, 119910, 0)
for extra in [0, 10000, 20000, 50000]:
    m, it = run(20000000, 119910, extra)
    saved = base[1] - it
    print(f"extra {money(extra):>6}: {m} months ({m // 12} y {m % 12} m), interest {money(it):>9}, saved {money(saved)}")
