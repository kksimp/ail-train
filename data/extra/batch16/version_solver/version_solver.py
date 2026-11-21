class Rule:
    def __init__(s, pkg, ver, dep, lo, hi):
        s.pkg, s.ver, s.dep, s.lo, s.hi = pkg, ver, dep, lo, hi

def consistent(chosen, rules):
    for r in rules:
        owner_ok = r.pkg < 0 or chosen[r.pkg] == r.ver
        if owner_ok and chosen[r.dep] > 0:
            v = chosen[r.dep]
            if v < r.lo or v > r.hi:
                return False
    return True

def solve(i, chosen, versions, rules, tries):
    if i == len(chosen):
        return True
    for v in versions[i]:
        chosen[i] = v
        tries[0] += 1
        if consistent(chosen, rules) and solve(i + 1, chosen, versions, rules, tries):
            return True
    chosen[i] = 0
    return False

names = ["web", "db", "log"]
versions = [[3, 2, 1], [2, 1], [3, 2, 1]]
rules = [Rule(-1, 0, 0, 2, 99), Rule(0, 3, 1, 2, 99), Rule(0, 3, 2, 3, 99), Rule(0, 2, 2, 2, 99), Rule(1, 2, 2, 1, 2), Rule(1, 1, 2, 1, 1)]
for r in rules:
    owner = "root" if r.pkg < 0 else f"{names[r.pkg]} {r.ver}"
    print(f"{owner:<6} needs {names[r.dep]} {r.lo} to {r.hi}")
chosen = [0, 0, 0]
tries = [0]
if solve(0, chosen, versions, rules, tries):
    picks = ", ".join(f"{names[i]} {chosen[i]}" for i in [0, 1, 2])
    print(f"solution: {picks}")
else:
    print("no solution")
print(f"versions tried: {tries[0]}")
