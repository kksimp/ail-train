def leaks(towers, hp):
    pos = []; life = []; leaked = 0
    for tick in range(40):
        if tick % 2 == 0 and tick < 10:
            pos.append(0); life.append(hp)
        for t in towers:
            target = -1
            for e in range(len(pos)):
                if life[e] > 0 and abs(pos[e] - t) <= 2 and (target < 0 or pos[e] > pos[target]): target = e
            if target >= 0: life[target] -= 4
        for e in range(len(pos)):
            if life[e] > 0:
                pos[e] += 1
                if pos[e] == 20:
                    leaked += 1; life[e] = 0
    return leaked
spots = [3, 8, 13, 17, 6, 11, 15, 19]
for hp in [12, 20, 30, 45, 60, 80]:
    need = -1
    for k in range(1, len(spots) + 1):
        if leaks(spots[:k], hp) == 0:
            need = k; break
    if need < 0:
        print(f"health {hp:>2}: even {len(spots)} towers leak {leaks(spots, hp)} enemies")
    else:
        print(f"health {hp:>2}: {need} towers hold the path")
