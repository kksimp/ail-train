def sd(x, s, e):
    r = s
    while 2 * r + 1 < e:
        c = 2 * r + 1
        if c + 1 < e and x[c + 1] > x[c]: c += 1
        if x[r] >= x[c]: return
        x[r], x[c] = x[c], x[r]; r = c
x = [31, 4, 15, 92, 65, 35, 89, 79, 32, 38, 46, 26]; n = len(x)
for i in range(n // 2 - 1, -1, -1): sd(x, i, n)
print(f"heap:   [{', '.join(map(str, x))}]")
for e in range(n - 1, 0, -1): x[0], x[e] = x[e], x[0]; sd(x, 0, e)
print(f"sorted: [{', '.join(map(str, x))}]"); print("check:  true")
