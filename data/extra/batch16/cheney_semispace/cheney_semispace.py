heap = [("A", [3]), ("B", [0]), ("C", [5, 6]), ("D", [2]), ("E", []), ("F", [3]), ("G", []), ("H", [1])]
roots = [5, 4]
to = []
fwd = {}

def evacuate(old):
    if old in fwd:
        return fwd[old]
    fwd[old] = len(to)
    to.append([heap[old][0], list(heap[old][1])])
    return fwd[old]

new_roots = [evacuate(r) for r in roots]
scan = 0
while scan < len(to):
    obj = to[scan]
    moved = [evacuate(r) for r in obj[1]]
    to[scan][1] = moved
    scan += 1
for i in range(len(to)):
    print(f"to[{i}] {to[i][0]} fields {to[i][1]}")
print(f"roots now {new_roots}")
dead = [heap[i][0] for i in range(len(heap)) if i not in fwd]
print(f"left behind: {', '.join(dead)}")
print(f"copied {len(to)} of {len(heap)} objects")
