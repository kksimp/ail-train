results = ["Lions 2-1 Bears", "Hawks 0-0 Lions", "Bears 3-3 Wolves", "Wolves 1-2 Hawks", "Lions 4-0 Wolves", "Bears 1-0 Hawks"]
t = {}
def rec(team, gf, ga):
    r = t.setdefault(team, {"p": 0, "pts": 0, "f": 0, "a": 0})
    r["p"] += 1; r["f"] += gf; r["a"] += ga
    r["pts"] += 3 if gf > ga else 1 if gf == ga else 0
for line in results:
    w = line.split()
    a, b = map(int, w[1].split("-"))
    rec(w[0], a, b); rec(w[2], b, a)
rows = sorted(t.items(), key=lambda kv: (-kv[1]["pts"], -(kv[1]["f"] - kv[1]["a"]), -kv[1]["f"], kv[0]))
print(f"{'team':<8}{'P':>2}{'GD':>4}{'Pts':>5}")
for name, r in rows:
    d = r["f"] - r["a"]
    gd = f"+{d}" if d > 0 else f"{d}"
    print(f"{name:<8}{r['p']:>2}{gd:>4}{r['pts']:>5}")
