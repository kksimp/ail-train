def height(ch):
    if ch == 'S': return 0
    if ch == 'E': return 25
    return ord(ch) - 97

lines = ["Sabcdefg", "onmlkjih", "pqrstuvw", "abccEzyx", "aabbccdd"]
g = [list(l) for l in lines]
rows = len(g); cols = len(g[0])
dist = {}; queue = []
for r in range(rows):
    for c in range(cols):
        if g[r][c] == 'E':
            dist[r * 100 + c] = 0; queue.append(r * 100 + c)
head = 0
while head < len(queue):
    cur = queue[head]; head += 1
    r = cur // 100; c = cur % 100
    for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nr = r + d[0]; nc = c + d[1]
        if 0 <= nr < rows and 0 <= nc < cols and (nr * 100 + nc) not in dist:
            if height(g[r][c]) <= height(g[nr][nc]) + 1:
                dist[nr * 100 + nc] = dist[cur] + 1; queue.append(nr * 100 + nc)
print(f"{len(dist)} of {rows * cols} cells can reach the summit")
print(f"part 1: {dist.get(0, -1)} steps from S")
best = 1000
for r in range(rows):
    for c in range(cols):
        if height(g[r][c]) == 0 and (r * 100 + c) in dist:
            best = min(best, dist[r * 100 + c])
print(f"part 2: {best} steps from the best low cell")
