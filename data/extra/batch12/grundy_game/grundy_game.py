def grundy(limit, takes):
    g = []
    for n in range(limit + 1):
        reach = set()
        for t in takes:
            if t <= n:
                reach.add(g[n - t])
        m = 0
        while m in reach:
            m += 1
        g.append(m)
    return g

takes = [1, 3, 4]
g = grundy(20, takes)
print(f"grundy values 0..20: {g}")
losing = [n for n in range(21) if g[n] == 0]
print(f"losing pile sizes: {losing}")
for piles in [[5, 7], [2, 9, 13], [6, 6], [4, 8, 10]]:
    x = 0
    for p in piles:
        x = x ^ g[p]
    if x == 0:
        print(f"{piles}: xor 0, the player to move loses")
    else:
        move = "none"
        for i, p in enumerate(piles):
            for t in takes:
                if t <= p and move == "none" and ((x ^ g[p]) ^ g[p - t]) == 0:
                    move = f"take {t} from pile {i + 1}"
        print(f"{piles}: xor {x}, win by {move}")
