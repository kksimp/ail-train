def transform(w):
    s = w + "$"
    n = len(s)
    rots = sorted(s[i:] + s[:i] for i in range(n))
    return "".join(r[n - 1] for r in rots)

def invert(b):
    last = list(b)
    counts = {}
    occ = []
    for c in last:
        occ.append(counts.get(c, 0))
        counts[c] = counts.get(c, 0) + 1
    start = {}
    total = 0
    for c in sorted(counts):
        start[c] = total
        total += counts[c]
    out = []
    row = 0
    for step in range(len(last) - 1):
        c = last[row]
        out.append(c)
        row = start[c] + occ[row]
    out.reverse()
    return "".join(out)

def runs(s):
    n = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            n += 1
    return n

for w in ["banana", "mississippi", "abracadabra", "bookkeeper", "tobeornottobe"]:
    b = transform(w)
    back = invert(b)
    ok = "ok" if back == w else "MISMATCH"
    print(f"{w:<14} -> {b:<15} runs {runs(w):>2} -> {runs(b):>2}, back {ok}")
