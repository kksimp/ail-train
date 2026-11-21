def rate_at(minute):
    h = (minute % 1440) // 60
    if 18 <= h < 23:
        return 2150
    if h >= 23 or h < 7:
        return 2300
    return 2000

def shift_pay(a, b):
    return sum(rate_at(m) for m in range(a, b)) // 60

def clock(m):
    return f"{(m % 1440) // 60:02d}:{m % 60:02d}"

def money(c):
    return f"{c // 100}.{c % 100:02d}"

shifts = [("Mon", 540, 1020), ("Tue", 840, 1320), ("Wed", 1320, 1860), ("Thu", 1080, 1590), ("Sat", 300, 780)]
week = 0
extra = 0
for day, a, b in shifts:
    pay = shift_pay(a, b)
    plain = (b - a) * 2000 // 60
    week += pay
    extra += pay - plain
    print(f"{day} {clock(a)}-{clock(b)}: {money(pay):>6} (premium {money(pay - plain)})")
print(f"week {money(week)}, of which premium {money(extra)}")
