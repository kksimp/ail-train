def payoff(start, fixed):
    balance = start
    months = 0
    interest = 0
    while balance > 0 and months < 600:
        charge = balance * 22 // 1200
        balance += charge
        interest += charge
        minimum = max(balance * 25 // 1000, 2500)
        pay = fixed if fixed > 0 else minimum
        balance -= min(pay, balance)
        months += 1
    return [months, interest]
start = 300000
for name, fixed in [("minimum only", 0), ("100 a month", 10000), ("150 a month", 15000), ("300 a month", 30000)]:
    res = payoff(start, fixed)
    years = res[0] // 12
    extra = res[0] % 12
    cents = res[1] % 100
    print(f"{name:<13} {res[0]:>3} months ({years} y {extra} m), interest {res[1] // 100}.{cents:02}")
