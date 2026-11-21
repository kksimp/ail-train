def cut_size(edges, side):
    return sum(1 for e in edges if side[e[0]] != side[e[1]])

def local_search(n, edges, side):
    moves = 0
    improved = True
    while improved:
        improved = False
        for v in range(n):
            same = 0
            across = 0
            for e in edges:
                if e[0] == v or e[1] == v:
                    other = e[1] if e[0] == v else e[0]
                    if side[other] == side[v]:
                        same += 1
                    else:
                        across += 1
            if same > across:
                side[v] = 1 - side[v]
                moves += 1
                improved = True
    return moves

n = 10
edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 6], [5, 6], [5, 7], [6, 8], [7, 8], [7, 9], [8, 9], [0, 9], [2, 7]]
side = [0] * 10
moves = local_search(n, edges, side)
found = cut_size(edges, side)
print(f"{len(edges)} rivalries; after {moves} moves {found} cross the split")
print(f"team of each member: {side}")
best = 0
for mask in range(1 << n):
    trial = [(mask >> i) & 1 for i in range(n)]
    best = max(best, cut_size(edges, trial))
print(f"best possible split cuts {best}; half of all edges is {len(edges) // 2}")
