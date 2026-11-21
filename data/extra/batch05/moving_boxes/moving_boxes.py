I = sorted([("books", 12), ("plates", 9), ("lamp", 4), ("pans", 7), ("shoes", 5), ("toys", 6), ("files", 11), ("rug", 8), ("vase", 3)], key=lambda i: (-i[1], i[0])); B = []; L = []
for it in I:
    for b in range(len(B)):
        if L[b] + it[1] <= 20: B[b].append(it); L[b] += it[1]; break
    else: B.append([it]); L.append(it[1])
for b in range(len(B)): print(f"box {b + 1} ({L[b]} kg): {', '.join(i[0] for i in B[b])}")
