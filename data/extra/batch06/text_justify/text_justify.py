def js(W, w):
    L = []; c = []; u = 0
    for x in W:
        if c and u + 1 + len(x) > w: L.append(c); c = []; u = 0
        u += len(x) if not c else 1 + len(x); c.append(x)
    o = []
    for l in L:
        g = len(l) - 1
        if g == 0: o.append(l[0]); continue
        s = w - sum(len(x) for x in l); t = l[0]
        for k in range(g): t += " " * (s // g + (1 if k < s % g else 0)) + l[k + 1]
        o.append(t)
    o.append(" ".join(c)); return o
for l in js("This is an example of text justification where every line but the last is padded to the same width.".split(" "), 24): print(f"|{l:<24}|")
