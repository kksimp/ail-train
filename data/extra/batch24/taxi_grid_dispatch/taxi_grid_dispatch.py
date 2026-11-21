taxis = [[0, 0, 0, 0], [5, 5, 0, 0], [9, 1, 0, 0]]
def dist(ax, ay, bx, by): return abs(ax - bx) + abs(ay - by)
rides = [[0, 1, 1, 6, 4], [2, 8, 2, 3, 7], [3, 4, 4, 9, 9], [4, 0, 8, 2, 0], [6, 6, 6, 1, 1], [7, 9, 9, 0, 9]]
total_wait = 0
for q in rides:
    t = q[0]
    pick = -1
    for i in range(3):
        if taxis[i][2] <= t:
            if pick < 0 or dist(taxis[i][0], taxis[i][1], q[1], q[2]) < dist(taxis[pick][0], taxis[pick][1], q[1], q[2]):
                pick = i
    if pick < 0:
        pick = 0
        for i in range(1, 3):
            if taxis[i][2] < taxis[pick][2]: pick = i
    start = max(taxis[pick][2], t)
    reach = dist(taxis[pick][0], taxis[pick][1], q[1], q[2])
    wait = start - t + reach
    total_wait += wait
    taxis[pick][3] += reach
    taxis[pick][2] = start + reach + dist(q[1], q[2], q[3], q[4])
    taxis[pick][0] = q[3]; taxis[pick][1] = q[4]
    print(f"minute {t}: taxi {pick + 1} picks up at ({q[1]},{q[2]}) after {wait} min, free again at {taxis[pick][2]}")
print(f"total wait {total_wait} min, empty km per taxi {[tx[3] for tx in taxis]}")
