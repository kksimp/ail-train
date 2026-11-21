def band(h):
    if 0 <= h <= 6:
        return 20
    if 18 <= h <= 21:
        return 15
    if 22 <= h <= 23:
        return 20
    return 10

def extra_halves(m):
    return 0 if m <= 30 else (m - 30 + 29) // 30

def money(c):
    return f"{c // 100}.{c % 100:02d}"

jobs = [("Mon", 10, 25), ("Tue", 19, 50), ("Fri", 23, 95), ("Sun", 14, 30), ("Sun", 3, 61), ("Wed", 7, 120)]
total = 0
for day, hour, mins in jobs:
    base = 6000 * band(hour) // 10
    sunday = 2500 if day == "Sun" else 0
    tm = extra_halves(mins) * 3000
    charge = base + sunday + tm
    total += charge
    mult = band(hour)
    print(f"{day} {hour:02d}:00, {mins:>3} min: base {money(base)} (x{mult // 10}.{mult % 10}) + Sunday {money(sunday)} + time {money(tm)} = {money(charge)}")
print(f"week's call-outs: {money(total)}")
