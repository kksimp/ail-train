def elementary(roots):
    e = [1]
    for r in roots:
        nx = e + [0]
        for i in range(len(e)):
            nx[i + 1] += r * e[i]
        e = nx
    return e
def power_sums(e, upto):
    n = len(e) - 1
    p = [n]
    for k in range(1, upto + 1):
        t = 0
        for i in range(1, k):
            if i <= n:
                t += (1 if i % 2 == 1 else -1) * e[i] * p[k - i]
        if k <= n:
            t += (1 if k % 2 == 1 else -1) * k * e[k]
        p.append(t)
    return p
def back(p, n):
    e = [1]
    for k in range(1, n + 1):
        t = 0
        for i in range(1, k + 1):
            t += (1 if i % 2 == 1 else -1) * e[k - i] * p[i]
        e.append(t // k)
    return e
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
roots = [1, 2, 3, 5]
e = elementary(roots)
print(f"roots {fl(roots)}: e1..e4 = {fl(e[1:])}")
p = power_sums(e, 6)
for k in range(1, 7):
    direct = sum(r ** k for r in roots)
    print(f"p{k} from coefficients {p[k]:>6}, summed directly {direct:>6}")
print(f"back from power sums: {fl(back(p, 4)[1:])}")
cubic = power_sums([1, 6, 11, 6], 2)
print(f"x^3 - 6x^2 + 11x - 6: sum of squared roots is {cubic[2]}")
