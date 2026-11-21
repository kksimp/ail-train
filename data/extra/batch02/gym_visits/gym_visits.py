DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
log = ["Mon ana", "Mon ben", "Tue ana", "Wed cai", "Wed ana", "Wed ben", "Fri dee", "Sat ana", "Sat cai", "Sat ben", "Sat dee", "Sun ben"]
pd, pm = {}, {}
for e in log:
    d, m = e.split()
    pd[d] = pd.get(d, 0) + 1; pm[m] = pm.get(m, 0) + 1
for d in DAYS:
    n = pd.get(d, 0)
    print(f"{d} {'|' * n} {n}")
print(f"busiest: {max(DAYS, key=lambda d: pd.get(d, 0))}")
print("regulars: " + ", ".join(sorted(m for m in pm if pm[m] >= 3)))
print("no visits: " + ", ".join(d for d in DAYS if d not in pd))
