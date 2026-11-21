days = [[101, 102, 103, 101, 104], [102, 105, 101, 105, 106], [107, 101, 102, 108, 103]]
ever = set(); per = []
for d, scans in enumerate(days):
    today = set(); f = b = a = 0
    for i in scans:
        if i in today: a += 1; continue
        today.add(i)
        if i not in ever: ever.add(i); f += 1
        else: b += 1
    per.append(today)
    print(f"day {d + 1}: {f} new, {b} returning, {a} re-entries")
print(f"came every day: {sorted(per[0] & per[1] & per[2])}")
print(f"{len(ever)} different members visited")
