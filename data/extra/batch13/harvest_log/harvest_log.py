picks = [(27, "beans", 450), (27, "courgette", 1200), (28, "beans", 820), (28, "tomato", 600), (28, "courgette", 2100), (29, "tomato", 1500), (29, "beans", 640), (30, "tomato", 2300), (30, "courgette", 900), (31, "tomato", 1800), (31, "beans", 200)]
expected = {"beans": [400, 6], "courgette": [3000, 2], "tomato": [2500, 3]}
per_crop = {}
per_week = {}
for week, crop, grams in picks:
    per_crop[crop] = per_crop.get(crop, 0) + grams
    per_week[week] = per_week.get(week, 0) + grams
for crop, total in per_crop.items():
    e = expected.get(crop, [0, 1])
    goal = e[0] * e[1]
    pct = total * 100 // goal
    print(f"{crop:<10} {total:>5} g of {goal:>5} g expected ({pct}%)")
weeks = sorted(per_week.keys())
best = weeks[0]
for w in weeks:
    kg = per_week[w] // 1000
    rest = per_week[w] % 1000 // 100
    print(f"week {w}: {kg}.{rest} kg")
    if per_week[w] > per_week[best]:
        best = w
print(f"best week: {best}")
