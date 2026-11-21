def fj(s):
    if len(s) <= 1: return 0
    j = reach = edge = 0
    for i in range(len(s) - 1):
        if i > reach: return None
        reach = max(reach, i + s[i])
        if i == edge:
            j += 1; edge = reach
            if edge >= len(s) - 1: return j
    return j if edge >= len(s) - 1 else None
for s in [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4], [1, 1, 1, 1], [5], [0, 1], [4, 1, 1, 3, 1, 1, 1]]:
    j = fj(s)
    print(f"{' '.join(map(str, s))}: {f'{j} jumps' if j is not None else 'stuck'}")
