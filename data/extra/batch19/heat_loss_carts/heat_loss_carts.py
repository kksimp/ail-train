import heapq
def least(g, lo, hi):
    h = len(g); w = len(g[0])
    dr = [0, 1, 0, -1]; dc = [1, 0, -1, 0]
    big = 10000
    best = {}
    heap = [0]
    while heap:
        top = heapq.heappop(heap)
        cost = top // big; st = top % big
        run = st % 11; d = st // 11 % 4; cell = st // 44
        r = cell // w; c = cell % w
        if r == h - 1 and c == w - 1 and run >= lo:
            return cost
        if cost > best.get(st, cost):
            continue
        for nd in range(4):
            turning = nd != d
            if nd == (d + 2) % 4 or (not turning and run >= hi) or (turning and run > 0 and run < lo):
                continue
            nr = r + dr[nd]; nc = c + dc[nd]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            nrun = 1 if turning else run + 1
            ncost = cost + g[nr][nc]
            nst = ((nr * w + nc) * 4 + nd) * 11 + nrun
            if ncost < best.get(nst, 1000000):
                best[nst] = ncost
                heapq.heappush(heap, ncost * big + nst)
    return -1

rows = ["8252524", "8511325", "3278312", "5662879", "8296313", "5369222"]
g = [[int(ch) for ch in r] for r in rows]
for r in rows:
    print(r)
print(f"part 1, light cart (1 to 3 straight): least loss {least(g, 1, 3)}")
print(f"part 2, heavy cart (4 to 7 straight): least loss {least(g, 4, 7)}")
