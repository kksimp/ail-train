def leap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def money(c):
    return f"{c // 100}.{c % 100:02d}"

day = 4
for y in range(2024, 2034):
    length = 366 if leap(y) else 365
    first = day
    count = 0
    last = day
    while day < length:
        count += 1
        last = day
        day += 14
    day -= length
    per = 5200000 // count
    print(f"{y}: {count} paydays, days {first + 1} to {last + 1}, {money(per)} per payday")
