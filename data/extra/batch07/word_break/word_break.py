def sw(s, D):
    n = len(s); b = [-1] * (n + 1); f = [0] * (n + 1); b[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if b[j] < 0: continue
            if s[j:i] in D and (b[i] < 0 or b[j] + 1 < b[i]): b[i] = b[j] + 1; f[i] = j
    if b[n] < 0: return None
    w = []; a = n
    while a > 0: w.append(s[f[a]:a]); a = f[a]
    return w[::-1]
D = {"apple", "pen", "applepen", "pine", "pineapple", "cats", "cat", "and", "sand", "dog", "sea", "seashell", "shell", "sells"}
for s in ["pineapplepenapple", "catsanddog", "seashellsells", "catsandog", "applepenapple"]:
    w = sw(s, D); print(f"{s}: {' '.join(w)}" if w else f"{s}: no split")
