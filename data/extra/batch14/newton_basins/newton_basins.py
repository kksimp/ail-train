roots = [[1.0, 0.0], [-0.5, 0.8660254037844386], [-0.5, -0.8660254037844386]]
marks = ["A", "B", "C"]
counts = [0, 0, 0]
for j in range(11):
    row = []
    for i in range(26):
        x = (2 * i - 25) / 12.0
        y = (11 - 2 * j) / 7.0
        for step in range(30):
            x2 = x * x - y * y
            y2 = 2.0 * x * y
            fre = x2 * x - y2 * y - 1.0
            fim = x2 * y + y2 * x
            dre = 3.0 * x2
            dim = 3.0 * y2
            d = dre * dre + dim * dim
            x -= (fre * dre + fim * dim) / d
            y -= (fim * dre - fre * dim) / d
        best, best_d = 0, 1000000.0
        for r in range(3):
            dx = x - roots[r][0]
            dy = y - roots[r][1]
            dist = dx * dx + dy * dy
            if dist < best_d:
                best, best_d = r, dist
        counts[best] += 1
        row.append(marks[best])
    print("".join(row))
print(f"points reaching 1: {counts[0]}, reaching -1/2 + 0.866i: {counts[1]}, reaching -1/2 - 0.866i: {counts[2]}")
