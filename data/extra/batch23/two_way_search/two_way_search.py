def neighbours(v, n):
    return [(v + 1) % n, (v + n - 1) % n, v * 2 % n, v * 5004 % n]

def one_way(n, s, t):
    d = [-1] * n
    d[s] = 0
    queue = [s]
    head = 0
    labelled = 1
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in neighbours(u, n):
            if d[v] < 0:
                d[v] = d[u] + 1
                labelled += 1
                if v == t:
                    return [d[v], labelled]
                queue.append(v)
    return [d[t], labelled]

def expand(front, n, mine, other, stats):
    nxt = []
    for u in front:
        for v in neighbours(u, n):
            if other[v] >= 0:
                total = mine[u] + 1 + other[v]
                if stats[1] < 0 or total < stats[1]:
                    stats[1] = total
            if mine[v] < 0:
                mine[v] = mine[u] + 1
                stats[0] += 1
                nxt.append(v)
    return nxt

def two_way(n, s, t):
    ds = [-1] * n
    dt = [-1] * n
    ds[s] = 0
    dt[t] = 0
    fs = [s]
    ft = [t]
    stats = [2, -1]
    while stats[1] < 0 and len(fs) > 0 and len(ft) > 0:
        if len(fs) <= len(ft):
            fs = expand(fs, n, ds, dt, stats)
        else:
            ft = expand(ft, n, dt, ds, stats)
    return [stats[1], stats[0]]

n = 10007
print(f"{n} nodes, from node 1; 5004 halves because 2 x 5004 = 1 mod {n}")
for t in [9, 77, 500, 1234, 3141, 9999]:
    a = one_way(n, 1, t)
    b = two_way(n, 1, t)
    print(f"to {t:>4}: distance {a[0]:>2} | one-way labels {a[1]:>4} | two-way labels {b[1]:>3} (distance {b[0]})")
