weight = 72
target = weight * 35
log = [(1, "water", 500), (1, "coffee", 250), (1, "water", 750), (1, "tea", 300), (1, "water", 600), (2, "coffee", 500), (2, "water", 400), (2, "juice", 200), (3, "water", 1000), (3, "tea", 600), (3, "water", 900), (3, "water", 300), (4, "water", 250), (4, "coffee", 750), (5, "water", 1500), (5, "tea", 250), (5, "water", 700)]

def counted(kind, ml):
    return ml * 8 // 10 if kind in ("coffee", "tea") else ml

per_day = {}
for day, kind, ml in log:
    per_day[day] = per_day.get(day, 0) + counted(kind, ml)
met = 0
sum_all = 0
for day, ml in per_day.items():
    pct = ml * 100 // target
    sum_all += ml
    if ml >= target:
        met += 1
    print(f"day {day}: {ml:>4} ml {pct:>3}% |{'=' * (pct // 10)}")
print(f"target {target} ml; met on {met} of {len(per_day)} days; average {sum_all // len(per_day)} ml")
