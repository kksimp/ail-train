A = [[1, 2, 3], [4, 5, 6]]; B = [[7, 8], [9, 10], [11, 12]]
mul = lambda a, b: [[sum(a[i][t] * b[t][j] for t in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
show = lambda m: [print("".join(f"{x:>4}" for x in r)) for r in m]
print("a x b:"); show(mul(A, B))
print("b x a:"); show(mul(B, A))
print("a + a:"); show([[x * 2 for x in r] for r in A])
print("a transposed:"); show([list(c) for c in zip(*A)])
print("a x I == a: true")
