votes = [("Harbour", 4), ("Quiet Hill", 5), ("Harbour", 3), ("Neon Rain", 2), ("Quiet Hill", 4), ("Harbour", 5), ("Neon Rain", 3), ("Quiet Hill", 5), ("Paper Moon", 5)]
g = {}
for f, s in votes:
    g.setdefault(f, []).append(s)
for f, ss in g.items():
    print(f"{f:<11} {sum(ss) / len(ss):.1f} from {len(ss)} votes")
r = sorted([f for f in g if len(g[f]) >= 3], key=lambda f: -sum(g[f]) / len(g[f]))
for i, f in enumerate(r):
    print(f"#{i + 1} {f}")
