rain = [0, 4, 12, 0, 0, 0, 1, 25, 18, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
cap = 200
level = 60
overflow = tap = short_days = 0
for d, mm in enumerate(rain):
    level += mm * 12 * 9 // 10
    if level > cap:
        overflow += level - cap
        level = cap
    if mm < 2:
        if level >= 25:
            level -= 25
        else:
            tap += 25 - level
            level = 0
            short_days += 1
    if d % 3 == 2:
        bar = "#" * (level // 10)
        print(f"day {d + 1:>2}: {level:>3} L |{bar}")
print(f"overflowed {overflow} L; tap water {tap} L on {short_days} days")
