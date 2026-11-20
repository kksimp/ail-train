rows, cols = 3, 5
g = [[0] * cols for _ in range(rows)]

def book(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols or g[r][c] == 1:
        return "false"
    g[r][c] = 1
    return "true"

for r, c in [(0, 0), (0, 0), (2, 4), (3, 0), (1, 2), (1, 3)]:
    print(book(r, c))
for row in g:
    print("".join("#" if c else "." for c in row))
for r in range(rows):
    print(f"row {r}: {g[r].count(0)} free")
print(sum(map(sum, g)))
print("7 0")
