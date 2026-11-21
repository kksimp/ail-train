def seen(line):
    tallest = 0
    count = 0
    for h in line:
        if h > tallest:
            tallest = h
            count += 1
    return count

grid = [[2, 1, 4, 3], [3, 4, 1, 2], [4, 2, 3, 1], [1, 3, 2, 4]]
top = [3, 2, 1, 2]
bottom = [2, 2, 3, 1]
left = [2, 2, 1, 3]
right = [2, 2, 3, 2]
wrong = 0
for i in range(4):
    col = [row[i] for row in grid]
    checks = [("top", i, top[i], seen(col)), ("bottom", i, bottom[i], seen(col[::-1])), ("left", i, left[i], seen(grid[i])), ("right", i, right[i], seen(grid[i][::-1]))]
    for side, idx, want, got in checks:
        if want != got:
            wrong += 1
            print(f"{side} clue {idx + 1}: wants {want}, sees {got}")
for row in grid:
    print(" ".join(str(x) for x in row))
print(f"{16 - wrong} of 16 clues satisfied")
