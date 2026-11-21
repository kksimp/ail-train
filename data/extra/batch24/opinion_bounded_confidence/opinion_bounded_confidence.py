state = 1001
def below(n):
    global state
    state = (state * 1103515245 + 12345) % 2147483648
    return (state // 65536) % n
def camps(views):
    s = sorted(views); n = 1
    for i in range(1, len(s)):
        if s[i] - s[i - 1] > 20: n += 1
    return n
views = [3, 12, 25, 31, 44, 52, 67, 71, 88, 97]
for talk in range(1, 401):
    a = below(10); b = below(10)
    d = views[b] - views[a]
    if a != b and abs(d) <= 20:
        step = abs(d) // 4
        if d > 0:
            views[a] += step; views[b] -= step
        else:
            views[a] -= step; views[b] += step
    if talk % 100 == 0:
        print(f"after {talk} talks: {sorted(views)}, {camps(views)} camps")
