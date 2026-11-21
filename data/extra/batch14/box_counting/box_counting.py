import math
rows = []
row = [1]
for r in range(256):
    cells = [False] * 256
    for c in range(len(row)):
        cells[c] = row[c] == 1
    rows.append(cells)
    row = [1] + [(row[i - 1] + row[i]) % 2 for i in range(1, len(row))] + [1]
def boxes(pic, s):
    count = 0
    for by in range(256 // s):
        for bx in range(256 // s):
            hit = False
            for y in range(by * s, by * s + s):
                for x in range(bx * s, bx * s + s):
                    if pic[y][x]:
                        hit = True
            if hit:
                count += 1
    return count
line = [[x == y for x in range(256)] for y in range(256)]
square = [[True] * 256 for y in range(256)]
print("box side   Pascal mod 2      line    square")
for s in [64, 16, 4, 1]:
    scale = math.log(float(256 // s))
    a, b, c = boxes(rows, s), boxes(line, s), boxes(square, s)
    da, db, dc = math.log(float(a)) / scale, math.log(float(b)) / scale, math.log(float(c)) / scale
    print(f"{s:>8} {a:>6} ({da:.3f}) {b:>4} ({db:.1f}) {c:>5} ({dc:.1f})")
print(f"exact dimension of the triangle: log 3 / log 2 = {math.log(3.0) / math.log(2.0):.3f}")
