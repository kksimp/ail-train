D = []; L = []
for c in [18, 12, 30, 7, 25, 9, 14, 22, 5, 11]:
    p = -1
    for i in range(len(L)):
        if L[i] >= c and (p < 0 or L[i] < L[p]): p = i
    if p < 0: D.append([c]); L.append(50 - c)
    else: D[p].append(c); L[p] -= c
for i in range(len(D)): print(f"drum {i + 1}: {' + '.join(map(str, D[i]))}, offcut {L[i]} m")
print(f"waste {sum(L)} m over {len(D)} drums")
