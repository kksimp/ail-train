def build(t, p, n, k, a, out):
    if t > n:
        if n % p == 0:
            for i in range(1, p + 1):
                out.append(a[i])
        return
    a[t] = a[t - p]
    build(t + 1, p, n, k, a, out)
    for j in range(a[t - p] + 1, k):
        a[t] = j
        build(t + 1, t, n, k, a, out)

def de_bruijn(k, n):
    a = [0] * (n + 1)
    out = []
    build(1, 1, n, k, a, out)
    return out

def distinct_windows(seq, n):
    seen = set()
    for i in range(len(seq)):
        seen.add("".join(str(seq[(i + j) % len(seq)]) for j in range(n)))
    return len(seen)

for k, n in [[2, 3], [2, 4], [3, 2], [3, 3], [4, 2]]:
    s = de_bruijn(k, n)
    print(f"B({k}, {n}) length {len(s)}: {''.join(str(x) for x in s)}, distinct windows {distinct_windows(s, n)}")
code = de_bruijn(10, 3)
print(f"a 3-digit keypad needs {len(code) + 2} presses instead of {3 * 1000}")
