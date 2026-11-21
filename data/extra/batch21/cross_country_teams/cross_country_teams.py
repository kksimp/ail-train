finish = "ABCBABACBAACBCBCDDDACDDEE"
names = {'A': "Alder", 'B': "Beech", 'C': "Cedar", 'D': "Damson", 'E': "Elm"}
places = {}
for i, c in enumerate(finish):
    places.setdefault(c, []).append(i + 1)

def score(ps):
    return sum(ps[:5])

def sixth(ps):
    return ps[5] if len(ps) > 5 else 999

scoring = []
for club, ps in places.items():
    if len(ps) >= 5:
        scoring.append(club)
    else:
        print(f"{names[club]}: only {len(ps)} finishers, no team score")
ranked = sorted(scoring, key=lambda c: (score(places[c]), sixth(places[c])))
for i, c in enumerate(ranked):
    ps = places[c]
    top = "[" + ", ".join(str(x) for x in ps[:5]) + "]"
    sx = "none" if sixth(ps) == 999 else f"{sixth(ps)}"
    print(f"{i + 1}. {names[c]:<7} {score(ps):>3} points {top} (6th runner {sx})")
a, b = ranked[0], ranked[1]
if score(places[a]) == score(places[b]):
    print(f"{names[a]} beat {names[b]} on the sixth runner")
