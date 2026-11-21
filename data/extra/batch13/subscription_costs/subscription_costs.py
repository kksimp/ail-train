subs = [("music", 1099, "Monthly", 1), ("video", 1549, "Monthly", 75), ("cloud", 9999, "Yearly", 3), ("newspaper", 350, "Weekly", 40), ("gym", 3500, "Monthly", 92), ("game pass", 5999, "Yearly", 200)]

def monthly(cents, period):
    if period == "Weekly":
        return cents * 52 // 12
    if period == "Monthly":
        return cents
    return cents // 12

def money(c):
    return f"{c // 100}.{c % 100:02}"

total = 0
saving = 0
for name, cents, period, days in subs:
    m = monthly(cents, period)
    total += m
    idle = days > 60
    if idle:
        saving += m
    flag = f"  unused for {days} days" if idle else ""
    print(f"{name:<10} {period:<7} {money(cents):>7} -> {money(m):>6} a month{flag}")
print(f"monthly {money(total)}, yearly {money(total * 12)}")
print(f"cancelling unused plans saves {money(saving)} a month")
