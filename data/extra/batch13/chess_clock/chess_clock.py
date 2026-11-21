def after_move(c, left, used):
    rest = left - used
    if rest < 0:
        return rest
    if c[0] == "Fischer":
        return rest + c[1]
    if c[0] == "Bronstein":
        return rest + min(used, c[1])
    return rest

def show(tenths):
    s = tenths // 10
    return f"{s // 60}:{s % 60:02}.{tenths % 10}"

white = [32, 95, 120, 410, 650, 233, 300, 780, 52, 75, 240, 180]
black = [41, 60, 380, 22, 505, 470, 120, 64, 560, 210, 55, 330]
for c, label in [(("Fischer", 20), "Fischer +2s"), (("Bronstein", 50), "Bronstein delay 5s"), (("Sudden", 0), "sudden death")]:
    clocks = [3000, 3000]
    flag = ""
    for m in range(len(white)):
        clocks[0] = after_move(c, clocks[0], white[m])
        if clocks[0] < 0:
            flag = f"white flags on move {m + 1}"
            break
        clocks[1] = after_move(c, clocks[1], black[m])
        if clocks[1] < 0:
            flag = f"black flags on move {m + 1}"
            break
    if flag == "":
        print(f"{label}: white {show(clocks[0])}, black {show(clocks[1])}")
    else:
        print(f"{label}: {flag}")
