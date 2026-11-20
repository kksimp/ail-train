def bc(pr, n):
    val = [0] * (n + 1); fst = [0] * (n + 1)
    for l in range(1, n + 1):
        for c in range(1, min(l, len(pr)) + 1):
            v = pr[c - 1] + val[l - c]
            if v > val[l]: val[l] = v; fst[l] = c
    ps, left = [], n
    while left > 0:
        ps.append(fst[left]); left -= fst[left]
    return val[n], ps
for n in [1, 4, 7, 8, 10, 13]:
    v, ps = bc([1, 5, 8, 9, 10, 17, 17, 20], n)
    print(f"length {n:>2}: {v:>2} from {'+'.join(map(str, ps))}")
