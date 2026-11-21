def job(a, today):
    room, inst, tested, batt = a
    if today - inst >= 3650:
        return "Replace"
    if today - batt >= 365:
        return "Battery"
    if today - tested > 30:
        return "Test"
    return "Fine"

def describe(a, today):
    j = job(a, today)
    if j == "Replace":
        return f"replace the unit (fitted {today - a[1]} days ago)"
    if j == "Battery":
        return f"change the battery ({today - a[3]} days old)"
    if j == "Test":
        return f"press the test button ({today - a[2]} days since)"
    return "fine"

today = 4000
alarms = [("hall", 100, 3990, 3800), ("landing", 900, 3950, 3700), ("kitchen", 2500, 3900, 3500), ("loft", 350, 3000, 3000), ("bedroom", 3000, 3985, 3640)]
counts = {}
for a in alarms:
    counts[job(a, today)] = counts.get(job(a, today), 0) + 1
    print(f"{a[0]:<8} {describe(a, today)}")
for j in ["Replace", "Battery", "Test", "Fine"]:
    print(f"{j}: {counts.get(j, 0)}")
