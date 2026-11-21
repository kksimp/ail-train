h = a = 0
for side in ["home", "away", "home"]:
    if side == "home": h += 1
    else: a += 1
print(f"half time {h}-{a}")
hh, ha = h, a
for side in ["home", "away", "away"]:
    if side == "home": h += 1
    else: a += 1
print(f"pitchside: {h}-{a}"); print(f"press box: {h}-{a}")
print("same cell: true")
print(f"half-time copy stays {hh}-{ha}")
