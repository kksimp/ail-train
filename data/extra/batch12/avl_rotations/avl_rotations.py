class Node:
    def __init__(self, key):
        self.key = key; self.left = -1; self.right = -1; self.height = 1

def ht(ns, i):
    return 0 if i < 0 else ns[i].height

def fix(ns, i):
    ns[i].height = 1 + max(ht(ns, ns[i].left), ht(ns, ns[i].right))

def rot_right(ns, y):
    x = ns[y].left
    ns[y].left = ns[x].right
    ns[x].right = y
    fix(ns, y); fix(ns, x)
    return x

def rot_left(ns, x):
    y = ns[x].right
    ns[x].right = ns[y].left
    ns[y].left = x
    fix(ns, x); fix(ns, y)
    return y

def insert(ns, root, key, log):
    if root < 0:
        ns.append(Node(key))
        return len(ns) - 1
    if key < ns[root].key:
        ns[root].left = insert(ns, ns[root].left, key, log)
    else:
        ns[root].right = insert(ns, ns[root].right, key, log)
    fix(ns, root)
    bal = ht(ns, ns[root].left) - ht(ns, ns[root].right)
    k = ns[root].key
    if bal > 1:
        l = ns[root].left
        if key >= ns[l].key:
            log.append(f"left-right at {k}")
            ns[root].left = rot_left(ns, l)
        else:
            log.append(f"right at {k}")
        return rot_right(ns, root)
    if bal < -1:
        r = ns[root].right
        if key < ns[r].key:
            log.append(f"right-left at {k}")
            ns[root].right = rot_right(ns, r)
        else:
            log.append(f"left at {k}")
        return rot_left(ns, root)
    return root

def pre(ns, i, out):
    if i >= 0:
        out.append(f"{ns[i].key}/{ns[i].height}")
        pre(ns, ns[i].left, out)
        pre(ns, ns[i].right, out)

ns = []
root = -1
for key in [10, 20, 30, 40, 50, 25, 5, 4, 3, 35, 45, 47]:
    log = []
    root = insert(ns, root, key, log)
    note = ", ".join(log) if len(log) > 0 else "no rotation"
    print(f"insert {key:>2}: {note}")
out = []
pre(ns, root, out)
print(f"preorder key/height: {' '.join(out)}")
