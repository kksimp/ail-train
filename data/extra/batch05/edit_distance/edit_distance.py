def d(a, b):
    p = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        c = [i]
        for j in range(1, len(b) + 1): c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (a[i - 1] != b[j - 1])))
        p = c
    return p[len(b)]
for a, b in [("kitten", "sitting"), ("flaw", "lawn"), ("same", "same"), ("", "abc")]: print(f"{a} -> {b}: {d(a, b)}")
W = ["receive", "separate", "definitely", "necessary", "occasion"]
for t in ["recieve", "seperate", "definately", "neccesary", "ocassion"]:
    n = min(W, key=lambda w: (d(t, w), w)); print(f"{t}: {n} ({d(t, n)})")
