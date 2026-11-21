def combos(total, cells, low):
    if cells == 0:
        return [""] if total == 0 else []
    out = []
    for d in range(low, 10):
        if d > total:
            break
        for rest in combos(total - d, cells - 1, d + 1):
            out.append(f"{d}{rest}")
    return out

def digits(options):
    s = set()
    for o in options:
        for c in o:
            s.add(c)
    return s

clues = [[3, 2], [16, 2], [17, 2], [10, 3], [23, 3], [7, 3], [30, 4], [12, 4]]
for clue in clues:
    found = combos(clue[0], clue[1], 1)
    shown = " ".join(found)
    tag = " (unique)" if len(found) == 1 else ""
    print(f"{clue[0]:>2} in {clue[1]}: {shown}{tag}")
across = digits(combos(10, 3, 1))
down = digits(combos(16, 2, 1))
both = sorted(across & down)
print(f"a cell in 10/3 across and 16/2 down can hold {''.join(both)}")
