table = {}

def award(table, team, score, other, tries):
    r = table.get(team, {"played": 0, "points": 0, "diff": 0, "bonus": 0})
    r["played"] += 1
    r["diff"] += score - other
    if score > other:
        r["points"] += 4
    elif score == other:
        r["points"] += 2
    extra = 0
    if tries >= 4:
        extra += 1
    if score < other and other - score <= 7:
        extra += 1
    r["points"] += extra
    r["bonus"] += extra
    table[team] = r

results = [("Lions", 31, 5, "Bears", 24, 3), ("Hawks", 18, 1, "Wolves", 18, 2), ("Bears", 40, 6, "Hawks", 10, 1), ("Wolves", 22, 2, "Lions", 27, 4), ("Lions", 12, 1, "Hawks", 15, 0), ("Bears", 33, 4, "Wolves", 29, 4)]
for home, hs, ht, away, aws, at in results:
    award(table, home, hs, aws, ht)
    award(table, away, aws, hs, at)
names = sorted(table.keys(), key=lambda n: (-table[n]["points"], -table[n]["diff"]))
print("team     P  BP  diff  pts")
for n in names:
    r = table[n]
    print(f"{n:<7} {r['played']:>2} {r['bonus']:>3} {r['diff']:>5} {r['points']:>4}")
