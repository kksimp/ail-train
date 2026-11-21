def eulerian(size):
    a = [[1]]
    for n in range(1, size + 1):
        row = []
        for k in range(n):
            left = (k + 1) * a[n - 1][k] if k < len(a[n - 1]) else 0
            right = (n - k) * a[n - 1][k - 1] if k > 0 else 0
            row.append(left + right)
        a.append(row)
    return a

def count_ascents(perm, used, n, counts):
    if len(perm) == n:
        asc = sum(1 for i in range(1, n) if perm[i] > perm[i - 1])
        counts[asc] += 1
        return
    for v in range(n):
        if not used[v]:
            used[v] = True
            perm.append(v)
            count_ascents(perm, used, n, counts)
            perm.pop()
            used[v] = False

a = eulerian(7)
for n in range(1, 8):
    print(f"n = {n}: {a[n]} sum {sum(a[n])}")
for n in [4, 5, 6]:
    counts = [0] * n
    count_ascents([], [False] * n, n, counts)
    print(f"brute force n = {n}: {counts}")
