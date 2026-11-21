def trail(edges, start):
    used = [False] * len(edges); stack = [start]; path = []
    while stack:
        v = stack[-1]; found = -1
        for i in range(len(edges)):
            if not used[i] and (edges[i][0] == v or edges[i][1] == v): found = i; break
        if found < 0: path.append(v); stack.pop()
        else:
            used[found] = True; stack.append(edges[found][1] if edges[found][0] == v else edges[found][0])
    return path[::-1]
def plan(places, edges):
    deg = [0] * len(places)
    for a, b in edges: deg[a] += 1; deg[b] += 1
    odd = [i for i in range(len(places)) if deg[i] % 2 == 1]
    if len(odd) not in (0, 2): print(f"{len(odd)} places with odd paths: no single walk"); return
    s = odd[0] if len(odd) == 2 else 0
    print(" -> ".join(places[i] for i in trail(edges, s)))
places = ["Gate", "Pond", "Mill", "Hill", "Oak"]
plan(places, [[0, 1], [1, 2], [2, 0], [0, 3], [3, 4], [4, 0], [1, 3]])
plan(places, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]])
plan(places, [[0, 1], [0, 2], [0, 3], [1, 2]])
