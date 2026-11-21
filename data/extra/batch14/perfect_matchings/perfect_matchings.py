def ryser(a):
    n = len(a)
    total = 0
    for mask in range(1, 1 << n):
        prod = 1
        for i in range(n):
            row = 0
            for j in range(n):
                if (mask >> j) & 1 == 1:
                    row += a[i][j]
            prod *= row
        bits = bin(mask).count("1")
        sign = 1 if (n - bits) % 2 == 0 else -1
        total += sign * prod
    return total

def search(a, i, used):
    if i == len(a):
        return 1
    c = 0
    for j in range(len(a)):
        if a[i][j] == 1 and (used >> j) & 1 == 0:
            c += search(a, i + 1, used | (1 << j))
    return c

workers = ["Ana", "Bo", "Cy", "Di", "Ed"]
allowed = [[1, 1, 0, 0, 1], [0, 1, 1, 0, 0], [1, 0, 1, 1, 0], [0, 0, 1, 1, 1], [1, 1, 0, 1, 0]]
for i in range(5):
    print(f"{workers[i]:<4} [{', '.join(str(x) for x in allowed[i])}]")
print(f"Ryser: {ryser(allowed)} rotas, search: {search(allowed, 0, 0)} rotas")
for n in range(2, 8):
    d = [[0 if i == j else 1 for j in range(n)] for i in range(n)]
    print(f"nobody on own shift, n = {n}: {ryser(d)}")
