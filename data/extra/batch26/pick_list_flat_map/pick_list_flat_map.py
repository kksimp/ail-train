orders = [(501, [("A-12", 2), ("C-03", 1)]), (502, [("B-07", 3)]), (503, [("A-12", 1), ("B-01", 1), ("C-03", 2)])]
picks = [f"{s}@{oid}" for oid, ls in orders for s, q in ls for _ in range(q)]
print(f"{len(picks)} picks from {len(orders)} orders")
g = {}
for p in picks:
    g.setdefault(p[0], []).append(p)
for a in sorted(g):
    print(f"aisle {a} ({len(g[a])}): {' '.join(g[a])}")
print(f"distinct SKUs: {', '.join(sorted({p.split('@')[0] for p in picks}))}")
