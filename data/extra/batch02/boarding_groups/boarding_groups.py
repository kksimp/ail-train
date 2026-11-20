ppl = [("Abe", 3, False), ("Bia", 30, False), ("Cem", 14, True), ("Dag", 22, False), ("Eve", 38, False), ("Fox", 9, False), ("Gil", 25, False)]
def g(p):
    if p[2]: return 0
    return 1 if 25 <= p[1] <= 40 else 2 if 13 <= p[1] <= 24 else 3
gs = {}
for p in ppl: gs.setdefault(g(p), []).append(p)
for k in sorted(gs):
    print(f"group {k}: " + " ".join(f"{p[0]}({p[1]})" for p in sorted(gs[k], key=lambda p: -p[1])))
print("boarding order: " + " ".join(p[0] for p in sorted(ppl, key=lambda p: (g(p), -p[1]))))
