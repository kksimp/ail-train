def plan(supply, demand, cost, cheapest):
    s, d = list(supply), list(demand)
    ship = [[0] * len(d) for _ in s]
    i = j = 0
    while True:
        if cheapest:
            best = -1
            for a in range(len(s)):
                for b in range(len(d)):
                    if s[a] > 0 and d[b] > 0 and (best < 0 or cost[a][b] < cost[best // 10][best % 10]):
                        best = a * 10 + b
            if best < 0:
                break
            i, j = best // 10, best % 10
        elif i >= len(s) or j >= len(d):
            break
        amount = min(s[i], d[j])
        ship[i][j] += amount
        s[i] -= amount
        d[j] -= amount
        if not cheapest:
            if s[i] == 0:
                i += 1
            else:
                j += 1
    return ship
def total(ship, cost):
    return sum(ship[i][j] * cost[i][j] for i in range(len(ship)) for j in range(len(ship[i])))
supply = [20, 30, 25]
demand = [10, 25, 15, 25]
cost = [[8, 6, 10, 9], [9, 12, 13, 7], [14, 9, 16, 5]]
for cheapest in [False, True]:
    ship = plan(supply, demand, cost, cheapest)
    print(("least cost" if cheapest else "north-west corner") + ":")
    for row in ship:
        print("".join(f"{v:>4}" for v in row))
    print(f"    total cost {total(ship, cost)}")
