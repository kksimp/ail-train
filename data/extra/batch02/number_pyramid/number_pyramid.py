def mp(rows):
    best = rows[-1]
    for r in range(len(rows) - 2, -1, -1):
        best = [rows[r][i] + max(best[i], best[i + 1]) for i in range(len(rows[r]))]
    return best[0]
p = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
print(f"rows: {len(p)}, best: {mp(p)}")
b = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34]]
print(f"rows: {len(b)}, best: {mp(b)}")
print(42)
