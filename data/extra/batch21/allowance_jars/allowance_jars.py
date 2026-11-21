def jars(c):
    spend = c * 50 // 100
    give = c * 10 // 100
    return [spend, c - spend - give, give]

def weeks_to(goal, w):
    return (goal + w - 1) // w

def money(c):
    return f"{c // 100}.{c % 100:02d}"

kids = [("Mia", 7, 2500), ("Leo", 9, 4000), ("Ivy", 12, 9999), ("Sam", 5, 1200), ("Ola", 11, 3300)]
charity = 0
for name, age, goal in kids:
    wk = age * 50
    j = jars(wk)
    w = weeks_to(goal, j[1])
    charity += j[2] * w
    print(f"{name:<4} {money(wk)}/week: spend {money(j[0])}, save {money(j[1])}, give {money(j[2])}; goal {money(goal)} in {w} weeks")
fastest = min(kids, key=lambda k: weeks_to(k[2], jars(k[1] * 50)[1]))
print(f"first to reach a goal: {fastest[0]}")
print(f"given to charity by then: {money(charity)}")
