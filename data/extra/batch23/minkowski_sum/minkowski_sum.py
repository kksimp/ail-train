def lowest_first(p):
    k = 0
    for i in range(1, len(p)):
        if p[i][1] < p[k][1] or (p[i][1] == p[k][1] and p[i][0] < p[k][0]):
            k = i
    return [p[(k + i) % len(p)] for i in range(len(p))]

def minkowski(a0, b0):
    a = lowest_first(a0)
    b = lowest_first(b0)
    n = len(a)
    m = len(b)
    a.append(a[0])
    a.append(a[1])
    b.append(b[0])
    b.append(b[1])
    out = []
    i = 0
    j = 0
    while i < n or j < m:
        out.append([a[i][0] + b[j][0], a[i][1] + b[j][1]])
        ex = a[i + 1][0] - a[i][0]
        ey = a[i + 1][1] - a[i][1]
        fx = b[j + 1][0] - b[j][0]
        fy = b[j + 1][1] - b[j][1]
        c = ex * fy - ey * fx
        if c >= 0 and i < n:
            i += 1
        if c <= 0 and j < m:
            j += 1
    return out

def twice_area(p):
    s = 0
    for i in range(len(p)):
        q = p[(i + 1) % len(p)]
        s += p[i][0] * q[1] - q[0] * p[i][1]
    return s

def show(p):
    return " ".join(f"({v[0]},{v[1]})" for v in p)

obstacle = [[4, 2], [8, 3], [7, 7], [3, 6]]
robot = [[0, 0], [2, 0], [1, 2]]
flipped = [[-v[0], -v[1]] for v in robot]
region = minkowski(obstacle, flipped)
print(f"obstacle: {show(obstacle)}")
print(f"no-go region for the robot's anchor: {show(region)}")
print(f"doubled areas: obstacle {twice_area(obstacle)}, robot {twice_area(robot)}, region {twice_area(region)}")
squares = minkowski([[0, 0], [1, 0], [1, 1], [0, 1]], [[0, 0], [2, 0], [2, 2], [0, 2]])
print(f"unit square + 2-square: {show(squares)}")
