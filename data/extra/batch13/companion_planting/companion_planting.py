def pair_key(a, b):
    return f"{a}+{b}" if a < b else f"{b}+{a}"

bed = [["tomato", "basil", "carrot", "onion"], ["fennel", "tomato", "lettuce", "bean"], ["bean", "onion", "radish", "lettuce"]]
good = {"basil+tomato", "carrot+onion", "lettuce+radish", "bean+carrot", "carrot+tomato", "lettuce+onion", "carrot+radish"}
bad = {"fennel+tomato", "bean+onion", "bean+fennel", "basil+fennel"}
friends = 0
clashes = []
for r in range(len(bed)):
    for c in range(len(bed[r])):
        here = bed[r][c]
        for d in [[0, 1], [1, 0]]:
            nr = r + d[0]
            nc = c + d[1]
            if nr < len(bed) and nc < len(bed[r]):
                k = pair_key(here, bed[nr][nc])
                if k in good:
                    friends += 1
                if k in bad:
                    clashes.append(f"{k} at row {r + 1} col {c + 1}")
for row in bed:
    cells = "".join(f"{x:<8}" for x in row)
    print(cells.rstrip())
print(f"friendly neighbours: {friends}")
for cl in clashes:
    print(f"conflict: {cl}")
