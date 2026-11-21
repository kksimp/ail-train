def count_true(vals, ops):
    n = len(vals)
    t = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        if vals[i]:
            t[i][i] = 1
        else:
            f[i][i] = 1
    for gap in range(1, n):
        for i in range(0, n - gap):
            j = i + gap
            for k in range(i, j):
                lt = t[i][k]; lf = f[i][k]; rt = t[k + 1][j]; rf = f[k + 1][j]
                all_ways = (lt + lf) * (rt + rf)
                if ops[k] == '&':
                    yes = lt * rt
                elif ops[k] == '|':
                    yes = all_ways - lf * rf
                else:
                    yes = lt * rf + lf * rt
                t[i][j] += yes
                f[i][j] += all_ways - yes
    return t[0][n - 1]

def parse(expr):
    vals = []
    ops = []
    for ch in expr:
        if ch == 'T' or ch == 'F':
            vals.append(ch == 'T')
        else:
            ops.append(ch)
    return count_true(vals, ops)

for e in ["T|F&T", "T^F|F", "T&F^T|F", "F|T^F&T|F", "T^T^T^T", "F&F|T^T&F|T"]:
    print(f"{e:<12} {parse(e):>4} true bracketings")
