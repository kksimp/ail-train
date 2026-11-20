prices = [12, 30, 18, 25, 7, 30, 5, 20]
def first_pair(ps, v):
    seen = {}
    for i, p in enumerate(ps):
        if v - p in seen:
            return seen[v - p], i
        seen.setdefault(p, i)
    return None
def all_pairs(ps, v):
    c, n = {}, 0
    for p in ps:
        n += c.get(v - p, 0)
        c[p] = c.get(p, 0) + 1
    return n
for v in [37, 60, 50, 100, 25]:
    pr = first_pair(prices, v)
    if pr:
        a, b = pr
        print(f"{v}: items {a + 1} and {b + 1} ({prices[a]} + {prices[b]}), {all_pairs(prices, v)} pairs in all")
    else:
        print(f"{v}: no pair")
