def day_reached(base, goal):
    level = 1; points = 0
    for day in range(1, 201):
        points += 300 + 20 * day
        while points >= base * level * level // 10 + 100:
            points -= base * level * level // 10 + 100
            level += 1
        if level >= goal: return day
    return -1
pick = 0; pick_gap = 1000
for base in [100, 150, 200, 250, 300, 400]:
    d10 = day_reached(base, 10); d20 = day_reached(base, 20)
    print(f"base {base}: level 10 on day {d10:>2}, level 20 on day {d20:>2}")
    if abs(d10 - 14) < pick_gap:
        pick_gap = abs(d10 - 14); pick = base
print(f"base {pick} lands level 10 closest to day 14")
