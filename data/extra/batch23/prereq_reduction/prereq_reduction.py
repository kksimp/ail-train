def reaches(adj, frm, target, skip):
    seen = set()
    stack = [v for v in adj[frm] if v != skip]
    while stack:
        u = stack.pop()
        if u == target:
            return True
        if u not in seen:
            seen.add(u)
            for w in adj[u]:
                stack.append(w)
    return False

names = ["intro", "maths", "data", "algo", "systems", "compilers", "graphics", "thesis"]
links = [[0, 2], [1, 2], [0, 3], [2, 3], [1, 3], [2, 4], [3, 5], [4, 5], [2, 5], [1, 6], [3, 6], [5, 7], [6, 7], [0, 7], [3, 7]]
adj = [[] for _ in names]
for a, b in links:
    adj[a].append(b)
kept = 0
for a, b in links:
    if reaches(adj, a, b, b):
        print(f"drop {names[a]} -> {names[b]} (implied)")
    else:
        kept += 1
print(f"{kept} of {len(links)} links are needed")
