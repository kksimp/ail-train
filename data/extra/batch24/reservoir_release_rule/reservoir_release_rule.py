def release(level):
    if level > 800: return 100 + (level - 800) // 4
    if level < 400: return min(60, level)
    return 100
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
inflow = [180, 320, 420, 300, 60, 0, 0, 0, 0, 10, 20, 90]
level = 600; short = 0; spilled = 0
for m in range(12):
    level += inflow[m]
    out = release(level)
    level -= out
    spill = max(level - 1000, 0)
    level -= spill; spilled += spill
    if out < 100: short += 100 - out
    print(f"{months[m]}: in {inflow[m]:>3}, out {out:>3}, spill {spill:>3}, level {level:>4}")
print(f"year: {spilled} spilled, demand short by {short}")
