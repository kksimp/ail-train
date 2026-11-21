a = ["buy milk", "walk dog", "call mum", "fix bike", "read book"]; b = ["buy milk", "call mum", "fix bike tyre", "read book", "water plants"]
n, m = len(a), len(b); t = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        t[i][j] = t[i + 1][j + 1] + 1 if a[i] == b[j] else max(t[i + 1][j], t[i][j + 1])
x = y = 0
while x < n and y < m:
    if a[x] == b[y]: print(f"  {a[x]}"); x += 1; y += 1
    elif t[x + 1][y] >= t[x][y + 1]: print(f"- {a[x]}"); x += 1
    else: print(f"+ {b[y]}"); y += 1
for k in range(x, n): print(f"- {a[k]}")
for k in range(y, m): print(f"+ {b[k]}")
