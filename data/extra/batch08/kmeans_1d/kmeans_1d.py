times = [8.0, 9.5, 11.0, 12.0, 19.0, 21.5, 22.0, 24.0, 23.0, 41.0, 38.5, 45.0, 44.0, 10.0]
cen = [10.0, 20.0, 30.0]
for rnd in range(1, 21):
    groups = [[], [], []]
    for t in times:
        best = 0
        for k in range(1, 3):
            if abs(t - cen[k]) < abs(t - cen[best]): best = k
        groups[best].append(t)
    moved = False
    for k in range(3):
        if groups[k]:
            m = sum(groups[k]) / len(groups[k])
            if m != cen[k]: moved = True
            cen[k] = m
    print(f"round {rnd}: centres {cen[0]:.3f}, {cen[1]:.3f}, {cen[2]:.3f}")
    if not moved: break
for k in range(3): print(f"group {k + 1}: {' '.join(str(x) for x in sorted(groups[k]))}")
