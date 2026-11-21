def cp(s):
    D = {chr(97 + i): i for i in range(26)}; w = ""; o = []
    for c in s:
        if w + c in D: w = w + c
        else: o.append(D[w]); D[w + c] = len(D); w = c
    if w: o.append(D[w])
    return o
def ex(C):
    T = [chr(97 + i) for i in range(26)]; w = T[C[0]]; o = w
    for k in C[1:]:
        e = T[k] if k < len(T) else w + w[0]; o += e; T.append(w + e[0]); w = e
    return o
for s in ["tobeornottobeortobeornot", "abababababababab", "banana", "aaaaaaaaaaaaaaaaaaaa"]:
    c = cp(s); print(f"{s}: {' '.join(map(str, c))}"); print(f"  {len(s)} letters -> {len(c)} codes, back: {'true' if ex(c) == s else 'false'}")
