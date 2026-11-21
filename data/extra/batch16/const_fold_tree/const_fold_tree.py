class Node:
    def __init__(s, op, val, l, r):
        s.op, s.val, s.l, s.r = op, val, l, r

class Folded:
    def __init__(s, known, val, text):
        s.known, s.val, s.text = known, val, text

def add_node(t, op, val, l, r):
    t.append(Node(op, val, l, r))
    return len(t) - 1

def show(t, i):
    n = t[i]
    if n.op == "num":
        return f"{n.val}"
    if n.l < 0:
        return n.op
    return f"({show(t, n.l)} {n.op} {show(t, n.r)})"

def leaf(f):
    return f"{f.val}" if f.known else f.text

def konst(v):
    return Folded(True, v, "")

def fold(t, i):
    n = t[i]
    if n.op == "num":
        return konst(n.val)
    if n.l < 0:
        return Folded(False, 0, n.op)
    a = fold(t, n.l)
    b = fold(t, n.r)
    if a.known and b.known:
        v = a.val + b.val if n.op == "+" else a.val * b.val
        return konst(v)
    if n.op == "*" and ((a.known and a.val == 0) or (b.known and b.val == 0)):
        return konst(0)
    one = 1 if n.op == "*" else 0
    if a.known and a.val == one:
        return b
    if b.known and b.val == one:
        return a
    return Folded(False, 0, f"({leaf(a)} {n.op} {leaf(b)})")

t = []
x = add_node(t, "x", 0, -1, -1)
y = add_node(t, "y", 0, -1, -1)
n2 = add_node(t, "num", 2, -1, -1)
n3 = add_node(t, "num", 3, -1, -1)
n0 = add_node(t, "num", 0, -1, -1)
n1 = add_node(t, "num", 1, -1, -1)
m6 = add_node(t, "*", 0, n2, n3)
e1 = add_node(t, "+", 0, m6, x)
p1 = add_node(t, "+", 0, n1, n0)
e2 = add_node(t, "*", 0, x, p1)
s4 = add_node(t, "+", 0, n2, n2)
y4 = add_node(t, "*", 0, y, s4)
x0 = add_node(t, "+", 0, x, n0)
e3 = add_node(t, "*", 0, x0, y4)
z = add_node(t, "*", 0, n0, n3)
yz = add_node(t, "+", 0, y, m6)
e4 = add_node(t, "*", 0, yz, z)
for e in [e1, e2, e3, e4]:
    before = show(t, e)
    after = leaf(fold(t, e))
    print(f"{before:<26} => {after}")
print(f"nodes in pool: {len(t)}")
