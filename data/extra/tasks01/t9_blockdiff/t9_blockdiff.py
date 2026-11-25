import sys

lines = sys.stdin.read().split("\n")
if lines and lines[-1] == "":
    lines.pop()
if "---" in lines:
    p = lines.index("---")
    a, b = lines[:p], lines[p + 1:]
else:
    a, b = lines, []
n, m = len(a), len(b)
L = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if a[i] == b[j]:
            L[i][j] = L[i + 1][j + 1] + 1
        else:
            L[i][j] = max(L[i + 1][j], L[i][j + 1])
i = j = 0
add = rem = same = 0
while i < n or j < m:
    if i < n and j < m and a[i] == b[j]:
        print("  " + a[i])
        i += 1
        j += 1
        same += 1
    elif j == m or (i < n and L[i + 1][j] >= L[i][j + 1]):
        print("- " + a[i])
        i += 1
        rem += 1
    else:
        print("+ " + b[j])
        j += 1
        add += 1
print("+%d -%d =%d" % (add, rem, same))
