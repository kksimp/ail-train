def call(n): return ["love", "15", "30", "40"][min(n, 3)]
def point(g, w):
    k = g[0]
    if k == "P":
        a, b = g[1], g[2]
        a += w == "A"; b += w == "B"
        if a == 4 and b <= 2: return ("W", "A")
        if b == 4 and a <= 2: return ("W", "B")
        if a == 3 and b == 3: return ("D",)
        return ("P", a, b)
    if k == "D": return ("Adv", w)
    if k == "Adv": return ("W", w) if g[1] == w else ("D",)
    return g
def show(g):
    k = g[0]
    if k == "P": return f"{call(g[1])} all" if g[1] == g[2] else f"{call(g[1])}-{call(g[2])}"
    if k == "D": return "deuce"
    if k == "Adv": return f"advantage {g[1]}"
    return f"game {g[1]}"
for r in ["AAAA", "ABABABBB", "ABABABABAA", "BBAB"]:
    g = ("P", 0, 0); cs = []
    for c in r:
        g = point(g, c); cs.append(show(g))
    print(f"{r}: {', '.join(cs)}")
