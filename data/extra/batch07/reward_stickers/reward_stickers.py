def st(c):
    n = len(c); s = [1] * n
    for i in range(1, n):
        if c[i] > c[i - 1]: s[i] = s[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if c[i] > c[i + 1] and s[i] <= s[i + 1]: s[i] = s[i + 1] + 1
    return s
for L in [[1, 0, 2], [1, 2, 2], [5, 4, 3, 2, 1], [1, 3, 4, 5, 2], [2, 2, 2, 2], [1, 6, 10, 8, 7, 3, 2]]:
    s = st(L); print(f"scores {' '.join(map(str, L))} -> stickers {' '.join(map(str, s))} (total {sum(s)})")
