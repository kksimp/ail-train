def prefix_function(cs):
    n = len(cs)
    pi = [0] * n
    for i in range(1, n):
        k = pi[i - 1]
        while k > 0 and cs[i] != cs[k]:
            k = pi[k - 1]
        if cs[i] == cs[k]:
            k += 1
        pi[i] = k
    return pi

for s in ["abcabcabc", "abab", "abcab", "aaaaaa", "drumdrumdr", "xyz"]:
    pi = prefix_function(s)
    n = len(s)
    p = n - pi[n - 1]
    borders = []
    b = pi[n - 1]
    while b > 0:
        borders.append(s[:b])
        b = pi[b - 1]
    shown = "none" if not borders else ", ".join(borders)
    unit = s[:p]
    rep = f"{unit} x {n // p}" if n % p == 0 else "not a whole repeat"
    print(f"{s:<11} period {p}: {rep}; borders {shown}")
