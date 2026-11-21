def ext_gcd(a, b):
    if b == 0:
        return [a, 1, 0]
    r = ext_gcd(b, a % b)
    return [r[0], r[2], r[1] - (a // b) * r[2]]

def crt(rems, mods):
    x = rems[0]
    m = mods[0]
    for i in range(1, len(mods)):
        mi = mods[i]
        g = ext_gcd(m, mi)
        inv = ((g[1] % mi) + mi) % mi
        diff = (((rems[i] - x) % mi) + mi) % mi
        k = diff * inv % mi
        x = x + m * k
        m = m * mi
    return [x, m]

systems = [[[2, 3, 2], [3, 5, 7]], [[1, 2, 3, 4], [2, 3, 5, 7]], [[1, 1, 1, 0], [3, 4, 5, 7]], [[5, 7, 11], [11, 13, 17]]]
for s in systems:
    rems, mods = s
    r = crt(rems, mods)
    parts = [f"{r[0] % mods[i]} mod {mods[i]}" for i in range(len(mods))]
    print(f"x = {r[0]} (mod {r[1]}): {', '.join(parts)}")
eggs = crt([1, 1, 1, 0], [3, 4, 5, 7])
print(f"smallest egg basket: {eggs[0]}, next {eggs[0] + eggs[1]}")
