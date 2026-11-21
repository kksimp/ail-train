def mean(xs):
    return float(sum(xs)) / float(len(xs))
def zone(r):
    return "undertrained" if r < 0.8 else ("safe" if r <= 1.3 else ("caution" if r <= 1.5 else "danger"))
loads = []
for day in range(42):
    base = 0 if day % 7 == 6 else 300 + (day % 3) * 50
    extra = 250 if day >= 35 else 0
    loads.append(base + extra)
for day in [27, 30, 34, 37, 41]:
    acute = mean(loads[day - 6:day + 1])
    chronic = mean(loads[day - 27:day + 1])
    r = acute / chronic
    print(f"day {day + 1}: acute {acute:.1f}, chronic {chronic:.1f}, ratio {r:.2f} ({zone(r)})")
