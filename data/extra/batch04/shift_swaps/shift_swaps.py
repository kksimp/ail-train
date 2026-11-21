D = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
R = {"mon": "Ida", "tue": "Jon", "wed": "Ida", "thu": "Kit", "fri": "Jon", "sat": "Kit", "sun": "Ida"}
cnt = lambda w: sum(1 for x in R.values() if x == w)
for d, t, a in [("tue", "Ida", True), ("thu", "Jon", True), ("sat", "Ida", False), ("mon", "Kit", True)]:
    g = R[d]
    if not a: print(f"{d}: {t} did not agree")
    elif cnt(t) >= 3: print(f"{d}: {t} already has {cnt(t)} shifts")
    else: R[d] = t; print(f"{d}: {g} -> {t}")
print(" ".join(f"{d}={R[d]}" for d in D))
