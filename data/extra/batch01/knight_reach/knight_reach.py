from collections import deque
N = 8
d = [[-1] * N for _ in range(N)]; d[0][0] = 0
q = deque([(0, 0)])
J = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
while q:
    c, r = q.popleft()
    for dc, dr in J:
        nc, nr = c + dc, r + dr
        if 0 <= nc < N and 0 <= nr < N and d[nr][nc] == -1:
            d[nr][nc] = d[r][c] + 1; q.append((nc, nr))
for k in range(8):
    r = 7 - k
    print(f"{r + 1} " + " ".join(map(str, d[r])))
far = max(max(row) for row in d)
print(f"farthest from a1: {far} moves, at " + " ".join(f"{chr(97 + c)}{r + 1}" for r in range(N) for c in range(N) if d[r][c] == far))
print(f"a1 to h8: {d[7][7]}")
