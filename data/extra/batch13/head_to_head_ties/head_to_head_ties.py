teams = ["Ards", "Bray", "Cobh", "Derry"]
results = [("Ards", "Bray", 2, 1), ("Cobh", "Derry", 0, 0), ("Bray", "Cobh", 5, 0), ("Derry", "Ards", 1, 0), ("Ards", "Cobh", 1, 1), ("Bray", "Derry", 0, 1), ("Cobh", "Ards", 0, 4), ("Derry", "Bray", 0, 2), ("Bray", "Ards", 3, 0)]

def points_for(results, team, among):
    pts = gd = 0
    for h, a, hg, ag in results:
        if h not in among or a not in among:
            continue
        if h == team or a == team:
            mine = hg if h == team else ag
            theirs = ag if h == team else hg
            gd += mine - theirs
            pts += 3 if mine > theirs else (1 if mine == theirs else 0)
    return [pts, gd]

overall = {}
for t in teams:
    overall[t] = points_for(results, t, teams)
    print(f"{t:<6} {overall[t][0]:>2} pts, goal difference {overall[t][1]}")

def tie_key(t):
    level = [x for x in teams if overall[x][0] == overall[t][0]]
    h = points_for(results, t, level)
    return h[0] * 100 + h[1]

ranked = sorted(teams, key=lambda t: (-overall[t][0], -tie_key(t), -overall[t][1]))
for i, t in enumerate(ranked):
    print(f"{i + 1}. {t}")
