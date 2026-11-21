def betweenness(n, links):
    adj = [[] for _ in range(n)]
    score = [0.0] * n
    for a, b in links:
        adj[a].append(b)
        adj[b].append(a)
    for s in range(n):
        sigma = [0] * n
        dist = [-1] * n
        delta = [0.0] * n
        sigma[s] = 1
        dist[s] = 0
        order = [s]
        head = 0
        while head < len(order):
            u = order[head]
            head += 1
            for w in adj[u]:
                if dist[w] < 0:
                    dist[w] = dist[u] + 1
                    order.append(w)
                if dist[w] == dist[u] + 1:
                    sigma[w] += sigma[u]
        i = len(order) - 1
        while i > 0:
            w = order[i]
            for v in adj[w]:
                if dist[v] == dist[w] - 1:
                    delta[v] += float(sigma[v]) / float(sigma[w]) * (1.0 + delta[w])
            score[w] += delta[w]
            i -= 1
    return [x / 2.0 for x in score]

names = ["Amy", "Bob", "Cal", "Dee", "Eli", "Fay", "Gil", "Hal"]
links = [[0, 1], [0, 2], [1, 2], [2, 3], [3, 4], [3, 5], [4, 5], [5, 6], [6, 7], [4, 6]]
b = betweenness(len(names), links)
ranked = sorted(range(len(names)), key=lambda i: -b[i])
for i in ranked:
    print(f"{names[i]:<4} {b[i]:>6.2f}")
