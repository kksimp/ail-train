boxes = [("large", [60, 40, 40]), ("small", [20, 15, 10]), ("long", [100, 12, 12]), ("medium", [35, 25, 20])]
def vol(d):
    r = 1
    for x in d:
        r *= x
    return r
def fits(item, b):
    a, c = sorted(item), sorted(b[1])
    return all(a[i] <= c[i] for i in range(3))
for item in [[10, 18, 9], [90, 10, 5], [30, 30, 30], [70, 50, 10], [24, 22, 34]]:
    label = "x".join(str(d) for d in item)
    fit = [b for b in boxes if fits(item, b)]
    if fit:
        b = min(fit, key=lambda b: vol(b[1]))
        print(f"{label}: {b[0]} (spare {vol(b[1]) - vol(item)})")
    else:
        print(f"{label}: no box")
