def best_reply(pay, counts):
    best, best_v = 0, -1000000000
    for m in range(3):
        v = sum(pay[m][o] * counts[o] for o in range(3))
        if v > best_v:
            best, best_v = m, v
    return best
pay = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
sa, sb = [1, 0, 0], [0, 1, 0]
rnd = 1
for stop in [10, 100, 1000, 10000, 100000]:
    while rnd < stop:
        a = best_reply(pay, sb)
        b = best_reply(pay, sa)
        sa[a] += 1
        sb[b] += 1
        rnd += 1
    print(f"after {rnd:>6} rounds player A played rock {sa[0]:>5}, paper {sa[1]:>5}, scissors {sa[2]:>5}")
print("the counts even out towards a third each, the mixed equilibrium")
