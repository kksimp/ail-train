def years_lasting(start, pct, returns):
    bal = start
    w = start * pct // 100
    year = 0
    while year < 40 and bal >= w:
        r = returns[year % len(returns)]
        bal = (bal - w) * (100 + r) // 100
        w = w * 103 // 100
        year += 1
    return year

returns = [7, -12, 15, 4, -3, 9, 11, -8, 6, 2, 13, -5]
for pct in [4, 5, 6, 7]:
    n = years_lasting(500000, pct, returns)
    note = "40 years or more" if n == 40 else f"{n} years"
    print(f"withdraw {pct}% ({500000 * pct // 100} in year 1): lasts {note}")
bad = [-12, -3, -8, -5, 7, 15, 4, 9, 11, 6, 2, 13]
n = years_lasting(500000, 5, bad)
print(f"5% with the bad years first: lasts {n} years")
