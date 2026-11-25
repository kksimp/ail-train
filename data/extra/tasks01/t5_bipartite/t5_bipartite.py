import sys


def side_line(label, names):
    return f"{label}: " + " ".join(names) if names else f"{label}:"


adj = {}
nodes = set()
for line in sys.stdin.read().splitlines():
    w = line.split()
    if len(w) != 2:
        continue
    nodes.update(w)
    adj.setdefault(w[0], []).append(w[1])
    adj.setdefault(w[1], []).append(w[0])
color = {}
for root in sorted(nodes):
    if root in color:
        continue
    color[root] = 0
    queue = [root]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in sorted(adj.get(u, [])):
            if v not in color:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                print("not bipartite")
                print(f"conflict: {u} {v}")
                sys.exit(0)
print("bipartite")
print(side_line("left", [n for n in sorted(nodes) if color[n] == 0]))
print(side_line("right", [n for n in sorted(nodes) if color[n] == 1]))
