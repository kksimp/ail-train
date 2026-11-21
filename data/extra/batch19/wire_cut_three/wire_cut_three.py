def group_size(n, edges, cut):
    adj = [[] for i in range(n)]
    for i, e in enumerate(edges):
        if i not in cut:
            adj[e[0]].append(e[1]); adj[e[1]].append(e[0])
    seen = {0}; queue = [0]
    while queue:
        v = queue.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); queue.append(w)
    return len(seen)

names = ["ab", "cd", "ef", "gh", "ij", "kl", "mn", "op"]
links = ["ab-cd", "ab-ef", "cd-ef", "cd-gh", "ef-gh", "ab-gh", "ij-kl", "ij-mn", "kl-mn", "kl-op", "mn-op", "ij-op", "ab-ij", "cd-kl", "gh-op"]
index = {n: i for i, n in enumerate(names)}
edges = [[index[x] for x in l.split("-")] for l in links]
n = len(names)
splits = 0; answer = 0
for a in range(len(edges)):
    for b in range(a + 1, len(edges)):
        for c in range(b + 1, len(edges)):
            size = group_size(n, edges, [a, b, c])
            if size < n:
                splits += 1
                if size * (n - size) > answer:
                    answer = size * (n - size)
                    print(f"cutting {links[a]}, {links[b]}, {links[c]} leaves groups of {size} and {n - size}")
print(f"part 1: group size product {answer}")
print(f"part 2: {splits} of the triples split the panel")
