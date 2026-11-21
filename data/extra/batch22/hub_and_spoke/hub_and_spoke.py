def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def trucks(p):
    return (p + 25) // 26

names = ["A", "B", "C", "D", "E"]
at = [[0, 40], [35, 10], [20, -30], [-25, -25], [-40, 15]]
hub = [0, 0]
demand = [[0, 8, 5, 12, 3], [6, 0, 9, 4, 7], [10, 3, 0, 6, 2], [4, 11, 7, 0, 5], [2, 6, 9, 3, 0]]
pallets = 0
direct_trucks = 0
direct_km = 0
for i in range(5):
    for j in range(5):
        if demand[i][j] > 0:
            n = trucks(demand[i][j])
            pallets += demand[i][j]
            direct_trucks += n
            direct_km += n * dist(at[i], at[j])
hub_trucks = 0
hub_km = 0
for k in range(5):
    out = sum(demand[k])
    inn = sum(row[k] for row in demand)
    n = trucks(out) + trucks(inn)
    hub_trucks += n
    hub_km += n * dist(at[k], hub)
    print(f"{names[k]}: sends {out}, receives {inn}, {n} hub trucks over {dist(at[k], hub)} km")
print(f"direct: 20 lanes, {direct_trucks} trucks, {direct_km} truck-km, fill {pallets * 100 // (direct_trucks * 26)}%")
print(f"hub: 10 lanes, {hub_trucks} trucks, {hub_km} truck-km, fill {pallets * 200 // (hub_trucks * 26)}%")
