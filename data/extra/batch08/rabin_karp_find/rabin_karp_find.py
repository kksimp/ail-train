def search(text, pat):
    t = [ord(c) for c in text]; p = [ord(c) for c in pat]; m = len(p); high = 1
    for i in range(m - 1): high = (high * 256) % 13
    hp = ht = 0
    for i in range(m): hp = (hp * 256 + p[i]) % 13; ht = (ht * 256 + t[i]) % 13
    hits = []; fa = 0
    for s in range(len(t) - m + 1):
        if hp == ht:
            if t[s:s + m] == p: hits.append(s)
            else: fa += 1
        if s + m < len(t): ht = ((ht - (t[s] * high) % 13 + 13) * 256 + t[s + m]) % 13
    print(f"'{pat}' at [{', '.join(str(h) for h in hits)}], {fa} hash collisions")
for pat in ["at", "the", "sat", "dog", "hat t"]: search("the cat sat on the mat with the hat that sat", pat)
