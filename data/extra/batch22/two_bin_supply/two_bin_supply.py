def simulate(use, b, lead, log):
    front = b
    back = b
    due = -1
    short = 0
    for day in range(len(use)):
        if day == due:
            back = b
            due = -1
            if log:
                print(f"day {day + 1:>2}: refill arrives")
        need = use[day]
        while need > 0:
            if front > 0:
                take = min(need, front)
                front -= take
                need -= take
            elif back > 0:
                front = back
                back = 0
                due = day + lead
                if log:
                    print(f"day {day + 1:>2}: front bin empty, card sent")
            else:
                short += need
                if log:
                    print(f"day {day + 1:>2}: short {need}")
                need = 0
    return short

use = [6, 8, 5, 9, 7, 10, 4, 8, 12, 6, 9, 11, 5, 7, 8, 10, 6, 9, 7, 8]
short = simulate(use, 30, 3, True)
print(f"bins of 30, lead 3 days: {short} short")
for b in [20, 25, 35]:
    print(f"bins of {b}: {simulate(use, b, 3, False)} short")
