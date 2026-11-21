def ls(r, w, h):
    if r: return "locked: program running"
    if w: return "locked: draining water"
    if h: return "locked: cooling down"
    return "open"
temp, water, running, minute = 60, 30, True, 0
while minute < 12:
    st = ls(running, water > 0, temp >= 45)
    print(f"min {minute:>2}: temp {temp}, water {water} l -> {st}")
    if st == "open": break
    if minute == 2: running = False
    if not running: water = max(water - 15, 0)
    temp -= 3; minute += 1
print(f"door opens after {minute} minutes")
