def hhmm(t):
    return f"{t // 60:02d}:{t % 60:02d}"

sights = [("Castle", 570, 1020, 90), ("Gallery", 600, 1050, 60), ("Cathedral", 540, 720, 45), ("Market", 480, 840, 40), ("Gardens", 600, 1110, 50)]
walk = [[0, 15, 20, 10, 12, 25], [15, 0, 10, 12, 18, 20], [20, 10, 0, 14, 16, 8], [10, 12, 14, 0, 6, 22], [12, 18, 16, 6, 0, 19], [25, 20, 8, 22, 19, 0]]
t = 540
at = 0
seen = set()
while True:
    pick = -1
    for i, s in enumerate(sights):
        arrive = max(t + walk[at][i + 1], s[1])
        fits = arrive + s[3] <= s[2]
        if i not in seen and fits and (pick < 0 or s[2] < sights[pick][2]):
            pick = i
    if pick < 0:
        break
    s = sights[pick]
    reach = t + walk[at][pick + 1]
    start = max(reach, s[1])
    t = start + s[3]
    at = pick + 1
    seen.add(pick)
    print(f"{hhmm(start)}-{hhmm(t)} {s[0]} (waited {start - reach} min)")
t += walk[at][0]
print(f"back at the hotel {hhmm(t)}")
print(f"missed: {len([s for i, s in enumerate(sights) if i not in seen])}")
