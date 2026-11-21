import heapq
landings = [(0, "L1"), (1, "L2"), (2, "L3"), (7, "L4"), (8, "L5"), (9, "L6"), (16, "L7")]
takeoffs = [(0, "T1"), (3, "T2"), (4, "T3"), (5, "T4"), (12, "T5")]
land_q = []; take_q = []
now = 0; li = 0; ti = 0; delay = [0, 0]
while li < len(landings) or ti < len(takeoffs) or land_q or take_q:
    while li < len(landings) and landings[li][0] <= now:
        heapq.heappush(land_q, landings[li]); li += 1
    while ti < len(takeoffs) and takeoffs[ti][0] <= now:
        heapq.heappush(take_q, takeoffs[ti]); ti += 1
    if land_q:
        t, f = heapq.heappop(land_q)
        delay[0] += now - t
        print(f"{now:>2}: {f} lands, {now - t} min late")
        now += 2
    elif take_q:
        t, f = heapq.heappop(take_q)
        delay[1] += now - t
        print(f"{now:>2}: {f} takes off, {now - t} min late")
        now += 2
    else:
        now += 1
print(f"landing delay {delay[0]} min, take-off delay {delay[1]} min")
