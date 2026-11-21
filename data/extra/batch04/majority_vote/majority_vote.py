def maj(v):
    c, n = "", 0
    for x in v:
        if n == 0: c, n = x, 1
        elif x == c: n += 1
        else: n -= 1
    return c if v.count(c) * 2 > len(v) else None
for p in [["red", "blue", "red", "red", "green", "red", "blue"], ["a", "b", "a", "b", "c"], ["yes"], ["x", "y", "x", "y", "x", "y"], ["oak", "oak", "elm", "oak", "elm", "oak", "elm"]]:
    print(f"{len(p)} votes: majority {maj(p) or 'none'}")
