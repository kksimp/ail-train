def rosen(p):
    a = 1.0 - p[0]
    b = p[1] - p[0] * p[0]
    return a * a + 100.0 * b * b
def towards(a, b, t):
    return [a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])]
s = [[-1.2, 1.0], [-1.0, 1.0], [-1.2, 1.2]]
for it in range(1, 161):
    for i in range(2):
        for j in range(2 - i):
            if rosen(s[j + 1]) < rosen(s[j]):
                s[j], s[j + 1] = s[j + 1], s[j]
    c = [(s[0][0] + s[1][0]) / 2.0, (s[0][1] + s[1][1]) / 2.0]
    w = s[2]
    r = towards(c, w, -1.0)
    fr = rosen(r)
    if fr < rosen(s[0]):
        e = towards(c, w, -2.0)
        s[2] = e if rosen(e) < fr else r
    elif fr < rosen(s[1]):
        s[2] = r
    else:
        k = towards(c, w, 0.5)
        if rosen(k) < rosen(w):
            s[2] = k
        else:
            s[1] = towards(s[0], s[1], 0.5)
            s[2] = towards(s[0], s[2], 0.5)
    if it % 20 == 0:
        print(f"step {it:>3}: best ({s[0][0]:.4f}, {s[0][1]:.4f}), f = {rosen(s[0]):.5f}")
print("the true minimum is f(1, 1) = 0")
