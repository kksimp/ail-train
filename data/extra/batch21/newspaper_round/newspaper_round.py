houses = [(2, True, True, []), (5, True, False, [[3, 9]]), (8, False, True, [[6, 6]]), (11, True, True, [[0, 13]]), (14, True, False, [[0, 1], [12, 13]])]

def held(day, holds):
    return any(h[0] <= day <= h[1] for h in holds)

def money(c):
    return f"{c // 100}.{c % 100:02d}"

rnd = 0
for number, daily, sunday, holds in houses:
    bill = papers = 0
    for week in range(2):
        any_week = False
        for d in range(week * 7, week * 7 + 7):
            is_sun = d % 7 == 6
            wanted = sunday if is_sun else daily
            if wanted and not held(d, holds):
                bill += 300 if is_sun else 180
                papers += 1
                any_week = True
        if any_week:
            bill += 150
    rnd += bill
    print(f"no. {number:>2}: {papers:>2} papers, bill {money(bill)}")
print(f"fortnight takings {money(rnd)}")
