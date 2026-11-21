def value(w, L, D): 
    v = 0
    for c in w: v = v * 10 + D[L.index(c)]
    return v
def search(k, L, leads, words, D, used, first):
    if k == len(L):
        a = value(words[0], L, D); b = value(words[1], L, D); t = value(words[2], L, D)
        if a + b == t:
            if not first: first.append(f"{a} + {b} = {t}")
            return 1
        return 0
    cnt = 0
    for d in range(10):
        if not used[d] and not (d == 0 and L[k] in leads):
            used[d] = True; D[k] = d; cnt += search(k + 1, L, leads, words, D, used, first); used[d] = False
    return cnt
for pz in [["TO", "GO", "OUT"], ["TWO", "TWO", "FOUR"], ["AB", "BA", "CC"], ["ODD", "ODD", "EVEN"]]:
    L = []
    for w in pz:
        for c in w:
            if c not in L: L.append(c)
    leads = set(w[0] for w in pz); first = []
    n = search(0, L, leads, pz, [0] * len(L), [False] * 10, first)
    lab = f"{pz[0]} + {pz[1]} = {pz[2]}"
    print(f"{lab}: no solution" if n == 0 else f"{lab}: {n} found, first {first[0]}")
