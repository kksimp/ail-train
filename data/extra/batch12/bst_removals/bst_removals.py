class Node:
    def __init__(self, key):
        self.key = key; self.left = -1; self.right = -1

def add(ns, root, key):
    if root < 0:
        ns.append(Node(key))
        return len(ns) - 1
    if key < ns[root].key:
        ns[root].left = add(ns, ns[root].left, key)
    else:
        ns[root].right = add(ns, ns[root].right, key)
    return root

def remove(ns, root, key):
    if root < 0:
        return -1
    l = ns[root].left
    r = ns[root].right
    if key < ns[root].key:
        ns[root].left = remove(ns, l, key)
        return root
    if key > ns[root].key:
        ns[root].right = remove(ns, r, key)
        return root
    if l < 0:
        return r
    if r < 0:
        return l
    s = r
    while ns[s].left >= 0:
        s = ns[s].left
    succ = ns[s].key
    ns[root].key = succ
    ns[root].right = remove(ns, r, succ)
    return root

def walk(ns, i, pre, out):
    if i < 0:
        return
    if pre:
        out.append(ns[i].key)
    walk(ns, ns[i].left, pre, out)
    if not pre:
        out.append(ns[i].key)
    walk(ns, ns[i].right, pre, out)

def show(ns, root):
    a = []; b = []
    walk(ns, root, False, a)
    walk(ns, root, True, b)
    return f"in {a} pre {b}"

ns = []
root = -1
for k in [50, 30, 70, 20, 40, 60, 80, 35, 45, 65]:
    root = add(ns, root, k)
print(f"start: {show(ns, root)}")
for k in [20, 60, 30, 50, 99]:
    root = remove(ns, root, k)
    print(f"remove {k}: {show(ns, root)}")
