def shortest(grid, limit):
    cells = [list(line) for line in grid]
    rows = len(cells)
    cols = len(cells[0])
    layers = limit + 1
    dist = [-1] * (rows * cols * layers)
    dist[0] = 0
    queue = [0]
    head = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while head < len(queue):
        s = queue[head]
        head += 1
        k = s % layers
        cell = s // layers
        r = cell // cols
        c = cell % cols
        if r == rows - 1 and c == cols - 1:
            return dist[s]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols:
                wall = 1 if cells[nr][nc] == '#' else 0
                nk = k + wall
                if nk <= limit:
                    ns = (nr * cols + nc) * layers + nk
                    if dist[ns] < 0:
                        dist[ns] = dist[s] + 1
                        queue.append(ns)
    return -1

grid = [".........", "########.", ".........", ".########", ".........", "########.", "........."]
for row in grid:
    print(row)
for k in range(3):
    steps = shortest(grid, k)
    shown = "no way through" if steps < 0 else f"{steps} steps"
    print(f"break up to {k} walls: {shown}")
