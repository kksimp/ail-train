W = ["cat", "cot", "cut", "cart", "coat", "colt", "dolt", "melt", "mint", "most", "cast", "cost"]
def ft(p, w): return len(p) == len(w) and all(a == "." or a == b for a, b in zip(p, w))
for p in ["c.t", "co.t", "..lt", "c.st", "m..t", "x.."]: h = [w for w in W if ft(p, w)]; print(f"{p}: {' '.join(h) if h else '-'}")
