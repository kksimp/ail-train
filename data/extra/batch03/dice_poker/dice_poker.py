def hand(d):
    c = sorted({x: d.count(x) for x in d}.values(), reverse=True); s = sorted(d)
    st = len(c) == 5 and s[4] - s[0] == 4
    if c[0] == 5: return 7, "five of a kind"
    if c[0] == 4: return 6, "four of a kind"
    if c[0] == 3 and c[1] == 2: return 5, "full house"
    if st: return 4, "straight"
    if c[0] == 3: return 3, "three of a kind"
    if c[0] == 2 and c[1] == 2: return 2, "two pair"
    if c[0] == 2: return 1, "pair"
    return 0, "nothing"
t = [("Ana", [3, 3, 5, 3, 5]), ("Bo", [1, 2, 3, 4, 5]), ("Cy", [6, 6, 6, 6, 2]), ("Di", [2, 2, 4, 4, 1]), ("Ed", [1, 3, 4, 5, 6])]
for n, d in t: print(f"{n:<4} {d} {hand(d)[1]}")
print(f"winner: {max(t, key=lambda p: hand(p[1])[0])[0]}")
