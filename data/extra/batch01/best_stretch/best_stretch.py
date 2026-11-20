def best(xs):
    if not xs: return None
    b = (xs[0], 0, 0); cur = xs[0]; cs = 0
    for i in range(1, len(xs)):
        if cur < 0:
            cur, cs = xs[i], i
        else:
            cur += xs[i]
        if cur > b[0]:
            b = (cur, cs, i)
    return b
for xs in [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [3, -1, 2], [-4, -2, -7], [5], []]:
    label = "[" + " ".join(map(str, xs)) + "]"
    s = best(xs)
    print(f"{label}: {s[0]} from day {s[1] + 1} to {s[2] + 1}" if s else f"{label}: no days")
