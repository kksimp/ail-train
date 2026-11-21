def compose(a, b):
    return [a[b[i]] for i in range(4)]
elems = [[(i + k) % 4 for i in range(4)] for k in range(4)] + [[(k - i + 4) % 4 for i in range(4)] for k in range(4)]
names = ["e", "r1", "r2", "r3", "s0", "s1", "s2", "s3"]
print(" o |" + " ".join(n.rjust(2) for n in names))
for a in range(8):
    cells = [names[elems.index(compose(elems[a], elems[b]))].rjust(2) for b in range(8)]
    print(f"{names[a]:>2} |" + " ".join(cells))
orders = []
for a in range(8):
    p = elems[a]
    m = 1
    while p != elems[0]:
        p = compose(elems[a], p)
        m += 1
    orders.append(f"{names[a]}:{m}")
print("orders " + " ".join(orders))
x = elems.index(compose(elems[1], elems[4]))
y = elems.index(compose(elems[4], elems[1]))
print(f"r1 after s0 is {names[x]}, s0 after r1 is {names[y]}: not commutative")
