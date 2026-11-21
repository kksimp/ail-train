deadline = 2 * 1440 + 17 * 60
subs = [("Ana", 41, deadline - 30), ("Ben", 38, deadline + 45), ("Cy", 44, deadline + 61), ("Dot", 35, deadline + 1500), ("Eve", 47, deadline + 3 * 1440 + 100), ("Fin", 30, deadline + 6 * 1440), ("Gus", 4, deadline + 2000)]

def days_late(after):
    late = after - 60
    return 0 if late <= 0 else (late + 1439) // 1440

def final_mark(raw, days):
    return 0 if days > 5 else max(raw - days * 5, 0)

zero = 0
for name, raw, at in subs:
    d = days_late(at - deadline)
    mark = final_mark(raw, d)
    if mark == 0:
        zero += 1
    status = "on time" if d == 0 else f"{d} days late"
    print(f"{name:<4} {status:<12} {raw}/50 -> {mark}/50")
print(f"{zero} pieces scored zero")
