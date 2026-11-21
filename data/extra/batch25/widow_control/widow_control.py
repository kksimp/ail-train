page = 10
paras = [6, 3, 2, 4, 5, 3, 8, 4]
used = 0
pg = 1
fixes = 0
for i, n in enumerate(paras):
    left = n
    pieces = []
    while left > 0:
        room = page - used
        if left <= room:
            pieces.append(f"p{pg}:{left}")
            used += left
            left = 0
        else:
            take = room
            if take == 1 or (left == 2 and take > 0):
                take = 0
                fixes += 1
            elif left - take == 1:
                take -= 1
                fixes += 1
                if take == 1:
                    take = 0
            if take > 0:
                pieces.append(f"p{pg}:{take}")
            left -= take
            pg += 1
            used = 0
        if used == page:
            pg += 1
            used = 0
    print(f"paragraph {i + 1} ({n} lines): {' '.join(pieces)}")
last = pg - 1 if used == 0 else pg
print(f"{last} pages, {fixes} widow or orphan fixes")
