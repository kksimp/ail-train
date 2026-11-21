keys = []
kids = []
melds = [0]

def meld(a, b):
    if a < 0:
        return b
    if b < 0:
        return a
    melds[0] += 1
    if keys[b] < keys[a]:
        kids[b].append(a)
        return b
    kids[a].append(b)
    return a

def add(root, k):
    keys.append(k)
    kids.append([])
    return meld(root, len(keys) - 1)

def pop_min(root):
    cs = list(kids[root])
    paired = []
    i = 0
    while i < len(cs):
        if i + 1 < len(cs):
            paired.append(meld(cs[i], cs[i + 1]))
        else:
            paired.append(cs[i])
        i += 2
    out = -1
    j = len(paired) - 1
    while j >= 0:
        out = meld(paired[j], out)
        j -= 1
    return out

root = -1
for k in [42, 17, 8, 99, 23, 4, 61, 15, 30, 8, 77, 12]:
    root = add(root, k)
print(f"inserted 12 keys with {melds[0]} melds, minimum {keys[root]}")
order = []
while root >= 0:
    order.append(keys[root])
    root = pop_min(root)
print(f"pop order {order}")
print(f"total melds {melds[0]}")
