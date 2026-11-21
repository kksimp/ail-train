def carry(prev, prev_blame, cur, rev):
    n, m = len(prev), len(cur)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = dp[i + 1][j + 1] + 1 if prev[i] == cur[j] else max(dp[i + 1][j], dp[i][j + 1])
    blame = [rev] * m
    a = b = 0
    while a < n and b < m:
        if prev[a] == cur[b]:
            blame[b] = prev_blame[a]
            a += 1
            b += 1
        elif dp[a + 1][b] >= dp[a][b + 1]:
            a += 1
        else:
            b += 1
    return blame

authors = ["ann", "bo", "cy"]
revs = [["fn total(xs)", "    t = 0", "    for x in xs", "        t = t + x", "    return t"], ["fn total(xs)", "    t = 0", "    for x in xs", "        if x > 0", "            t = t + x", "    return t"], ["fn total(xs, lo)", "    t = 0", "    for x in xs", "        if x > lo", "            t = t + x", "    return t"]]
blame = [0, 0, 0, 0, 0]
for r in range(1, len(revs)):
    blame = carry(revs[r - 1], blame, revs[r], r)
last = revs[-1]
for k in range(len(last)):
    print(f"r{blame[k] + 1} {authors[blame[k]]:<3} | {last[k]}")
for r in range(len(authors)):
    print(f"{authors[r]} owns {sum(1 for x in blame if x == r)} lines")
