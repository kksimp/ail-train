def lf(ws, w):
    ls = []; cur = ""
    for x in ws:
        if cur == "": cur = x
        elif len(cur) + 1 + len(x) <= w: cur += " " + x
        else: ls.append(cur); cur = x
    if cur: ls.append(cur)
    return ls
W = "a journey of a thousand miles begins with a single step and the step after that".split(" ")
for w in [12, 20, 30, 50]:
    ls = lf(W, w); print(f"width {w}: {len(ls)} lines, longest {max(len(l) for l in ls)}")
for l in lf(W, 20): print(f"|{l:<20}|")
