houses = [("1 Elm Rd", 4, 1, 1200), ("3 Elm Rd", 8, 2, 1500), ("7 Elm Rd", 4, 4, 1000), ("2 Oak St", 4, 1, 1800), ("9 Oak St", 8, 5, 2200), ("4 Ash Cl", 4, 2, 900), ("6 Ash Cl", 8, 1, 1300)]

def due(week, every, first):
    return week >= first and (week - first) % every == 0

best_week, best_n, total = 0, -1, 0
for week in range(1, 9):
    on = [h for h in houses if due(week, h[1], h[2])]
    pay = sum(h[3] for h in on)
    total += pay
    if len(on) > best_n:
        best_n = len(on)
        best_week = week
    print(f"week {week}: {len(on)} houses, {pay // 100}.{pay % 100:02d}")
busy = [h[0] for h in houses if due(best_week, h[1], h[2])]
print(f"busiest week {best_week}: {', '.join(busy)}")
print(f"eight weeks takings {total // 100}.{total % 100:02d}")
