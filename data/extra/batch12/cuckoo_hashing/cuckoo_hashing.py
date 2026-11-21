def h1(k):
    return k % 7

def h2(k):
    return (k // 7) % 7

a = [-1] * 7
b = [-1] * 7

def insert(key):
    k = key
    path = []
    for kick in range(8):
        i = h1(k)
        if a[i] < 0:
            a[i] = k
            return f"{key} placed after {kick} kicks {path}"
        moved = a[i]
        a[i] = k
        path.append(moved)
        j = h2(moved)
        if b[j] < 0:
            b[j] = moved
            return f"{key} placed after {kick + 1} kicks {path}"
        k = b[j]
        b[j] = moved
        path.append(k)
    return f"{key} failed, {k} left homeless {path}"

def find(key):
    return a[h1(key)] == key or b[h2(key)] == key

for k in [20, 50, 53, 75, 100, 67, 105, 3, 36, 39]:
    print(insert(k))
print(f"table A: {a}")
print(f"table B: {b}")
for k in [53, 36, 40]:
    print(f"find {k}: {str(find(k)).lower()}")
