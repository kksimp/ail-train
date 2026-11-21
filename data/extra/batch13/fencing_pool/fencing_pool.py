names = ["Arno", "Bea", "Cato", "Dina", "Eli"]
pool = [{"name": n, "wins": 0, "bouts": 0, "scored": 0, "received": 0} for n in names]
bouts = [[0, 1, 5, 3], [0, 2, 4, 5], [0, 3, 5, 2], [0, 4, 5, 4], [1, 2, 5, 1], [1, 3, 2, 5], [1, 4, 5, 3], [2, 3, 5, 4], [2, 4, 3, 5], [3, 4, 5, 0]]
for b in bouts:
    pool[b[0]]["bouts"] += 1
    pool[b[1]]["bouts"] += 1
    pool[b[0]]["scored"] += b[2]
    pool[b[0]]["received"] += b[3]
    pool[b[1]]["scored"] += b[3]
    pool[b[1]]["received"] += b[2]
    if b[2] > b[3]:
        pool[b[0]]["wins"] += 1
    else:
        pool[b[1]]["wins"] += 1

def trunc_div(a, b):
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q

ranked = sorted(pool, key=lambda f: (trunc_div(-f["wins"] * 1000, f["bouts"]), -(f["scored"] - f["received"]), -f["scored"]))
print("place fencer  V/M   ind  TS  TR")
for i, f in enumerate(ranked):
    ind = f["scored"] - f["received"]
    ratio = float(f["wins"]) / float(f["bouts"])
    print(f"{i + 1:>5} {f['name']:<6} {ratio:.2f} {ind:>5} {f['scored']:>3} {f['received']:>3}")
