class Node:
    def __init__(self, score, name):
        self.score = score; self.name = name; self.left = -1; self.right = -1; self.rank = 1

def rk(ns, i):
    return 0 if i < 0 else ns[i].rank

def merge(ns, a, b):
    if a < 0:
        return b
    if b < 0:
        return a
    x, y = a, b
    if ns[y].score < ns[x].score:
        x, y = b, a
    ns[x].right = merge(ns, ns[x].right, y)
    if rk(ns, ns[x].left) < rk(ns, ns[x].right):
        ns[x].left, ns[x].right = ns[x].right, ns[x].left
    ns[x].rank = rk(ns, ns[x].right) + 1
    return x

def add(ns, root, score, name):
    ns.append(Node(score, name))
    return merge(ns, root, len(ns) - 1)

ns = []
north = -1
for score, name in [(4, "Ali"), (9, "Bea"), (2, "Cal"), (7, "Dee")]:
    north = add(ns, north, score, name)
south = -1
for score, name in [(5, "Eve"), (1, "Fox"), (8, "Gus"), (3, "Hal"), (6, "Ida")]:
    south = add(ns, south, score, name)
print(f"north top: {ns[north].name}, south top: {ns[south].name}")
root = merge(ns, north, south)
print(f"merged root rank: {ns[root].rank}")
order = []
while root >= 0:
    order.append(f"{ns[root].name}({ns[root].score})")
    l = ns[root].left
    r = ns[root].right
    root = merge(ns, l, r)
print(f"seen in order: {' '.join(order)}")
