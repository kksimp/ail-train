bal = {}
def ap(w, a):
    p = {"wash": 2, "dry": 1}.get(a, 0)
    if a == "buy": bal[w] = bal.get(w, 0) + 5; return None
    h = bal.get(w, 0)
    if h < p: return f"{w} cannot {a} with {h}"
    bal[w] = h - p
for w, a in [("ana", "buy"), ("ana", "wash"), ("ben", "dry"), ("ana", "wash"), ("ana", "dry"), ("ben", "buy"), ("ana", "wash"), ("ben", "wash")]:
    r = ap(w, a)
    if r: print(f"refused: {r}")
for w in sorted(bal): print(f"{w}: {bal[w]} tokens")
