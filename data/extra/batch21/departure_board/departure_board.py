def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

def status(s):
    if s[3] < 0:
        return "Cancelled"
    if s[3] == 0:
        return "On time"
    return f"Exp {hhmm(s[0] + s[3])}"

def plat(s):
    return f"{s[2]}" if s[4] == 0 else f"{s[4]} (was {s[2]})"

now = 845
allsvc = [(850, "Leeds", 3, 0, 0), (842, "York", 1, 5, 0), (835, "Hull", 2, 0, 0), (858, "Selby", 4, -1, 0), (905, "Doncaster", 3, 12, 5), (912, "Scarborough", 2, 0, 0), (920, "Harrogate", 1, 0, 4), (930, "Wakefield", 3, 0, 0)]
waiting = sorted([s for s in allsvc if s[0] + max(s[3], 0) >= now], key=lambda s: s[0])
print(f"Departures at {hhmm(now)}")
for s in waiting[:5]:
    print(f"{hhmm(s[0])} {s[1]:<12} {plat(s):<10} {status(s)}")
print(f"{len(waiting) - 5} more later")
