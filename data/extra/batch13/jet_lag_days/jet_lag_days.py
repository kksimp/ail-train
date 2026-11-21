def recovery(d, hours):
    return hours if d == "East" else (hours * 2 + 2) // 3

def clock(minutes):
    m = ((minutes % 1440) + 1440) % 1440
    return f"{m // 60:02}:{m % 60:02}"

trips = [("London to Tokyo", "East", 9), ("New York to Paris", "East", 6), ("Sydney to Perth", "West", 2), ("Berlin to Chicago", "West", 7), ("Delhi to Dubai", "West", 1)]
for name, d, hours in trips:
    pre = min(hours, 3)
    before = recovery(d, hours)
    after = recovery(d, hours - pre)
    print(f"{name:<18} Direction.{d} {hours} h: {before} days to adjust, {after} after {pre} days of shifting")
bedtime = 23 * 60
plan = [f"day -{4 - d} {clock(bedtime - d * 60)}" for d in range(1, 4)]
shown = ", ".join(plan)
print(f"bedtimes before flying to Tokyo: {shown}")
