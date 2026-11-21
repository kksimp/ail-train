deps = [(2, 2, 2), (7, 3, 3), (4, 8, 1)]
cov = set(); order = []; per = []
for cx, cy, r in deps:
    a = 0
    for x in range(10):
        for y in range(10):
            if abs(x - cx) + abs(y - cy) <= r and (x, y) not in cov: cov.add((x, y)); a += 1
    per.append(a)
print(f"new cells per depot: {per}")
print(f"{len(cov)} of 100 cells covered")
homes = [(1, 1), (5, 5), (9, 3), (4, 9), (0, 9), (6, 1)]
print("addresses outside coverage: " + " ".join(f"{h[0]},{h[1]}" for h in homes if h not in cov))
for y in range(10): print("".join("#" if (x, y) in cov else "." for x in range(10)))
