def plan(prices):
    n = len(prices)
    cost = [prices[0]]
    frm = [[-1, -1, -1]]
    for i in range(1, n):
        row = []
        via = []
        for c in range(3):
            best = -1
            for p in range(3):
                if p != c and (best < 0 or cost[i - 1][p] < cost[i - 1][best]):
                    best = p
            row.append(prices[i][c] + cost[i - 1][best])
            via.append(best)
        cost.append(row)
        frm.append(via)
    c = 0
    for k in range(1, 3):
        if cost[n - 1][k] < cost[n - 1][c]:
            c = k
    colours = []
    i = n - 1
    while i >= 0:
        colours.append(c)
        c = frm[i][c]
        i -= 1
    colours.reverse()
    colours.append(cost[n - 1][colours[n - 1]])
    return colours

prices = [[17, 2, 17], [16, 16, 5], [14, 3, 19], [6, 12, 8], [11, 9, 4], [3, 15, 10], [8, 7, 13]]
result = plan(prices)
names = ["Red", "Green", "Blue"]
for i in range(len(prices)):
    p = names[result[i]]
    print(f"house {i + 1}: {p:<5} costs {prices[i][result[i]]}")
print(f"total {result[len(prices)]}")
