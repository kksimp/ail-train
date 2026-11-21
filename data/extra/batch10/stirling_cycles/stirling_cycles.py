def table(size):
    c = []
    for n in range(size + 1):
        row = [0] * (size + 1)
        if n == 0:
            row[0] = 1
        else:
            for k in range(1, n + 1):
                row[k] = c[n - 1][k - 1] + (n - 1) * c[n - 1][k]
        c.append(row)
    return c

def cycles(perm):
    seen = [False] * len(perm)
    count = 0
    for s in range(len(perm)):
        if not seen[s]:
            count += 1
            j = s
            while not seen[j]:
                seen[j] = True
                j = perm[j]
    return count

def count_by_cycles(n, perm, used, counts):
    if len(perm) == n:
        counts[cycles(perm)] += 1
        return
    for v in range(n):
        if not used[v]:
            used[v] = True
            perm.append(v)
            count_by_cycles(n, perm, used, counts)
            perm.pop()
            used[v] = False

c = table(7)
for n in range(1, 8):
    row = c[n][1:n + 1]
    print(f"n = {n}: {row} sum {sum(row)}")
counts = [0] * 6
count_by_cycles(5, [], [False] * 5, counts)
print(f"counted cycles of all 120 orderings of 5: {counts[1:]}")
