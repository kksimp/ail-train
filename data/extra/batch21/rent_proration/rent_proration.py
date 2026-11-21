def month_days(y, m):
    if m == 2:
        leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        return 29 if leap else 28
    if m in (4, 6, 9, 11):
        return 30
    return 31

def prorate(rent, y, m, first, last):
    return rent * (last - first + 1) // month_days(y, m)

def money(c):
    return f"{c // 100}.{c % 100:02d}"

rent = 125000
stays = [(2024, 2, 10, 29, "Ana"), (2023, 2, 10, 28, "Ben"), (2025, 6, 1, 15, "Caro"), (2025, 7, 20, 31, "Dev"), (2025, 9, 16, 30, "Eli")]
total = 0
for y, m, a, b, who in stays:
    due = prorate(rent, y, m, a, b)
    total += due
    print(f"{who:<5} {y}-{m:02d} days {a:>2}-{b:>2} ({b - a + 1}/{month_days(y, m)}): {money(due)}")
print(f"total billed: {money(total)}")
print(f"a whole April costs {money(prorate(rent, 2025, 4, 1, 30))}")
