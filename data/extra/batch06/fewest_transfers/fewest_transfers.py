def bs(L, a, b):
    if a == b: return 0
    U = set(); R = {a}; c = 0
    while True:
        c += 1; g = False; N = set(R)
        for n, st in L:
            if n in U: continue
            if any(s in R for s in st): U.add(n); g = True; N |= set(st)
        if b in N: return c
        if not g: return -1
        R = N
L = [("1", ["Ash", "Bay", "Cove", "Dell"]), ("2", ["Cove", "Elm", "Fen"]), ("3", ["Fen", "Glen", "Hill"]), ("4", ["Bay", "Glen"]), ("5", ["Isle", "Jetty"])]
for a, b in [("Ash", "Dell"), ("Ash", "Elm"), ("Ash", "Hill"), ("Dell", "Fen"), ("Ash", "Jetty"), ("Elm", "Elm")]:
    n = bs(L, a, b); print(f"{a} -> {b}: {'no route' if n < 0 else 'already there' if n == 0 else str(n) + ' bus(es)'}")
