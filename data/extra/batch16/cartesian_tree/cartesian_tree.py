def build(xs):
    parent = [-1] * len(xs)
    stack = []
    for i in range(len(xs)):
        last = -1
        while stack and xs[stack[-1]] > xs[i]:
            last = stack.pop()
        if last >= 0:
            parent[last] = i
        if stack:
            parent[i] = stack[-1]
        stack.append(i)
    return parent

def depth(parent, i):
    d = 0
    while parent[i] >= 0:
        i = parent[i]
        d += 1
    return d

def lca(parent, a, b):
    x, y = a, b
    while depth(parent, x) > depth(parent, y):
        x = parent[x]
    while depth(parent, y) > depth(parent, x):
        y = parent[y]
    while x != y:
        x = parent[x]
        y = parent[y]
    return x

xs = [5, 2, 8, 6, 1, 9, 4, 7, 3]
parent = build(xs)
print(f"values  {xs}")
print(f"parents {parent}")
depths = [depth(parent, i) for i in range(len(xs))]
print(f"depths  {depths}")
for q in [[0, 3], [2, 3], [5, 8], [6, 7], [2, 8]]:
    m = lca(parent, q[0], q[1])
    brute = min(xs[q[0]:q[1] + 1])
    print(f"min of positions {q[0]}..{q[1]}: {xs[m]} at {m} (scan says {brute})")
