def row_line(p, smudges):
    for r in range(1, len(p)):
        diff = 0; k = 0
        while r - 1 - k >= 0 and r + k < len(p):
            a = p[r - 1 - k]; b = p[r + k]
            diff += sum(1 for i in range(len(a)) if a[i] != b[i])
            k += 1
        if diff == smudges:
            return r
    return 0

def transpose(p):
    return ["".join(row[c] for row in p) for c in range(len(p[0]))]

def score(p, smudges):
    return 100 * row_line(p, smudges) + row_line(transpose(p), smudges)

patterns = [[".......", "#.##...", "...##..", "..#....", "......."], ["......", "#..#..", "....#.", "####.#", "######"], [".####..#", "..##..##", ".......#", "#######.", "..##...."]]
p1 = p2 = 0
for i, p in enumerate(patterns):
    a = score(p, 0); b = score(p, 1)
    print(f"pattern {i + 1}: clean {a}, smudged {b}")
    p1 += a; p2 += b
print(f"part 1: {p1}")
print(f"part 2: {p2}")
