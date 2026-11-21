def routes(adj, at, path, spare):
    if at == "end": return 1
    total = 0
    for nxt in adj[at]:
        if nxt == "start": continue
        small = nxt == nxt.lower()
        if small and nxt in path:
            if spare:
                path.append(nxt)
                total += routes(adj, nxt, path, False)
                path.pop()
        else:
            path.append(nxt)
            total += routes(adj, nxt, path, spare)
            path.pop()
    return total

links = ["start-ka", "start-MX", "ka-MX", "ka-pt", "MX-pt", "pt-end", "ka-end", "MX-zz", "zz-end", "ka-QB", "QB-pt"]
adj = {}
for l in links:
    a, b = l.split("-")
    adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
print(f"{len(adj)} caves, {len(links)} tunnels")
print(f"part 1: {routes(adj, 'start', ['start'], False)} routes")
print(f"part 2: {routes(adj, 'start', ['start'], True)} routes with one repeat")
