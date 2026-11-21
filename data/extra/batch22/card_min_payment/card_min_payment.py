def money(c):
    return f"{c // 100}.{c % 100:02d}"

def min_due(bal):
    return max(bal * 3 // 100, 2500)

def payoff(start, fixed):
    bal = start
    months = 0
    interest = 0
    while bal > 0 and months < 600:
        i = bal * 2 // 100
        interest += i
        bal += i
        due = fixed if fixed > 0 else min_due(bal)
        bal -= min(due, bal)
        months += 1
    return months, interest

bal = 300000
for m in range(1, 4):
    i = bal * 2 // 100
    bal += i
    due = min_due(bal)
    bal -= due
    print(f"month {m}: interest {money(i)}, minimum {money(due)}, left {money(bal)}")
for fixed in [0, 15000, 30000]:
    months, interest = payoff(300000, fixed)
    label = "minimum only" if fixed == 0 else f"fixed {money(fixed)}"
    total = 300000 + interest
    print(f"{label:<13}: {months:>3} months, interest {money(interest):>8}, paid {money(total)}")
