def safe(free, held, most):
    work = list(free); done = [False] * len(held); order = []; prog = True
    while prog:
        prog = False
        for i in range(len(held)):
            if not done[i] and all(most[i][r] - held[i][r] <= work[r] for r in range(len(work))):
                for r in range(len(work)): work[r] += held[i][r]
                done[i] = True; order.append(i); prog = True
    return order
held = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
most = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
for free in [[3, 3, 2], [1, 0, 2], [0, 1, 1]]:
    o = safe(free, held, most); lab = ",".join(str(x) for x in free)
    if len(o) == len(held): print(f"free {lab}: safe, order {' '.join(f'J{i}' for i in o)}")
    else: print(f"free {lab}: unsafe, only {len(o)} of {len(held)} can finish")
