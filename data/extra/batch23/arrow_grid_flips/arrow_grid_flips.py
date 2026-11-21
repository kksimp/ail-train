from collections import deque

def min_flips(grid):
    rows = len(grid)
    cols = len(grid[0])
    cells = [list(line) for line in grid]
    dist = [1000000] * (rows * cols)
    dist[0] = 0
    dq = deque([0])
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    arrows = ['>', '<', 'v', '^']
    while dq:
        u = dq.popleft()
        r = u // cols
        c = u % cols
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < rows and 0 <= nc < cols:
                w = 0 if cells[r][c] == arrows[k] else 1
                v = nr * cols + nc
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if w == 0:
                        dq.appendleft(v)
                    else:
                        dq.append(v)
    return dist[rows * cols - 1]

grids = [[">>>>", "<<<<", ">>>>", "<<<<"], [">v<", "^<v", "<^<"], ["v>>v", ">^<v", "^<>v", "<<<>"]]
for g in grids:
    for line in g:
        print(line)
    print(f"fewest flips from top-left to bottom-right: {min_flips(g)}")
