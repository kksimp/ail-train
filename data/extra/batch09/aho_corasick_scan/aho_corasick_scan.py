def build(words):
    edges = [{}]
    fail = [0]
    out = [[]]
    for wi, w in enumerate(words):
        node = 0
        for c in w:
            if c not in edges[node]:
                edges.append({})
                fail.append(0)
                out.append([])
                edges[node][c] = len(edges) - 1
            node = edges[node][c]
        out[node].append(wi)
    queue = list(edges[0].values())
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for c, v in edges[u].items():
            queue.append(v)
            f = fail[u]
            while f > 0 and c not in edges[f]:
                f = fail[f]
            fail[v] = edges[f].get(c, 0)
            out[v].extend(list(out[fail[v]]))
    return edges, fail, out

words = ["he", "she", "his", "hers", "sea", "shore", "ell"]
edges, fail, out = build(words)
text = "she sells sea shells by the shore"
state = 0
found = 0
for i, c in enumerate(text):
    while state > 0 and c not in edges[state]:
        state = fail[state]
    state = edges[state].get(c, 0)
    for wi in out[state]:
        w = words[wi]
        start = i - len(w) + 1
        print(f"{start:>3} {w}")
        found += 1
print(f"{found} matches, {len(edges)} trie nodes")
