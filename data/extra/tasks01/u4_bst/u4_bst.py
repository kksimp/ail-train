import sys

def to_int(s):
    t = s[1:] if s.startswith("-") else s
    if t.isascii() and t.isdigit():
        return int(s)
    return None

class Node:
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None

root = None

def insert(n, k):
    if n is None:
        return Node(k), True
    if k < n.k:
        n.l, ok = insert(n.l, k)
    elif k > n.k:
        n.r, ok = insert(n.r, k)
    else:
        return n, False
    return n, ok

def delete(n, k):
    if n is None:
        return None, False
    if k < n.k:
        n.l, ok = delete(n.l, k)
        return n, ok
    if k > n.k:
        n.r, ok = delete(n.r, k)
        return n, ok
    if n.l is None:
        return n.r, True
    if n.r is None:
        return n.l, True
    m = n.r
    while m.l is not None:
        m = m.l
    n.k = m.k
    n.r, _ = delete(n.r, m.k)
    return n, True

def inorder(n, out):
    if n is not None:
        inorder(n.l, out)
        out.append(n.k)
        inorder(n.r, out)

def height(n):
    return 0 if n is None else 1 + max(height(n.l), height(n.r))

def contains(n, k):
    while n is not None:
        if k == n.k:
            return True
        n = n.l if k < n.k else n.r
    return False

for line in sys.stdin.read().splitlines():
    w = line.split()
    if not w:
        continue
    c = w[0]
    if c in ("insert", "delete", "contains") and len(w) == 2 and to_int(w[1]) is not None:
        k = to_int(w[1])
        if c == "insert":
            root, ok = insert(root, k)
            print("ok" if ok else "dup")
        elif c == "delete":
            root, ok = delete(root, k)
            print("ok" if ok else "missing")
        else:
            print("yes" if contains(root, k) else "no")
    elif c == "inorder" and len(w) == 1:
        out = []
        inorder(root, out)
        print(" ".join(map(str, out)) if out else "empty")
    elif c == "height" and len(w) == 1:
        print(height(root))
    elif c == "min" and len(w) == 1:
        if root is None:
            print("empty")
        else:
            m = root
            while m.l is not None:
                m = m.l
            print(m.k)
    else:
        print("error")
