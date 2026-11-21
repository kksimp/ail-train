bayer = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
rows = 8
cols = 32
on = 0
level_sum = 0
for y in range(rows):
    line = []
    for x in range(cols):
        v = min(x * 255 // (cols - 1) + y * 12, 255)
        level_sum += v
        if v > bayer[y % 4][x % 4] * 16 + 8:
            line.append("#")
            on += 1
        else:
            line.append(".")
    print("".join(line))
total = rows * cols
ink = on * 100 // total
mean = level_sum * 100 // (total * 255)
print(f"{on} of {total} dots on ({ink}%), mean brightness {mean}%")
