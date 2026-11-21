from collections import deque
def shortest(blocked):
    if 0 in blocked: return -1
    dist = {0: 0}; queue = [0]; head = 0
    while head < len(queue):
        u = queue[head]; head += 1
        if u == 48: return dist[u]
        r, c = divmod(u, 7)
        for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr = r + d[0]; nc = c + d[1]; k = nr * 7 + nc
            if 0 <= nr < 7 and 0 <= nc < 7 and k not in blocked and k not in dist:
                dist[k] = dist[u] + 1; queue.append(k)
    return -1

text = "1,4 3,6 6,3 6,4 5,6 2,5 4,3 2,0 6,1 4,5 1,5 5,3 4,6 2,2 0,1 5,1 5,2 4,2 6,0 5,5 0,3"
bs = [[int(v) for v in t.split(",")] for t in text.split(" ")]
blocked = set()
for i in range(12):
    blocked.add(bs[i][1] * 7 + bs[i][0])
print(f"{len(bs)} bytes fall")
print(f"part 1: after 12 bytes the shortest path takes {shortest(blocked)} steps")
for i in range(12, len(bs)):
    b = bs[i]
    blocked.add(b[1] * 7 + b[0])
    if shortest(blocked) < 0:
        print(f"part 2: byte {i + 1} at {b[0]},{b[1]} cuts the last path")
        break
