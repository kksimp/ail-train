import sys
L = sys.stdin.read().split("\n")
L += [""] * (4 - len(L))
W, H = map(int, L[0].split())
def cells(s):
    return [tuple(map(int, t.split(","))) for t in s.split()]
snake = cells(L[1])
food = cells(L[2])
moves = L[3].strip()
D = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
result = "alive"
score = 0
for k, m in enumerate(moves, 1):
    if m not in D:
        result = f"over bad move at step {k}"; break
    hx, hy = snake[0]
    nx, ny = hx + D[m][0], hy + D[m][1]
    if not (0 <= nx < W and 0 <= ny < H):
        result = f"over wall at step {k}"; break
    if food and food[0] == (nx, ny):
        food.pop(0); score += 1
        snake.insert(0, (nx, ny))
    else:
        body = snake[:-1]
        if (nx, ny) in body:
            result = f"over self at step {k}"; break
        snake = [(nx, ny)] + body
print("result", result)
print(f"length {len(snake)} score {score}")
g = [["."] * W for _ in range(H)]
if food:
    g[food[0][1]][food[0][0]] = "*"
for i, (x, y) in enumerate(snake):
    g[y][x] = "H" if i == 0 else "o"
for row in g:
    print("".join(row))
