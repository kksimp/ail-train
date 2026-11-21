dishes = [("potatoes", 200, 50), ("yorkshires", 220, 25), ("stuffing", 190, 35), ("lamb", 180, 90), ("gratin", 180, 60), ("parsnips", 200, 40), ("crumble", 175, 45)]

def group_temps(ts):
    groups = []
    for i, t in enumerate(ts):
        if not groups or ts[groups[-1][0]] - t > 10:
            groups.append([i])
        else:
            groups[-1].append(i)
    return groups

def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

hot = sorted(dishes, key=lambda d: -d[1])
groups = list(reversed(group_temps([d[1] for d in hot])))
total = sum(max(hot[i][2] for i in g) for g in groups)
t = 19 * 60 - total
print(f"oven on by {hhmm(t)}")
for g in groups:
    finish = t + max(hot[i][2] for i in g)
    parts = [f"{hot[i][0]} in {hhmm(finish - hot[i][2])}" for i in g]
    print(f"{hot[g[0]][1]} C until {hhmm(finish)}: {', '.join(parts)}")
    t = finish
