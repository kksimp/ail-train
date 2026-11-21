def fits(ls, slot, i, p):
    used = 0
    for j in range(i):
        if slot[j] == p:
            used += 1
            if ls[j][1] == ls[i][1] or ls[j][2] == ls[i][2]:
                return False
    return used < 2

def solve(ls, slot, i, tries):
    if i == len(ls):
        return True
    for p in range(4):
        tries[0] += 1
        if fits(ls, slot, i, p):
            slot[i] = p
            if solve(ls, slot, i + 1, tries):
                return True
            slot[i] = -1
    return False

ls = [("math", "Ng", "7A"), ("math", "Ng", "7B"), ("art", "Ruiz", "7A"), ("bio", "Okafor", "7B"), ("chem", "Okafor", "7A"), ("pe", "Ruiz", "7B"), ("math", "Ng", "7C"), ("art", "Ruiz", "7C")]
slot = [-1] * len(ls)
tries = [0]
if solve(ls, slot, 0, tries):
    for p in range(4):
        cells = [f"{ls[i][2]} {ls[i][0]} ({ls[i][1]})" for i in range(len(ls)) if slot[i] == p]
        print(f"period {p + 1}: {' | '.join(cells)}")
else:
    print("no timetable")
print(f"{tries[0]} placements tried")
