def kg(quarters):
    whole = quarters // 4
    r = quarters % 4
    return [f"{whole}", f"{whole}.25", f"{whole}.5", f"{whole}.75"][r]

def load(target):
    bar = 80
    if target < bar:
        return None, "lighter than the bar"
    side = (target - bar) // 2
    if (target - bar) % 2 != 0:
        return None, "needs uneven sides"
    plates = []
    for p in [100, 80, 60, 40, 20, 10, 5]:
        used = 0
        while side >= p and used < 2:
            plates.append(p)
            side -= p
            used += 1
    if side != 0:
        return None, f"short by {kg(side * 2)} kg"
    return plates, None

for t in [100.0, 102.5, 147.5, 60.0, 61.25, 222.5, 302.5]:
    quarters = int(t * 4.0)
    plates, err = load(quarters)
    if plates is not None:
        shown = ", ".join(kg(p) for p in plates)
        print(f"{kg(quarters):>6} kg: {shown} per side")
    else:
        print(f"{kg(quarters):>6} kg: {err}")
