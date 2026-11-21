teams = ["Otters", "Herons", "Badgers", "Foxes"]
wins = [[0, 4, 5, 6], [2, 0, 4, 5], [1, 2, 0, 4], [0, 1, 2, 0]]
n = len(teams)
p = [1.0, 1.0, 1.0, 1.0]
for rnd in range(200):
    nxt = []
    for i in range(n):
        w = float(sum(wins[i]))
        den = 0.0
        for j in range(n):
            if j != i:
                games = float(wins[i][j] + wins[j][i])
                den += games / (p[i] + p[j])
        nxt.append(w / den)
    total = 0.0
    for x in nxt:
        total = total + x
    p = [x * float(n) / total for x in nxt]
for i in range(n):
    print(f"{teams[i]:<8} won {sum(wins[i]):>2}  strength {p[i]:.3f}")
for i, j in [(0, 1), (0, 3), (1, 2), (2, 3)]:
    chance = p[i] / (p[i] + p[j]) * 100.0
    print(f"{teams[i]} beat {teams[j]} {chance:.1f}% of the time")
