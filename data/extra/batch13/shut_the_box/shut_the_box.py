def pick(tiles, target, start):
    if target == 0:
        return []
    for i in range(start, len(tiles)):
        t = tiles[i]
        if t <= target:
            rest = pick(tiles, target - t, i + 1)
            if rest is not None:
                return [t] + rest
    return None

seed = 77
for game in range(1, 3):
    open_ = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    rolls = 0
    log = []
    while len(open_) > 0:
        seed = (seed * 1103515245 + 12345) % 2147483648
        a = (seed // 65536) % 6 + 1
        seed = (seed * 1103515245 + 12345) % 2147483648
        b = (seed // 65536) % 6 + 1
        rolls += 1
        shut = pick(open_, a + b, 0)
        if shut is None:
            log.append(f"{a + b}: stuck")
            break
        open_ = [t for t in open_ if t not in shut]
        joined = "+".join(str(x) for x in shut)
        log.append(f"{a + b}: {joined}")
    print(f"game {game}: {', '.join(log)}")
    if not open_:
        print(f"game {game}: box shut in {rolls} rolls")
    else:
        print(f"game {game}: score {sum(open_)} with {len(open_)} tiles open")
