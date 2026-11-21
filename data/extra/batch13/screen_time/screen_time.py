week = [("Mon", 50, 20), ("Tue", 75, 30), ("Wed", 85, 0), ("Thu", 90, 70), ("Fri", 70, 10), ("Sat", 190, 40), ("Sun", 100, 0)]

def allowance(weekend):
    return 120 if weekend else 60

carry = 0
over_days = 0
for i, (name, used, reading) in enumerate(week):
    bonus = min(reading // 2, 30)
    limit = allowance(i >= 5) + bonus + carry
    left = limit - used
    status = f"over by {-left}" if left < 0 else f"{left} spare"
    if left < 0:
        over_days += 1
    carry = min(max(left, 0), 30)
    print(f"{name}: limit {limit:>3} (bonus {bonus:>2}), used {used:>3}, {status}")
print(f"over the limit on {over_days} day(s); {carry} minutes carry into next week")
