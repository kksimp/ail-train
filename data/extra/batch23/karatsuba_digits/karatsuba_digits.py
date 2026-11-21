def digits(s):
    return [ord(c) - 48 for c in s][::-1]

def kara(a, b, count):
    n = len(a)
    size = 2 * n
    out = [0 for i in range(size)]
    if n <= 4:
        for i in range(n):
            for j in range(n):
                count[0] += 1
                out[i + j] += a[i] * b[j]
        return out
    half = n // 2
    a0 = a[0:half]
    a1 = a[half:n]
    b0 = b[0:half]
    b1 = b[half:n]
    z0 = kara(a0, b0, count)
    z2 = kara(a1, b1, count)
    sa = [a0[i] + a1[i] for i in range(half)]
    sb = [b0[i] + b1[i] for i in range(half)]
    z1 = kara(sa, sb, count)
    for i in range(n):
        out[i] += z0[i]
        out[i + half] += z1[i] - z0[i] - z2[i]
        out[i + n] += z2[i]
    return out

def show(coeffs):
    cs = list(coeffs)
    cs.extend([0, 0, 0])
    ds = []
    carry = 0
    for c in cs:
        v = c + carry
        ds.append(v % 10)
        carry = v // 10
    while len(ds) > 1 and ds[-1] == 0:
        ds.pop()
    return "".join(str(d) for d in reversed(ds))

pi = "3141592653589793238462643383279502884197169399375105820974944592"
e = "2718281828459045235360287471352662497757247093699959574966967627"
for pair in [["1234", "5678"], [pi[0:16], e[0:16]], [pi[0:32], e[0:32]], [pi, e]]:
    a = digits(pair[0])
    b = digits(pair[1])
    count = [0]
    product = show(kara(a, b, count))
    assert int(product) == int(pair[0]) * int(pair[1])
    print(f"{len(a)} digits: {pair[0]} x {pair[1]}")
    print(f"  = {product} ({count[0]} digit products, schoolbook {len(a) * len(b)})")
assert show(kara(digits("1200"), digits("0034"), [0])) == "40800"
