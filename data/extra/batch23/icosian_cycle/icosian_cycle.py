def build(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return adj

def extend(adj, path, used, steps):
    steps[0] += 1
    last = path[-1]
    if len(path) == len(adj):
        return path[0] in adj[last]
    for v in adj[last]:
        if not used[v]:
            used[v] = True
            path.append(v)
            if extend(adj, path, used, steps):
                return True
            path.pop()
            used[v] = False
    return False

def tour(name, adj):
    used = [i == 0 for i in range(len(adj))]
    path = [0]
    steps = [0]
    if extend(adj, path, used, steps):
        shown = "-".join(str(x) for x in path)
        print(f"{name}: cycle {shown}-0")
    else:
        print(f"{name}: no Hamiltonian cycle")
    print(f"  {steps[0]} search steps")

dodeca = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 5], [1, 7], [2, 9], [3, 11], [4, 13], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 5], [6, 15], [8, 16], [10, 17], [12, 18], [14, 19], [15, 16], [16, 17], [17, 18], [18, 19], [19, 15]]
petersen = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0], [0, 5], [1, 6], [2, 7], [3, 8], [4, 9], [5, 7], [7, 9], [9, 6], [6, 8], [8, 5]]
tour("dodecahedron", build(20, dodeca))
tour("petersen", build(10, petersen))
tour("square", build(4, [[0, 1], [1, 2], [2, 3], [3, 0]]))
