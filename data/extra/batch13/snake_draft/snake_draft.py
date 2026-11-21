def order(managers, rounds):
    out = []
    for r in range(rounds):
        for i in range(managers):
            out.append(i if r % 2 == 0 else managers - 1 - i)
    return out

managers = ["Ash", "Bly", "Cruz", "Dev"]
pool = [("Ruiz", "RB", 1), ("Wade", "WR", 2), ("Rhee", "RB", 3), ("Webb", "WR", 4), ("Quan", "QB", 5), ("Rios", "RB", 6), ("Wong", "WR", 7), ("Quill", "QB", 8), ("Reed", "RB", 9), ("Ward", "WR", 10), ("Quade", "QB", 11), ("Qiu", "QB", 12)]
rosters = [[] for m in managers]
for n, m in enumerate(order(4, 3)):
    chosen = -1
    for i, p in enumerate(pool):
        if chosen < 0 and not any(q[1] == p[1] for q in rosters[m]):
            chosen = i
    p = pool[chosen]
    pool.pop(chosen)
    rosters[m].append(p)
    print(f"pick {n + 1:>2}: {managers[m]:<4} takes {p[0]} ({p[1]}, ranked {p[2]})")
