for xs in [[3, 7, 7, 2, 9], [1, 2, 3, 4], [5, 5, 1, 1, 3], [10], [4, 8, 6, 2]]:
    s = sorted(xs); n = len(s)
    if n % 2: med = f"{s[n // 2]}"
    else:
        t = s[n // 2 - 1] + s[n // 2]
        med = f"{t // 2}" if t % 2 == 0 else f"{t // 2}.5"
    c = {}
    for x in xs: c[x] = c.get(x, 0) + 1
    b = max(c.values())
    md = sorted(k for k in c if c[k] == b)
    print(f"{','.join(map(str, xs))}: mean {sum(xs) / len(xs):.2f}, median {med}, modes {'/'.join(map(str, md))}")
