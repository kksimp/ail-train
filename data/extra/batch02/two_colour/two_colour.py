from collections import deque
for n, edges in [(4, [(0, 1), (1, 2), (2, 3), (3, 0)]), (3, [(0, 1), (1, 2), (2, 0)]), (6, [(0, 3), (1, 4), (2, 5), (0, 4)]), (2, [])]:
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    col, err = {}, None
    for s in range(n):
        if s in col: continue
        col[s] = 0; q = deque([s])
        while q and not err:
            u = q.popleft()
            for v in adj.get(u, []):
                if v not in col:
                    col[v] = 1 - col[u]; q.append(v)
                elif col[v] == col[u]:
                    err = f"edge {u}-{v} joins two nodes of one colour"; break
        if err: break
    if err:
        print(f"{n} nodes: not two-colourable ({err})")
    else:
        print(f"{n} nodes: {','.join(str(i) for i in range(n) if col[i] == 0)} | {','.join(str(i) for i in range(n) if col[i] == 1)}")
