I = [("stove", 4, 40), ("tent", 9, 90), ("lamp", 2, 15), ("rope", 3, 18), ("food", 5, 60), ("radio", 3, 22)]; L = 15; n = len(I)
B = [[0] * (L + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = I[i - 1][1], I[i - 1][2]
    for c in range(L + 1):
        B[i][c] = B[i - 1][c]
        if w <= c and B[i - 1][c - w] + v > B[i][c]: B[i][c] = B[i - 1][c - w] + v
c = L; ch = []; i = n
while i > 0:
    if B[i][c] != B[i - 1][c]: ch.append(I[i - 1][0]); c -= I[i - 1][1]
    i -= 1
ch.reverse(); print(f"value {B[n][L]}, weight {L - c}: {', '.join(ch)}")
