def lis(xs):
    o = [1] * len(xs)
    for i in range(len(xs)):
        for j in range(i):
            if xs[j] < xs[i] and o[j] + 1 > o[i]: o[i] = o[j] + 1
    return o
def bit(xs):
    u = lis(xs); d = lis(xs[::-1])[::-1]
    return max((u[i] + d[i] - 1 for i in range(len(xs))), default=0)
for xs in [[1, 11, 2, 10, 4, 5, 2, 1], [12, 11, 40, 5, 3, 1], [80, 60, 30, 40, 20, 10], [1, 2, 3], []]:
    print(f"{' '.join(map(str, xs))}: {bit(xs)}")
