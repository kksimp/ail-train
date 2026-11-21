schools = [("A", 1, 2), ("B", 2, 9), ("C", 6, 4), ("D", 6, 10)]
rows = 8
cols = 12
counts = [0, 0, 0, 0]
farthest = [0, 0, 0, 0]
ties = 0
for r in range(rows):
    line = []
    for c in range(cols):
        best = -1
        best_d = 1000
        tied = False
        for i, (name, sr, sc) in enumerate(schools):
            d = abs(r - sr) + abs(c - sc)
            if d < best_d:
                best = i
                best_d = d
                tied = False
            elif d == best_d:
                tied = True
        if tied:
            ties += 1
            line.append("*")
        else:
            counts[best] += 1
            farthest[best] = max(farthest[best], best_d)
            line.append(schools[best][0].lower())
    print("".join(line))
for i, s in enumerate(schools):
    print(f"school {s[0]}: {counts[i]} cells, farthest {farthest[i]} blocks")
print(f"{ties} cells are equally far from two schools")
