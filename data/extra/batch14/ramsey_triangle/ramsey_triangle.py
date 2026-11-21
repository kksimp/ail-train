def edge_index(n):
    idx = [[0] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            idx[i][j] = k
            idx[j][i] = k
            k += 1
    return idx

def has_mono(n, mask, idx):
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                x = (mask >> idx[a][b]) & 1
                y = (mask >> idx[b][c]) & 1
                z = (mask >> idx[a][c]) & 1
                if x == y and y == z:
                    return True
    return False

def free_count(n):
    idx = edge_index(n)
    edges = n * (n - 1) // 2
    return sum(1 for mask in range(1 << edges) if not has_mono(n, mask, idx))

for n in range(3, 7):
    edges = n * (n - 1) // 2
    f = free_count(n)
    total = 1 << edges
    verdict = "a one-colour triangle is forced" if f == 0 else "can be avoided"
    print(f"K{n}: {edges} edges, {total} colourings, {f} without a one-colour triangle: {verdict}")
idx = edge_index(5)
ring = 0
for i in range(5):
    ring |= 1 << idx[i][(i + 1) % 5]
print(f"pentagon red, pentagram blue has a triangle: {'true' if has_mono(5, ring, idx) else 'false'}")
print("so R(3,3) = 6: any six people hold three mutual friends or three mutual strangers")
