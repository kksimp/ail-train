cap, level, sp, short = 300, 120, 0, 0
for d, mm in enumerate([0, 4, 9, 0, 0, 1, 6]):
    l = mm * 32; room = cap - level
    if l > room: sp += l - room; level = cap
    else: level += l
    got = min(60, level); level -= got; short += 60 - got
    print(f"day {d + 1}: {mm} mm, drew {got} l, level {level}/{cap}")
print(f"spilled {sp} l, garden short by {short} l")
