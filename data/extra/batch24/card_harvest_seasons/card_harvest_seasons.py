state = 3030
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def score(hand, season):
    matching = [c for c in hand if c[0] == season]
    points = sum(c[1] for c in matching)
    if len(matching) == 3: points += 5
    return [points, len(hand) - len(matching)]
seasons = ["spring", "summer", "autumn"]
totals = [0, 0]; compost = [0, 0]
for rnd in range(6):
    season = rnd % 3
    line = []
    for p in range(2):
        hand = []
        for k in range(3):
            s = below(3); v = 1 + below(6)
            hand.append((s, v))
        r = score(hand, season)
        totals[p] += r[0]; compost[p] += r[1]
        line.append(f"P{p + 1} +{r[0]}")
    print(f"year {rnd // 3 + 1} {seasons[season]:<6}: {', '.join(line)}")
for p in range(2):
    print(f"player {p + 1}: {totals[p]} from crops + {compost[p]} compost = {totals[p] + compost[p]}")
