def fc(n, s):
    sl = fa = s
    while True:
        if n[fa] < 0 or n[n[fa]] < 0: return None
        sl = n[sl]; fa = n[n[fa]]
        if sl == fa: break
    a, b = s, sl
    while a != b: a = n[a]; b = n[b]
    ln = 1; c = n[a]
    while c != a: c = n[c]; ln += 1
    return a, ln
for t in [[1, 2, 3, 4, 5, 2], [1, 2, 3, -1], [3, 0, 1, 1], [0]]:
    f = fc(t, 0)
    print(f"{t}: cycle starts at {f[0]}, length {f[1]}" if f else f"{t}: no cycle")
