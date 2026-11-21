DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day = 1
for k in range(5):
    rem = (day - 3 + 7) % 7
    print(f"collection {k + 1}: day {k * 9} ({DAYS[day]}), reminder {DAYS[rem]}")
    day = (day + 9 % 7) % 7
print(f"30 days after Tue is {DAYS[(1 + 30 % 7) % 7]}")
w = 0; d = 1
for k in range(14):
    if d >= 5:
        w += 1
    d = (d + 2) % 7
print(f"weekend collections in the first 14: {w}")
