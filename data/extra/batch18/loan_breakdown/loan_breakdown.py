loans = [("Dune", "sf", 14), ("Emma", "classic", 7), ("Hyperion", "sf", 28), ("Rebecca", "classic", 21), ("Gone Girl", "crime", 5), ("Solaris", "sf", 7)]
def count_by(xs, key):
    out = {}
    for x in xs: out[key(x)] = out.get(key(x), 0) + 1
    return out
def band(l): return "week" if l[2] <= 7 else ("fortnight+" if l[2] <= 21 else "long")
def show(t, c): print(f"{t}: {' '.join(f'{k}={v}' for k, v in c.items())}")
show("by genre", count_by(loans, lambda l: l[1]))
show("by length", count_by(loans, band))
show("by initial", count_by(["mia", "max", "ola", "mo", "ike", "oto"], lambda s: s[0]))
l = max(loans, key=lambda l: l[2])
print(f"longest loan: {l[0]} ({l[2]} days)")
