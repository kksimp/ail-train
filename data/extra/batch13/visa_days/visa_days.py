def days_in_window(trips, last):
    first = last - 179
    n = 0
    for t in trips:
        a = max(t[0], first)
        b = min(t[1], last)
        if b >= a:
            n += b - a + 1
    return n

trips = [[10, 40], [70, 95], [130, 150], [160, 178], [250, 262]]
taken = []
for t in trips:
    taken.append(t)
    used = days_in_window(taken, t[1])
    status = f"OVERSTAY by {used - 90}" if used > 90 else f"ok, {90 - used} left"
    print(f"trip day {t[0]:>3} to {t[1]:>3}: {used:>2} days in window, {status}")
start = 290
length = 0
while True:
    plan = list(taken)
    plan.append([start, start + length])
    if days_in_window(plan, start + length) > 90:
        break
    length += 1
print(f"a trip from day {start} can last {length} days")
