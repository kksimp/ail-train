lots = [("Elm Row", ("street", "brown", [2, 10, 30, 90, 160, 250]), "Ana", 0), ("Oak Lane", ("street", "brown", [4, 20, 60, 180, 320, 450]), "Ana", 2), ("Quay St", ("street", "blue", [35, 175, 500, 1100, 1300, 1500]), "Ben", 0), ("Park Rd", ("street", "blue", [50, 200, 600, 1400, 1700, 2000]), "Ana", 0), ("North Station", ("station",), "Ben", 0), ("East Station", ("station",), "Ben", 0), ("West Station", ("station",), "Ben", 0), ("Power Works", ("utility",), "Ana", 0), ("Water Works", ("utility",), "Ben", 0)]

def has_group(l, group):
    return l[1][0] == "street" and l[1][1] == group

def owns_group(lots, owner, group):
    return all(not has_group(l, group) or l[2] == owner for l in lots)

def rent(lots, l, dice):
    same = sum(1 for x in lots if x[2] == l[2] and x[1] == l[1])
    kind = l[1]
    if kind[0] == "street":
        if l[3] == 0 and owns_group(lots, l[2], kind[1]):
            return kind[2][0] * 2
        return kind[2][l[3]]
    if kind[0] == "station":
        return 25 * [1, 2, 4, 8][same - 1]
    return dice * 10 if same == 2 else dice * 4

landings = [(0, 7), (1, 9), (2, 4), (3, 6), (4, 8), (7, 5), (8, 11)]
for i, dice in landings:
    l = lots[i]
    print(f"{l[0]:<14} owned by {l[2]}, dice {dice:>2}: rent {rent(lots, l, dice)}")
