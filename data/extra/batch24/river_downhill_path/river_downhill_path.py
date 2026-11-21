state = 7
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def lowest_step(h, r, c):
    best = [r, c]
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(h) and 0 <= cc < len(h[0]) and h[rr][cc] < h[best[0]][best[1]]: best = [rr, cc]
    return best
h = []
for r in range(8):
    h.append([40 - 3 * r - 2 * c + below(6) for c in range(10)])
path = [[0, 0]]
while True:
    here = path[-1]
    nxt = lowest_step(h, here[0], here[1])
    if nxt == here: break
    path.append(nxt)
for r in range(8):
    print("".join("*" if [r, c] in path else "." for c in range(10)))
last = path[-1]
print(f"{len(path)} cells from height {h[0][0]} down to {h[last[0]][last[1]]}, pond at row {last[0]}, column {last[1]}")
