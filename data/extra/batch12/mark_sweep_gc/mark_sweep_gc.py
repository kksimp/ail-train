heap = [("config", [1]), ("logger", []), ("session", [3, 4]), ("cart", [5]), ("user", [2]), ("item", []), ("temp", [7]), ("buffer", [6])]
alive = [True] * len(heap)

def collect(heap, roots, alive):
    marked = [False] * len(heap)
    stack = list(roots)
    while stack:
        i = stack.pop()
        if alive[i] and not marked[i]:
            marked[i] = True
            for r in heap[i][1]:
                stack.append(r)
    freed = []
    for i in range(len(heap)):
        if alive[i] and not marked[i]:
            alive[i] = False
            freed.append(heap[i][0])
    return freed

rounds = [("both roots held", [0, 2]), ("session root dropped", [0]), ("config root dropped", [])]
for label, rs in rounds:
    freed = collect(heap, rs, alive)
    shown = "nothing" if len(freed) == 0 else ", ".join(freed)
    live = len([i for i in range(len(heap)) if alive[i]])
    print(f"{label}: freed {shown}; {live} objects live")
