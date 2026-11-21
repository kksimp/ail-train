ladder = ["Ash", "Bex", "Cal", "Dot", "Eli", "Fin"]
games = [("Dot", "Bex", True), ("Fin", "Cal", True), ("Eli", "Ash", True), ("Cal", "Fin", False), ("Bex", "Ash", True), ("Dot", "Eli", True), ("Gus", "Fin", True)]

def challenge(c, d, won):
    if c not in ladder:
        return False, f"{c} is not on the ladder"
    if d not in ladder:
        return False, f"{d} is not on the ladder"
    ci, di = ladder.index(c), ladder.index(d)
    gap = ci - di
    if gap < 1:
        return False, f"{d} is not above {c}"
    if gap > 2:
        return False, f"{d} is {gap} rungs above {c}, too far"
    if not won:
        return True, f"{d} holds rung {di + 1}"
    ladder.pop(ci)
    ladder.insert(di, c)
    return True, f"{c} climbs to rung {di + 1}"

for c, d, won in games:
    ok, msg = challenge(c, d, won)
    print(msg if ok else f"refused: {msg}")
for i, name in enumerate(ladder):
    print(f"{i + 1}. {name}")
