def turan_edges(n, r):
    sq = 0
    for i in range(r):
        size = n // r + (1 if i < n % r else 0)
        sq += size * size
    return (n * n - sq) // 2

def has_triangle(n, mask, idx):
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if (mask >> idx[a][b]) & 1 and (mask >> idx[b][c]) & 1 and (mask >> idx[a][c]) & 1:
                    return True
    return False

def brute(n):
    idx = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            idx[i][j] = k
            idx[j][i] = k
            k += 1
    best = 0
    for mask in range(1 << k):
        bits = bin(mask).count("1")
        if bits > best and not has_triangle(n, mask, idx):
            best = bits
    return best

print("  n  no triangle  no K4  no K5")
for n in range(3, 11):
    print(f"{n:>3} {turan_edges(n, 2):>12} {turan_edges(n, 3):>6} {turan_edges(n, 4):>6}")
for n in range(4, 7):
    print(f"brute force n = {n}: {brute(n)} edges, Mantel n*n/4 = {n * n // 4}")
