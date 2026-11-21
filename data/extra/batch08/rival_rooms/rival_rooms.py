def split(n, pairs):
    adj = [[] for i in range(n)]; side = [-1] * n
    for a, b in pairs: adj[a].append(b); adj[b].append(a)
    for s in range(n):
        if side[s] == -1:
            side[s] = 0; q = [s]; h = 0
            while h < len(q):
                v = q[h]; h += 1
                for w in adj[v]:
                    if side[w] == -1: side[w] = 1 - side[v]; q.append(w)
                    elif side[w] == side[v]: return []
    return side
def show(people, pairs):
    side = split(len(people), pairs)
    if not side: print("no split: some rivals form an odd loop"); return
    a = [p for i, p in enumerate(people) if side[i] == 0]; b = [p for i, p in enumerate(people) if side[i] == 1]
    print(f"room A: {', '.join(a)} | room B: {', '.join(b)}")
people = ["Ida", "Jon", "Kim", "Lou", "Mo", "Nia"]
show(people, [[0, 1], [1, 2], [2, 3], [0, 3], [4, 5], [1, 4]])
show(people, [[0, 1], [1, 2], [2, 0], [3, 4]])
show(people, [[0, 5]])
