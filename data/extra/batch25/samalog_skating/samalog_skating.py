def hundredths(t):
    mins = 0
    rest = t
    if ":" in t:
        parts = t.split(":")
        mins = int(parts[0])
        rest = parts[1]
    secs = rest.split(".")
    return (mins * 60 + int(secs[0])) * 100 + int(secs[1])

def leg_points(t, distance):
    return hundredths(t) * 10 * 500 // distance

def thousandths(points):
    whole = points // 1000
    frac = points % 1000
    pad = ""
    if frac < 10:
        pad = "00"
    elif frac < 100:
        pad = "0"
    return f"{whole}.{pad}{frac}"

distances = [500, 5000, 1500, 10000]
skaters = [("Anke", ["36.85", "6:21.40", "1:46.95", "13:12.80"]), ("Bram", ["35.90", "6:30.10", "1:45.20", "13:30.55"]), ("Cees", ["37.40", "6:15.05", "1:48.10", "12:58.30"])]
print("skater  500m    5000m   1500m   10000m  total")
best_name = ""
best = 0
second = 0
for name, times in skaters:
    row = []
    total = 0
    for i in range(4):
        p = leg_points(times[i], distances[i])
        total += p
        row.append(thousandths(p))
    cells = "  ".join(row)
    print(f"{name:<6}  {cells}  {thousandths(total)}")
    if best_name == "" or total < best:
        second = best
        best = total
        best_name = name
    elif second == 0 or total < second:
        second = total
print(f"champion {best_name}, ahead by {thousandths(second - best)} points")
