def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

outs = [(420, 495), (510, 590), (600, 668), (720, 790)]
backs = [(900, 975), (1020, 1100), (1140, 1205), (1290, 1360)]
valid = []
for i, o in enumerate(outs):
    for j, b in enumerate(backs):
        stay = b[0] - o[1]
        if stay >= 120 and b[1] <= 1320:
            valid.append([i, j, stay])
print(f"{len(valid)} of {len(outs) * len(backs)} pairs work")
for i, o in enumerate(outs):
    mine = [v for v in valid if v[0] == i]
    if mine:
        v = max(mine, key=lambda v: v[2])
        b = backs[v[1]]
        print(f"out {hhmm(o[0])} -> latest back {hhmm(b[0])}, {v[2] // 60} h {v[2] % 60:02d} m in town")
    else:
        print(f"out {hhmm(o[0])} -> no return fits")
ranked = sorted(valid, key=lambda v: (-v[2], backs[v[1]][1]))
best = ranked[0]
print(f"best: leave {hhmm(outs[best[0]][0])}, home {hhmm(backs[best[1]][1])}")
print(f"shortest workable stay: {ranked[-1][2]} min")
