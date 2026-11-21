def hits(hill, right, down):
    r = c = n = 0
    while r < len(hill):
        if hill[r][c % len(hill[r])] == '#': n += 1
        r += down; c += right
    return n

hill = ["..#....#...", "#...#......", ".#.....#..#", "...#.#....#", ".#...##..#.", "..#.#......", ".#....#.#.#", "#.......#..", "...##....#.", "#..#...#..#"]
print(f"part 1: right 3, down 1 hits {hits(hill, 3, 1)} trees")
product = 1
for s in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    n = hits(hill, s[0], s[1])
    print(f"  right {s[0]}, down {s[1]}: {n}")
    product *= n
print(f"part 2: product {product}")
