import math

def poisson(l, n):
    ps = [math.exp(-l)]
    for k in range(1, n + 1):
        ps.append(ps[k - 1] * l / float(k))
    return ps

home = poisson(1.6, 5)
away = poisson(1.1, 5)
win = draw = lose = over = 0.0
best = (0, 0)
print("home goals down, away goals across, 0 to 5")
for h in range(6):
    cells = []
    for a in range(6):
        p = home[h] * away[a] * 100.0
        cells.append(f"{p:>5.1f}")
        if h > a:
            win += p
        elif h == a:
            draw += p
        else:
            lose += p
        if h + a > 2:
            over += p
        if p > home[best[0]] * away[best[1]] * 100.0:
            best = (h, a)
    print(f"{h}  {' '.join(cells)}")
print(f"home {win:.1f}%  draw {draw:.1f}%  away {lose:.1f}%  over 2.5 goals {over:.1f}%")
print(f"most likely score {best[0]}-{best[1]}")
