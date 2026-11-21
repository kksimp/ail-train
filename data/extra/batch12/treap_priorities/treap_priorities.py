class Node:
    def __init__(self, key, pri):
        self.key = key; self.pri = pri; self.left = -1; self.right = -1

def insert(ns, root, key, pri):
    if root < 0:
        ns.append(Node(key, pri))
        return len(ns) - 1
    if key < ns[root].key:
        sub = insert(ns, ns[root].left, key, pri)
        ns[root].left = sub
        if ns[sub].pri > ns[root].pri:
            ns[root].left = ns[sub].right
            ns[sub].right = root
            return sub
    else:
        sub = insert(ns, ns[root].right, key, pri)
        ns[root].right = sub
        if ns[sub].pri > ns[root].pri:
            ns[root].right = ns[sub].left
            ns[sub].left = root
            return sub
    return root

def depth(ns, i):
    if i < 0:
        return 0
    return 1 + max(depth(ns, ns[i].left), depth(ns, ns[i].right))

seed = 2024
ns = []
root = -1
bst = []
broot = -1
for key in range(1, 32):
    seed = (seed * 75 + 74) % 65537
    root = insert(ns, root, key, seed)
    broot = insert(bst, broot, key, 0)
print("31 sorted keys")
print(f"plain tree depth: {depth(bst, broot)}")
print(f"treap depth: {depth(ns, root)}")
print(f"treap root: key {ns[root].key}, priority {ns[root].pri}")
l = ns[root].left
r = ns[root].right
print(f"root children: {ns[l].key} and {ns[r].key}")
