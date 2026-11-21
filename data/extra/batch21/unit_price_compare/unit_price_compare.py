packs = [("rice", "500 g bag", 500, 129, 1, 129), ("rice", "2 kg sack", 2000, 450, 1, 450), ("rice", "1 kg bag, 2 for 4", 1000, 249, 2, 400), ("pasta", "500 g", 500, 95, 1, 95), ("pasta", "750 g, 3 for 5", 750, 199, 3, 500), ("oats", "1 kg", 1000, 175, 1, 175), ("oats", "500 g organic", 500, 110, 1, 110)]

def per100(p):
    each = float(p[5]) / float(p[4])
    return each / float(p[2])

kinds = []
for p in packs:
    if p[0] not in kinds:
        kinds.append(p[0])
    print(f"{p[0]:<6} {p[1]:<18} {per100(p):.3f} per 100 g")
for k in kinds:
    group = [p for p in packs if p[0] == k]
    best = min(group, key=lambda p: int(per100(p) * 100000.0))
    worst = max(group, key=lambda p: int(per100(p) * 100000.0))
    ratio = per100(worst) / per100(best)
    print(f"best {k}: {best[1]} ({ratio:.2f}x cheaper than the dearest)")
