def da(p):
    n, w, c, s = p, 1, 9, 1
    while n > w * c: n -= w * c; w += 1; c *= 10; s *= 10
    return int(str(s + (n - 1) // w)[(n - 1) % w])
for p in [1, 9, 10, 11, 15, 190, 191, 192, 365]: print(f"position {p}: {da(p)}")
b = "".join(str(k) for k in range(1, 201)); print(f"matches brute force: {'true' if all(int(b[p - 1]) == da(p) for p in [1, 50, 189, 190, 300, 492]) else 'false'}")
