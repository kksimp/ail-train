times = [1, 8, 15]; vals = [450, 399, 420]
def at(times, vals, t):
    f = -1
    for i in range(len(times)):
        if times[i] <= t: f = i
    return None if f < 0 else vals[f]
for day in [0, 1, 7, 8, 20]:
    p = at(times, vals, day) or 0
    shown = "not listed" if p == 0 else f"{p // 100}.{p % 100:02}"
    print(f"day {day:>2}: {shown}")
pt = [0, 30, 34]; pv = ["green", "amber", "red"]
checks = [5, 31, 34, 60]
print(f"light at {checks}: {', '.join(at(pt, pv, t) for t in checks)}")
