def sweep_count(a, b, seidel):
    n = len(b)
    x = [0.0] * n
    sweeps = 0
    while sweeps < 1000:
        old = x[:]
        for i in range(n):
            s = b[i]
            for j in range(n):
                if j != i:
                    v = x[j] if seidel else old[j]
                    s -= a[i][j] * v
            x[i] = s / a[i][i]
        sweeps += 1
        change = 0.0
        for i in range(n):
            if abs(x[i] - old[i]) > change:
                change = abs(x[i] - old[i])
        if change < 0.000000001:
            break
    return x + [float(sweeps)]

a = [[10.0, -1.0, 2.0, 0.0], [-1.0, 11.0, -1.0, 3.0], [2.0, -1.0, 10.0, -1.0], [0.0, 3.0, -1.0, 8.0]]
b = [6.0, 25.0, -11.0, 15.0]
for seidel in [False, True]:
    r = sweep_count(a, b, seidel)
    name = "Gauss-Seidel" if seidel else "Jacobi"
    print(f"{name:<12} {int(r[4]):>3} sweeps: [{r[0]:.6f}, {r[1]:.6f}, {r[2]:.6f}, {r[3]:.6f}]")
c = [[4.0, 1.0, 1.0], [1.0, 5.0, 2.0], [1.0, 2.0, 6.0]]
d = [7.0, -8.0, 6.0]
for seidel in [False, True]:
    r = sweep_count(c, d, seidel)
    name = "Gauss-Seidel" if seidel else "Jacobi"
    print(f"{name:<12} {int(r[3]):>3} sweeps: [{r[0]:.6f}, {r[1]:.6f}, {r[2]:.6f}]")
