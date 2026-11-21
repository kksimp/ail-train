from collections import deque
ws = ["cold", "cord", "card", "ward", "warm", "word", "worm", "corm", "wore", "core", "bold", "bolt"]
def oa(a, b): return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1
def lad(s, g):
    cf = {s: ""}; q = deque([s])
    while q:
        w = q.popleft()
        if w == g:
            p = [w]
            while cf[p[-1]] != "": p.append(cf[p[-1]])
            return p[::-1]
        for n in ws:
            if n not in cf and oa(w, n): cf[n] = w; q.append(n)
    return []
for a, b in [("cold", "warm"), ("cold", "bolt"), ("card", "core"), ("cold", "pear")]:
    p = lad(a, b)
    print(f"{a} -> {b}: no ladder" if not p else f"{a} -> {b}: {' > '.join(p)} ({len(p) - 1} steps)")
