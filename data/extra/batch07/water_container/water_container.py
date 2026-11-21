def mw(h):
    i = 0; j = len(h) - 1; b = (0, 0, 0)
    while i < j:
        a = min(h[i], h[j]) * (j - i)
        if a > b[0]: b = (a, i, j)
        if h[i] < h[j]: i += 1
        else: j -= 1
    return b
for W in [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1], [4, 3, 2, 1, 4], [1, 2, 1], [2, 3, 10, 5, 7, 8, 9]]:
    b = mw(W); print(f"[{' '.join(map(str, W))}]: {b[0]} between walls {b[1] + 1} and {b[2] + 1}")
