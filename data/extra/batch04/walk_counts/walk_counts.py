A = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
mul = lambda a, b: [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
p = A
for l in range(1, 5):
    print(f"length {l}: A->D {p[0][3]}, B->B {p[1][1]}, total {sum(sum(r) for r in p)}"); p = mul(p, A)
print("towns: A B C D")
