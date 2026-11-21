N = ["farmer", "wolf", "goat", "cabbage"]
def sf(s): return not ((s[1] == s[2] and s[0] != s[2]) or (s[2] == s[3] and s[0] != s[2]))
k = lambda s: "".join(map(str, s)); st = [0, 0, 0, 0]; pv = {k(st): ("", "")}; q = [st]; h = 0
while h < len(q):
    c = q[h]; h += 1
    if k(c) == "1111": break
    for it in range(4):
        if it > 0 and c[it] != c[0]: continue
        n = c[:]; n[0] = 1 - c[0]
        if it > 0: n[it] = 1 - c[it]
        if sf(n) and k(n) not in pv: pv[k(n)] = (k(c), "alone" if it == 0 else f"with the {N[it]}"); q.append(n)
S = []; a = "1111"
while a != k(st): p = pv[a]; S.append(p[1]); a = p[0]
S.reverse()
for i, s in enumerate(S): print(f"{i + 1}. farmer goes {'across' if i % 2 == 0 else 'back'} {s}")
