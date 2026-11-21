best = None; beaten = 0
for day, kg in enumerate([60, 65, 62, 70, 70, 72]):
    if best is None or kg > best:
        best = kg; beaten += 1; note = "new record"
    else: note = "-"
    print(f"day {day + 1}: {kg} kg {note}")
print(f"records set: {beaten}, best {best} kg")
best = None; beaten = 0
for l in [(100, 5), (100, 6), (95, 10), (105, 3)]:
    if best is None or l > best:
        best = l; beaten += 1; print(f"squat record: {l[0]} kg x {l[1]}")
print(f"best squat {best[0]} x {best[1]} after {beaten} records")
