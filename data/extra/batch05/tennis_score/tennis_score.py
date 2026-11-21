N = ["love", "15", "30", "40"]
def cl(a, b):
    if a >= 3 and b >= 3:
        if a == b: return "deuce"
        if a == b + 1: return "advantage A"
        if b == a + 1: return "advantage B"
    if a >= 4 and a >= b + 2: return "game A"
    if b >= 4 and b >= a + 2: return "game B"
    return f"{N[a]}-{N[b]}"
for g in ["AAAA", "ABABABBB", "AABBABABAA", "BBBAAAB"]:
    a = b = 0; c = []
    for p in g:
        if p == "A": a += 1
        else: b += 1
        c.append(cl(a, b))
    print(f"{g}: {', '.join(c)}")
