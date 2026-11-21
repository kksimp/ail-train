def bitap(text, p, k):
    m = len(p)
    masks = {}
    for i in range(m):
        masks[p[i]] = masks.get(p[i], 0) | (1 << i)
    full = (1 << m) - 1
    hit = 1 << (m - 1)
    r = [0] * (k + 1)
    found = []
    for i, c in enumerate(text):
        b = masks.get(c, 0)
        old = r[0]
        r[0] = (((r[0] << 1) | 1) & b) & full
        for d in range(1, k + 1):
            tmp = r[d]
            r[d] = ((((r[d] << 1) | 1) & b) | ((old << 1) | 1)) & full
            old = tmp
        for d in range(k + 1):
            if (r[d] & hit) != 0:
                found.append([i, d])
                break
    return found

text = "the quick brown fox jumps over the lazy dog"
for pat in ["quack", "jumbs", "lazy", "brawn", "cat"]:
    hits = bitap(text, pat, 1)
    if not hits:
        print(f"{pat:<6} no match within 1 error")
    for h in hits:
        start = h[0] - len(pat) + 1
        piece = text[start:h[0] + 1]
        print(f"{pat:<6} ~ '{piece}' at {start}, {h[1]} error(s)")
