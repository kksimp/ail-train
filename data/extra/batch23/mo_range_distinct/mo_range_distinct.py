xs = [2, 5, 2, 8, 5, 3, 3, 9, 2, 8, 1, 5, 7, 7, 3, 2]
queries = [[0, 4], [3, 9], [1, 1], [5, 15], [0, 15], [10, 13], [2, 7], [8, 12]]
block = 4
order = sorted(range(len(queries)), key=lambda q: (queries[q][0] // block, queries[q][1]))
counts = {}
distinct = 0
lo = 0
hi = -1
moves = 0
answers = [0] * 8
for qi in order:
    l = queries[qi][0]
    r = queries[qi][1]
    while hi < r:
        hi += 1
        counts[xs[hi]] = counts.get(xs[hi], 0) + 1
        if counts[xs[hi]] == 1:
            distinct += 1
        moves += 1
    while hi > r:
        counts[xs[hi]] -= 1
        if counts[xs[hi]] == 0:
            distinct -= 1
        hi -= 1
        moves += 1
    while lo < l:
        counts[xs[lo]] -= 1
        if counts[xs[lo]] == 0:
            distinct -= 1
        lo += 1
        moves += 1
    while lo > l:
        lo -= 1
        counts[xs[lo]] = counts.get(xs[lo], 0) + 1
        if counts[xs[lo]] == 1:
            distinct += 1
        moves += 1
    answers[qi] = distinct
naive = 0
for i in range(len(queries)):
    q = queries[i]
    part = xs[q[0]:q[1] + 1]
    naive += len(part)
    print(f"[{q[0]:>2}, {q[1]:>2}]: {answers[i]} different values")
print(f"window steps: {moves} (rescanning each range would read {naive})")
