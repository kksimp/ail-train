def enc(d):
    return [d[0] ^ d[1] ^ d[3], d[0] ^ d[2] ^ d[3], d[0], d[1] ^ d[2] ^ d[3], d[1], d[2], d[3]]
def syn(c):
    return (c[0] ^ c[2] ^ c[4] ^ c[6]) + (c[1] ^ c[2] ^ c[5] ^ c[6]) * 2 + (c[3] ^ c[4] ^ c[5] ^ c[6]) * 4
show = lambda b: "".join(map(str, b))
for d in [[1, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]]:
    c = enc(d)
    for f in [0, 3, 7]:
        n = list(c)
        if f: n[f - 1] = 1 - n[f - 1]
        p = syn(n); x = list(n)
        if p: x[p - 1] = 1 - x[p - 1]
        print(f"{show(d)} -> {show(c)}, flip {f}: {show(n)} syndrome {p} -> {show([x[2], x[4], x[5], x[6]])}")
