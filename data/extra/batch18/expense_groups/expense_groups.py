sp = [("Ana", "food", 4250), ("Ben", "fuel", 6100), ("Ana", "rooms", 18000), ("Cai", "food", 3875), ("Ben", "food", 2290), ("Cai", "fuel", 5400)]
def money(c): return f"{c // 100}.{c % 100:02}"
g = {}
for e in sp: g.setdefault(e[1], []).append(e)
for cat, it in g.items():
    s = sum(e[2] for e in it); top = max(it, key=lambda e: e[2])[0]
    print(f"{cat:<6} {len(it)} items {money(s):>7}, most paid by {top}")
w = sum(e[2] for e in sp)
print(f"total {money(w)}, fair share {money(w // 3)} each")
