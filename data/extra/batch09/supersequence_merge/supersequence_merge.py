def merge(a, b):
    la, lb = len(a), len(b)
    dp = [[0] * (lb + 1) for _ in range(la + 1)]
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    out = []
    i, j = la, lb
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            out.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            out.append(a[i - 1])
            i -= 1
        else:
            out.append(b[j - 1])
            j -= 1
    while i > 0:
        out.append(a[i - 1])
        i -= 1
    while j > 0:
        out.append(b[j - 1])
        j -= 1
    out.reverse()
    return "".join(out)

pairs = [("geek", "eke"), ("abac", "cab"), ("strand", "stranger"), ("pear", "pare"), ("abc", "xyz")]
for a, b in pairs:
    m = merge(a, b)
    saved = len(a) + len(b) - len(m)
    print(f"{a} + {b} -> {m} (length {len(m)}, {saved} shared)")
