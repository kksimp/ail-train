def sign(pct):
    if abs(pct) >= 20.0:
        return "very steep"
    if abs(pct) >= 10.0:
        return "steep"
    return ""

route = [(0, 120), (400, 136), (650, 166), (800, 199), (1200, 211), (1500, 181), (1700, 141), (2300, 129)]
steepest = 0.0
warn = 0
for i in range(len(route) - 1):
    a = route[i]
    b = route[i + 1]
    run = b[0] - a[0]
    rise = b[1] - a[1]
    pct = rise / run * 100.0
    one_in = 0 if rise == 0 else run // abs(rise)
    s = sign(pct)
    if s != "":
        warn += 1
    if abs(pct) > abs(steepest):
        steepest = pct
    label = f"{a[0]}-{b[0]} m"
    print(f"{label:<12} {rise:>4} m  {pct:>6.1f}%  1 in {one_in:<3} {s}".rstrip())
total = route[-1][1] - route[0][1]
print(f"net change {total} m, steepest {steepest:.1f}%, {warn} warning signs")
