parents = {"bea": "ann", "cal": "ann", "dov": "bea", "eli": "dov", "fay": "cal", "gus": "eli"}
def depth(u):
    return 0 if u not in parents else 1 + depth(parents[u])
def chain(u):
    return u if u not in parents else f"{u} <- {chain(parents[u])}"
members = ["ann", "bea", "cal", "dov", "eli", "fay", "gus"]
for m in members:
    print(f"{m}: depth {depth(m)}")
best = members[0]
for m in members:
    if depth(m) > depth(best): best = m
print(f"longest chain: {chain(best)}")
d = {}
for c, p in parents.items():
    d[p] = d.get(p, 0) + 1
for p, n in d.items():
    print(f"{p} referred {n}")
print("everyone traces back to ann")
