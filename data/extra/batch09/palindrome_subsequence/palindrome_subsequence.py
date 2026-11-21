def table(cs):
    n = len(cs)
    dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for size in range(2, n + 1):
        for i in range(0, n - size + 1):
            j = i + size - 1
            if cs[i] == cs[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp

def longest(s):
    cs = s
    dp = table(cs)
    left = []
    middle = ""
    i = 0
    j = len(cs) - 1
    while i <= j:
        if i == j:
            middle = cs[i]
            break
        if cs[i] == cs[j]:
            left.append(cs[i])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    return "".join(left) + middle + "".join(reversed(left))

for w in ["character", "racecar", "agbdba", "programming", "abcd", "banana"]:
    p = longest(w)
    need = len(w) - len(p)
    print(f"{w:<12} longest palindromic subsequence {p:<8} ({len(p)}), insert {need} to make a palindrome")
