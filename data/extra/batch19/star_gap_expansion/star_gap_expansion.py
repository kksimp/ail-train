def spread(stars, er, ec, f):
    placed = [[s[0] + (f - 1) * sum(1 for r in er if r < s[0]), s[1] + (f - 1) * sum(1 for c in ec if c < s[1])] for s in stars]
    total = 0
    for i in range(len(placed)):
        for j in range(i + 1, len(placed)):
            total += abs(placed[i][0] - placed[j][0]) + abs(placed[i][1] - placed[j][1])
    return total

image = ["..#.....", "........", "#.....#.", "........", "...#....", ".......#", "........", ".#..#..."]
stars = [[r, c] for r, row in enumerate(image) for c, ch in enumerate(row) if ch == '#']
er = [r for r in range(len(image)) if '#' not in image[r]]
ec = [c for c in range(len(image[0])) if all(s[1] != c for s in stars)]
print(f"{len(stars)} stars, empty rows {er}, empty cols {ec}")
print(f"part 1: {spread(stars, er, ec, 2)}")
print(f"part 2: {spread(stars, er, ec, 100)}")
print(f"unexpanded: {spread(stars, er, ec, 1)}")
