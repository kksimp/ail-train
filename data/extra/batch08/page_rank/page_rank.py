pages = ["home", "about", "blog", "shop", "help"]; links = [[1, 2, 3], [0], [0, 3], [0, 4], [0, 3]]
n = 5; d = 0.85; rank = [1.0 / n] * n
for it in range(60):
    nx = [(1.0 - d) / n] * n
    for i in range(n):
        sh = rank[i] / len(links[i])
        for j in links[i]: nx[j] += d * sh
    rank = nx
used = set()
for k in range(n):
    pick = -1
    for i in range(n):
        if i not in used and (pick < 0 or rank[i] > rank[pick]): pick = i
    used.add(pick); print(f"{k + 1}. {pages[pick]:<6} {rank[pick]:.3f}")
print(f"ranks sum to {sum(rank):.3f}")
