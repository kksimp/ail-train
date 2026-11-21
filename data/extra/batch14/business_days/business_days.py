import datetime
hol = [[1, 1], [4, 3], [4, 6], [5, 4], [5, 25], [8, 31], [12, 25], [12, 28]]
base = datetime.date(1970, 1, 1)
def num(y, m, d):
    return (datetime.date(y, m, d) - base).days
holidays = {num(2026, m, d) for m, d in hol}
def is_workday(day):
    wd = (day + 4) % 7
    return wd != 0 and wd != 6 and day not in holidays
def civil(z):
    d = base + datetime.timedelta(days=z)
    return f"{d.year}-{d.month:02}-{d.day:02}"
total = 0
for q in range(4):
    a = num(2026, q * 3 + 1, 1)
    b = num(2027, 1, 1) if q == 3 else num(2026, q * 3 + 4, 1)
    n = len([d for d in range(a, b) if is_workday(d)])
    total += n
    print(f"Q{q + 1} 2026: {b - a} days, {n} working days")
print(f"2026 has {total} working days")
names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
for m, d, n in [[12, 18, 10], [3, 30, 5], [11, 21, 3]]:
    start = num(2026, m, d)
    day = start
    left = n
    while left > 0:
        day += 1
        if is_workday(day):
            left -= 1
    print(f"{civil(start)} + {n} working days = {civil(day)} ({names[(day + 4) % 7]})")
