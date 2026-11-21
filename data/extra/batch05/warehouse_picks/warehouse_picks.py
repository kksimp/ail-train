def rk(l): a = ord(l[0]) - 64; s = int(l[1:]); return (a, s) if a % 2 == 1 else (a, -s)
P = ["C4", "A2", "B7", "A9", "C1", "B2", "D5", "A5", "D8"]
print("route: " + " > ".join(sorted(P, key=rk))); a = {}
for p in P: a[p[0]] = a.get(p[0], 0) + 1
for k in sorted(a): print(f"aisle {k}: {a[k]} picks")
