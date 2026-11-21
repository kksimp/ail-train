def score(spells):
    s = len(spells); return s * s * sum(spells)
def action(b):
    if b <= 50: return "no action"
    if b <= 200: return "informal chat"
    if b <= 650: return "first written review"
    return "final review"
staff = [("Ada", [12]), ("Bill", [1, 1, 2, 1, 1, 1]), ("Chen", [3, 2]), ("Dee", [1, 2, 1, 1]), ("Eli", []), ("Fay", [5, 1, 1, 2, 1, 3, 1, 2])]
for name, spells in staff:
    b = score(spells)
    print(f"{name:<5} {len(spells)} spells, {sum(spells):>2} days: score {b:>4}, {action(b)}")
same = [score([6]), score([3, 3]), score([2, 2, 2]), score([1] * 6)]
print(f"six days off as 1, 2, 3 or 6 spells: [{', '.join(str(x) for x in same)}]")
