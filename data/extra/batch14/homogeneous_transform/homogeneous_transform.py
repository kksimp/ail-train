def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def apply(m, pts):
    return " ".join(f"({m[0][0] * x + m[0][1] * y + m[0][2]}, {m[1][0] * x + m[1][1] * y + m[1][2]})" for x, y in pts)
def translate(dx, dy):
    return [[1, 0, dx], [0, 1, dy], [0, 0, 1]]
def turn90():
    return [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
def scale(s):
    return [[s, 0, 0], [0, s, 0], [0, 0, 1]]
square = [[0, 0], [2, 0], [2, 1], [0, 1]]
print(f"tile corners:          {apply(scale(1), square)}")
print(f"turn 90:               {apply(turn90(), square)}")
print(f"turn, then move (5,0): {apply(matmul(translate(5, 0), turn90()), square)}")
print(f"move (5,0), then turn: {apply(matmul(turn90(), translate(5, 0)), square)}")
pivot = matmul(translate(2, 1), matmul(turn90(), translate(-2, -1)))
print(f"turn about (2,1):      {apply(pivot, square)}")
print(f"pivot matrix {pivot}")
big = matmul(scale(3), pivot)
print(f"then triple:           {apply(big, square)}")
four = turn90()
for k in range(3):
    four = matmul(four, turn90())
print(f"four quarter turns give the identity: {'true' if four == scale(1) else 'false'}")
