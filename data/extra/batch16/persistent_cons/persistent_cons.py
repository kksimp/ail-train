pool = []

def push(head, v):
    pool.append((v, head))
    return len(pool) - 1

def update(head, idx, v):
    if idx == 0:
        return push(pool[head][1], v)
    rest = update(pool[head][1], idx - 1, v)
    return push(rest, pool[head][0])

def items(head):
    out = []
    c = head
    while c >= 0:
        out.append(pool[c][0])
        c = pool[c][1]
    return out

v1 = push(-1, 3)
v2 = push(push(v1, 5), 6)
v3 = push(v1, 8)
v4 = pool[v2][1]
v5 = update(v2, 2, 30)
v6 = push(v4, 9)
names = ["v1", "v2", "v3", "v4", "v5", "v6"]
heads = [v1, v2, v3, v4, v5, v6]
total = 0
for i in range(len(heads)):
    xs = items(heads[i])
    total += len(xs)
    print(f"{names[i]}: {xs}")
print(f"{len(pool)} cells hold {total} list elements across six versions")
