def distinct_count(s):
    dp = [1]
    last = {}
    cs = list(s)
    for i in range(1, len(cs) + 1):
        c = cs[i - 1]
        v = dp[i - 1] * 2
        if c in last:
            v -= dp[last[c] - 1]
        dp.append(v)
        last[c] = i
    return dp[len(cs)]

def ways(text, word):
    w = list(word)
    dp = [1] + [0] * len(w)
    for c in text:
        j = len(w)
        while j >= 1:
            if w[j - 1] == c:
                dp[j] += dp[j - 1]
            j -= 1
    return dp[len(w)]

for s in ["abc", "aba", "aaa", "banana", "mississippi", "abcdefghij"]:
    print(f"{s:<12} {distinct_count(s)} distinct subsequences (with the empty one)")
for t, w in [("rabbbit", "rabbit"), ("babgbag", "bag"), ("subsequence", "sue"), ("aaaaa", "aa")]:
    print(f"{w} inside {t}: {ways(t, w)} ways")
