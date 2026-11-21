import datetime
lp = lambda y: (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
print(f"leap days 1901-2100: {sum(1 for y in range(1901, 2101) if lp(y))}")
for y, m, d in [(2000, 1, 1), (2024, 2, 29), (2026, 11, 21), (1969, 7, 20)]:
    print(f"{y}-{m:02d}-{d:02d}: {datetime.date(y, m, d).strftime('%A')}")
f = []; y = 2026
while len(f) < 3:
    if lp(y) and datetime.date(y, 2, 29).weekday() == 5: f.append(y)
    y += 1
print(f"29 February on a Saturday: {f}")
