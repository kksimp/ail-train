def swings(quota, w):
    n = len(w)
    out = [0] * n
    for mask in range(1 << n):
        total = sum(w[i] for i in range(n) if (mask >> i) & 1)
        if total >= quota:
            for i in range(n):
                if (mask >> i) & 1 and total - w[i] < quota:
                    out[i] += 1
    return out
def fl(xs):
    return "[" + ", ".join(map(str, xs)) + "]"
for quota, w in [(51, [49, 49, 2]), (6, [4, 3, 2, 1]), (12, [5, 5, 3, 2, 2, 1]), (9, [9, 3, 2, 1]), (16, [8, 8, 4, 4, 1])]:
    s = swings(quota, w)
    tot = sum(s)
    shares = [x * 100.0 / tot for x in s]
    joined = " ".join(f"{w[i]}:{shares[i]:.1f}%" for i in range(len(w)))
    print(f"quota {quota:>2} weights {fl(w)}: swings {fl(s)} -> {joined}")
