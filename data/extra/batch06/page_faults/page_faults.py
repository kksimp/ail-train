def fa(R, n, pol):
    M = []; c = 0
    for i, p in enumerate(R):
        if p in M:
            if pol == "LRU": M.remove(p); M.append(p)
            continue
        c += 1
        if len(M) == n:
            if pol == "OPT":
                v = 0; far = -1
                for k, m in enumerate(M):
                    rs = R[i + 1:]; nx = rs.index(m) if m in rs else 1000
                    if nx > far: far = nx; v = k
                M.pop(v)
            else: M.pop(0)
        M.append(p)
    return c
for R in [[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1], [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]]:
    for n in [3, 4]: print(f"{len(R)} refs, {n} frames: {', '.join(f'{p} {fa(R, n, p)}' for p in ['FIFO', 'LRU', 'OPT'])}")
