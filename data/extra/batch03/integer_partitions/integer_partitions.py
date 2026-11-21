def cp(n):
    w = [0] * (n + 1); w[0] = 1
    for p in range(1, n + 1):
        for t in range(p, n + 1): w[t] += w[t - p]
    return w[n]
print([cp(n) for n in range(1, 13)])
print(f"p(50) = {cp(50)}, p(100) = {cp(100)}")
out = []
def lp(n, m, pre):
    if n == 0: out.append("+".join(map(str, pre))); return
    for p in range(min(n, m), 0, -1): lp(n - p, p, pre + [p])
lp(6, 6, [])
print(f"6 has {len(out)}: {', '.join(out)}")
