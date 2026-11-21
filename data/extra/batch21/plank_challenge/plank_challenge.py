missed = {9, 17, 18}
target = 20
week_total = longest = two_min = total = 0

def mmss(s):
    return f"{s // 60}:{s % 60:02d}"

for day in range(1, 31):
    if day % 4 != 0 and day not in missed:
        week_total += target
        longest = max(longest, target)
        if target >= 120 and two_min == 0:
            two_min = day
        target += 5
    if day % 7 == 0 or day == 30:
        print(f"week {(day + 6) // 7}: {mmss(week_total)} holding")
        total += week_total
        week_total = 0
print(f"longest hold {mmss(longest)}, total {mmss(total)}")
if two_min > 0:
    print(f"first two-minute hold on day {two_min}")
else:
    print(f"two minutes not reached; next target {mmss(target)}")
