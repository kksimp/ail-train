def fits(rule, v):
    return rule[0] <= v <= rule[1] or rule[2] <= v <= rule[3]

names = ["class", "row", "seat"]
rules = [[1, 3, 5, 7], [6, 11, 33, 44], [13, 40, 45, 50]]
mine = [35, 6, 19]
nearby = [[33, 3, 47], [40, 4, 50], [38, 1, 14], [55, 2, 20], [40, 5, 45], [38, 6, 12]]
errors = 0; good = []
for p in nearby:
    bad = [v for v in p if not any(fits(r, v) for r in rules)]
    errors += sum(bad)
    if not bad: good.append(p)
print(f"part 1: error rate {errors}, {len(good)} passes are valid")
cands = [{f for f in range(len(rules)) if all(fits(rules[f], p[col]) for p in good)} for col in range(len(mine))]
field_of = [-1, -1, -1]; fixed = 0
while fixed < len(mine):
    for col in range(len(cands)):
        if field_of[col] < 0 and len(cands[col]) == 1:
            f = list(cands[col])[0]
            field_of[col] = f; fixed += 1
            for o in cands: o.discard(f)
product = 1
for col in range(len(mine)):
    print(f"column {col} is {names[field_of[col]]}: {mine[col]}")
    product *= mine[col]
print(f"part 2: product of my pass {product}")
