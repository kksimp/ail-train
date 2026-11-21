def motzkin(n):
    m = [1, 1]
    for k in range(2, n + 1):
        v = m[k - 1]
        for i in range(0, k - 1):
            v += m[i] * m[k - 2 - i]
        m.append(v)
    return m

def walks(n, level, path, out):
    if level < 0 or level > n:
        return
    if n == 0:
        if level == 0:
            out.append(path)
        return
    walks(n - 1, level + 1, path + "U", out)
    walks(n - 1, level, path + "F", out)
    walks(n - 1, level - 1, path + "D", out)

m = motzkin(12)
print(f"M(0..12) = {m}")
for n in range(1, 9):
    out = []
    walks(n, 0, "", out)
    print(f"length {n}: {len(out)} walks generated, recurrence {m[n]}")
four = []
walks(4, 0, "", four)
print(f"length 4: {' '.join(four)}")
