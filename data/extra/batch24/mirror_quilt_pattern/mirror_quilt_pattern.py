state = 8080
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
fa = {'<': '>', '>': '<'}; fd = {'^': 'v', 'v': '^'}
tiles = ['<', '>', '^', 'v', 'o', '.']
quarter = [[tiles[below(len(tiles))] for c in range(4)] for r in range(4)]
top = []
for row in quarter:
    full = list(row) + [fa.get(row[3 - k], row[3 - k]) for k in range(4)]
    top.append(full)
quilt = list(top) + [[fd.get(ch, ch) for ch in top[3 - k]] for k in range(4)]
counts = {}
for row in quilt:
    print("".join(row))
    for ch in row: counts[ch] = counts.get(ch, 0) + 1
print(", ".join(f"{t} {counts.get(t, 0)}" for t in tiles))
